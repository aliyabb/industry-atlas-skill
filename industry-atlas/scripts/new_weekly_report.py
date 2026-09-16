#!/usr/bin/env python3
"""Create a weekly report draft from 14-Monitoring/Weekly-Industry-Report.md.

    python3 tools/new_weekly_report.py              # current ISO week
    python3 tools/new_weekly_report.py 2026-09-07   # ISO week containing this date

On a Monday, a report about the week that just ended is usually what people
want: pass any date from last week.

Everything below the <!-- REPORT-START --> marker in the template is copied,
{{WEEK}}, {{DATE_FROM}} and {{DATE_TO}} are filled in, and relative links are
rewritten for the Reports/ subfolder.
"""
import argparse
import datetime as dt
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import atlas_common as ac  # noqa: E402

MARKER = "<!-- REPORT-START -->"
RELATIVE_LINK = re.compile(r"\]\((?!https?://|mailto:|#|\{\{)([^)\s]+)\)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("date", nargs="?", help="any date inside the target ISO week (YYYY-MM-DD)")
    parser.add_argument("--root")
    args = parser.parse_args()

    root = ac.find_root(args.root)
    cfg = ac.load_config(root)
    L = ac.labels(cfg, "report")
    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    year, week, _ = day.isocalendar()
    monday = day - dt.timedelta(days=day.weekday())
    sunday = monday + dt.timedelta(days=6)
    week_id = f"{year}-W{week:02d}"

    template = root / "14-Monitoring" / "Weekly-Industry-Report.md"
    reports = root / "14-Monitoring" / "Reports"
    out = reports / f"{week_id}.md"
    if not template.exists():
        sys.exit(f"missing {template.relative_to(root)} — run scaffold.py monitoring first")
    if out.exists():
        sys.exit(f"{out.relative_to(root)} already exists")

    text = template.read_text(encoding="utf-8")
    if MARKER not in text:
        sys.exit(f"{template.relative_to(root)} has no {MARKER} marker")
    body = text.split(MARKER, 1)[1].lstrip("\n")
    body = (body.replace("{{WEEK}}", week_id)
                .replace("{{DATE_FROM}}", monday.strftime("%d.%m"))
                .replace("{{DATE_TO}}", sunday.strftime("%d.%m.%Y")))
    body = RELATIVE_LINK.sub(lambda m: f"](../{m.group(1)})", body)

    frontmatter = "\n".join([
        "---",
        f"title: {ac.q(L['title'].format(week=week_id))}",
        "type: report",
        f"tags: {ac.yaml_list([cfg['industry_tag'], 'monitoring', 'weekly', 'report'])}",
        f"region: {ac.yaml_list(cfg['regions'])}",
        f"updated: {dt.date.today().isoformat()}",
        "sources:",
        f"  - https://example.com/  # {L['source_hint']}",
        "---",
        "",
    ])
    reports.mkdir(parents=True, exist_ok=True)
    out.write_text(frontmatter + "\n" + body, encoding="utf-8")
    print(f"created {out.relative_to(root)} ({monday}–{sunday})")
    print("next: fill it with verified news, add a row to 14-Monitoring/Reports/README.md, validate, commit")


if __name__ == "__main__":
    main()
