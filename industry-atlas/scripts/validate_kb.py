#!/usr/bin/env python3
"""Validate an Industry Atlas knowledge base.

Checks every .md file for YAML frontmatter (required fields, allowed type and
region values, first tag = industry tag, ISO `updated` date not in the future,
sources list), relative links and heading anchors. Also scans all text files
for leaked secrets.

Usage:
    python3 tools/validate_kb.py                          # errors -> exit code 1
    python3 tools/validate_kb.py --stale 90               # also list files not updated for 90+ days
    python3 tools/validate_kb.py --expect-date 2026-09-14 # initial build: every file carries this date
    python3 tools/validate_kb.py --mixed-script           # flag words mixing Latin and Cyrillic letters
    python3 tools/validate_kb.py --warnings               # list files whose sources list is still empty
    python3 tools/validate_kb.py --root path/to/atlas     # run from anywhere

Requires PyYAML: pip install pyyaml
"""
import argparse
import datetime as dt
import os
import re
import sys
import unicodedata

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import atlas_common as ac  # noqa: E402

REQUIRED = ["title", "type", "tags", "region", "updated", "sources"]
MIXED_SCRIPT = re.compile(r"\b\w*(?:[a-zA-Z][а-яА-ЯёЁ]|[а-яА-ЯёЁ][a-zA-Z])\w*\b")
SECRET_PATTERNS = re.compile(
    r"ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|gho_[A-Za-z0-9]{30,}"
    r"|sk-(?:ant-)?[A-Za-z0-9_-]{24,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----"
)
TEXT_EXTENSIONS = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".opml", ".xml", ".csv", ".html", ".toml", ".cfg", ".ini", ".env"}
_anchor_cache = {}


def slug(heading):
    """GitHub-style anchor: lowercase, keep letters, digits, spaces, '-' and '_'."""
    kept = [ch for ch in heading.strip().lower()
            if ch in " -_" or unicodedata.category(ch)[0] in ("L", "N")]
    return "".join(kept).replace(" ", "-")


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def anchors(path):
    if path not in _anchor_cache:
        with open(path, encoding="utf-8") as f:
            body = re.sub(r"```.*?```", "", f.read(), flags=re.S)
        _anchor_cache[path] = {slug(m.group(2)) for m in re.finditer(r"^(#{1,6})\s+(.+)$", body, re.M)}
    return _anchor_cache[path]


def walk(root, extensions=None):
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and d not in ("node_modules", "__pycache__"))
        for name in sorted(files):
            if extensions is None or os.path.splitext(name)[1].lower() in extensions:
                yield os.path.join(folder, name)


def parse_date(value):
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    return dt.date.fromisoformat(str(value))


def check_frontmatter(rel, fm, raw, cfg, args, errors, warnings, stale):
    for key in REQUIRED:
        if key not in fm:
            errors.append(f"{rel}: missing {key}")
    if rel.startswith(ac.TEMPLATES_DIR + os.sep) and "{{" in raw:
        return  # card templates keep placeholders in frontmatter
    types = ac.BASE_TYPES | set(cfg["extra_types"])
    if fm.get("type") not in types:
        errors.append(f"{rel}: bad type {fm.get('type')}")
    region = fm.get("region")
    if not isinstance(region, list) or set(region) - set(cfg["region_values"]):
        errors.append(f"{rel}: bad region {region}")
    tags = fm.get("tags")
    if not isinstance(tags, list) or not tags or tags[0] != cfg["industry_tag"]:
        errors.append(f"{rel}: tags must be a list starting with {cfg['industry_tag']}")
    sources = fm.get("sources")
    if "sources" in fm and not isinstance(sources, list):
        errors.append(f"{rel}: sources must be a list")
    elif not sources:
        warnings.append(f"{rel}: sources list is empty")
    try:
        updated = parse_date(fm.get("updated"))
    except ValueError:
        errors.append(f"{rel}: updated is not YYYY-MM-DD ({fm.get('updated')})")
        return
    today = dt.date.today()
    if updated > today:
        errors.append(f"{rel}: updated is in the future ({updated})")
    if args.expect_date and str(updated) != args.expect_date:
        errors.append(f"{rel}: updated={updated}, expected {args.expect_date}")
    if args.stale and (today - updated).days >= args.stale:
        stale.append(f"{rel}: updated {updated}")


def check_links(path, rel, text, errors):
    if rel.startswith(ac.TEMPLATES_DIR + os.sep):
        return  # templates contain placeholder links
    for m in re.finditer(r"\]\(([^)\s]+)\)", strip_code(text)):
        target = m.group(1)
        if target.startswith(("http://", "https://", "mailto:")) or "{{" in target:
            continue
        path_part, _, anchor = target.partition("#")
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), path_part)) if path_part else path
        if not os.path.exists(resolved):
            errors.append(f"{rel}: broken link -> {target}")
        elif anchor and resolved.endswith(".md") and anchor not in anchors(resolved):
            errors.append(f"{rel}: broken anchor -> {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", help="atlas root (default: nearest folder with atlas.config.yaml)")
    parser.add_argument("--stale", type=int, default=0, metavar="DAYS")
    parser.add_argument("--expect-date", metavar="YYYY-MM-DD")
    parser.add_argument("--mixed-script", action="store_true")
    parser.add_argument("--no-secrets", action="store_true", help="skip the secret scan")
    parser.add_argument("--warnings", action="store_true", help="list files with an empty sources list")
    args = parser.parse_args()

    root = str(ac.find_root(args.root))
    cfg = ac.load_config(root)
    mixed = args.mixed_script or cfg["mixed_script_check"]
    allow = set(cfg["mixed_script_allow"])
    errors, warnings, stale, count = [], [], [], 0

    for path in walk(root, {".md"}):
        count += 1
        rel = os.path.relpath(path, root)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        match = ac.FRONTMATTER.match(text)
        if not match:
            errors.append(f"{rel}: no frontmatter at line 1")
            continue
        try:
            fm = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{rel}: YAML error {e}")
            continue
        check_frontmatter(rel, fm, match.group(1), cfg, args, errors, warnings, stale)
        check_links(path, rel, text, errors)
        if mixed:
            for n, line in enumerate(text.splitlines(), 1):
                for word in MIXED_SCRIPT.findall(line):
                    if word not in allow:
                        errors.append(f"{rel}:{n}: mixed Latin/Cyrillic word '{word}'")

    if not args.no_secrets:
        for path in walk(root, TEXT_EXTENSIONS):
            if os.path.getsize(path) > 2_000_000:
                continue
            with open(path, encoding="utf-8", errors="ignore") as f:
                for n, line in enumerate(f, 1):
                    if SECRET_PATTERNS.search(line):
                        errors.append(f"{os.path.relpath(path, root)}:{n}: possible secret or token")

    print(f"checked {count} md files in {root}")
    if warnings:
        if args.warnings:
            print(f"\n{len(warnings)} warnings:")
            print("\n".join(warnings))
        else:
            print(f"\n{len(warnings)} files have an empty sources list (show them with --warnings)")
    if stale:
        print(f"\n{len(stale)} files not updated for {args.stale}+ days:")
        print("\n".join(stale))
    if errors:
        print(f"\n{len(errors)} errors:")
        print("\n".join(errors))
        sys.exit(1)
    print("OK: no errors")


if __name__ == "__main__":
    main()
