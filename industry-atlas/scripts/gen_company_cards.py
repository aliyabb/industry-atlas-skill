#!/usr/bin/env python3
"""Generate company cards and the 02-Companies master table from YAML data.

Use it for the initial bulk build (100-200 companies). Afterwards the cards
are the source of truth: edit them directly and keep the data files outside
the repository.

    python3 tools/gen_company_cards.py data/companies-us.yaml data/companies-eu.yaml

Each YAML file is a list of records. Required keys: file, name, group,
country, founded, regions, segment, customer_types, status, website, summary.
Optional keys: subsegment, ticker, status_note, why[], people, funding,
valuation, investors, products[], customers, model, pricing, metrics[],
competitors[], events[], angle, sources[], checks[], tags[].
Segments come from `segments:` and groups from `company_groups:` in
atlas.config.yaml; headings from `labels.company` / `labels.company_index`.
"""
import argparse
import collections
import pathlib
import sys

import yaml

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import atlas_common as ac  # noqa: E402

REQUIRED = ["file", "name", "group", "country", "founded", "regions", "segment",
            "customer_types", "status", "website", "summary"]
DEFAULT_GROUPS = [
    {"key": "US", "title": "🇺🇸 United States"}, {"key": "UK", "title": "🇬🇧 United Kingdom"},
    {"key": "EU", "title": "🇪🇺 European Union"}, {"key": "Asia", "title": "🌏 Asia-Pacific"},
    {"key": "LATAM", "title": "🌎 Latin America"}, {"key": "MENA", "title": "🌍 Middle East and North Africa"},
    {"key": "Africa", "title": "🌍 Africa"}, {"key": "Global", "title": "🌐 Global"},
    {"key": "Failures", "title": "💥 Notable failures (case studies)"},
]


def bullets(items, na):
    return "\n".join(f"- {x}" for x in items) if items else f"- {na}"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("data", nargs="+", help="YAML files with company records")
    parser.add_argument("--root")
    args = parser.parse_args()

    root = ac.find_root(args.root)
    cfg = ac.load_config(root)
    L, LI = ac.labels(cfg, "company"), ac.labels(cfg, "company_index")
    updated, tag, marker = ac.as_of(cfg), cfg["industry_tag"], cfg["verification_marker"]
    segments = {s["key"]: s for s in cfg["segments"]}
    groups = cfg.get("company_groups") or DEFAULT_GROUPS
    group_keys = {g["key"] for g in groups}
    statuses = L["status_values"]

    companies = []
    for data_file in args.data:
        companies += yaml.safe_load(pathlib.Path(data_file).read_text(encoding="utf-8")) or []

    problems, files = [], set()
    for c in companies:
        missing = [k for k in REQUIRED if c.get(k) in (None, "", [])]
        if missing:
            problems.append(f"{c.get('name', '?')}: missing {missing}")
            continue
        if c["file"] in files:
            problems.append(f"duplicate file {c['file']}")
        files.add(c["file"])
        if segments and c["segment"] not in segments:
            problems.append(f"{c['name']}: unknown segment {c['segment']}")
        if set(c["regions"]) - set(cfg["region_values"]):
            problems.append(f"{c['name']}: bad regions {c['regions']}")
        if c["status"] not in statuses:
            problems.append(f"{c['name']}: bad status {c['status']}")
        if c["group"] not in group_keys:
            problems.append(f"{c['name']}: unknown group {c['group']}")
    if problems:
        sys.exit("data errors:\n" + "\n".join(problems))

    out = root / "02-Companies"
    out.mkdir(exist_ok=True)
    by_name = {}
    for c in companies:
        by_name[c["name"]] = c["file"]
        by_name[c["file"]] = c["file"]

    def company_link(name):
        target = by_name.get(name)
        if not target and (out / f"{name}.md").exists():
            target = name
        return f"[{name}]({target}.md)" if target else name

    def segment_link(key):
        seg = segments.get(key)
        if not seg:
            return key
        overview = seg.get("overview", "README.md")
        if (root / "01-Segments" / seg["folder"] / overview).exists():
            return f"[{seg['name']}](../01-Segments/{seg['folder']}/{overview})"
        return seg["name"]

    def segment_name(key):
        return segments.get(key, {}).get("name", key)

    for c in companies:
        tags = []
        for t in [tag, c["segment"], *c.get("tags", []), *c["customer_types"], c["status"]]:
            if t not in tags:
                tags.append(t)
        sources = list(c.get("sources") or [])
        if c["website"] not in sources:
            sources.append(c["website"])
        na = L["na"]
        valuation = c.get("valuation", na)
        fm = ["---", f"title: {ac.q(c['name'])}", "type: company", f"tags: {ac.yaml_list(tags[:8])}",
              f"region: {ac.yaml_list(c['regions'])}", f"updated: {updated}", "sources:",
              *[f"  - {u}" for u in sources],
              f"country: {ac.q(c['country'])}", f"founded: {c['founded']}", f"segment: {ac.q(c['segment'])}",
              f"status: {ac.q(c['status'])}", f"ticker: {ac.q(c.get('ticker', ''))}",
              f"website: {ac.q(c['website'])}", f"last_valuation_usd: {ac.q(valuation)}", "---", ""]
        ticker = f" ({c['ticker']})" if c.get("ticker") else ""
        note = f" — {c['status_note']}" if c.get("status_note") else ""
        search = c["name"].replace(" ", "%20")
        social = (f"[LinkedIn](https://www.linkedin.com/search/results/companies/?keywords={search}) · "
                  f"[X](https://x.com/search?q={search}) {L['social_search']}")
        competitor_rows = "\n".join(f"| {company_link(x)} |" for x in c.get("competitors", [])) or f"| {na} |"
        checks = list(c.get("checks", [])) + [L["checks_default"]]
        body = f"""# {c['name']}

> {c['summary']}

## {L['snapshot']}

| {L['field']} | {L['value']} |
|---|---|
| {L['country']} | {c['country']} |
| {L['founded']} | {c['founded']} |
| {L['segment']} | {segment_link(c['segment'])} / {c.get('subsegment', na)} |
| {L['customers']} | {', '.join(x.upper() for x in c['customer_types'])} |
| {L['status']} | {statuses[c['status']]}{ticker}{note} |
| {L['website']} | {c['website']} |
| {L['social']} | {social} |

## {L['why']}

{bullets(c.get('why', []), na)}

## {L['people']}

{c.get('people', na)}

## {L['funding']}

| {L['field']} | {L['value']} |
|---|---|
| {L['raised']} | {c.get('funding', na)} |
| {L['valuation']} | {valuation} |
| {L['investors']} | {c.get('investors', na)} |

## {L['products']}

{bullets(c.get('products', []), na)}

## {L['target']}

{c.get('customers', na)}

## {L['model']}

- **{L['model_label']}:** {c.get('model', na)}
- **{L['pricing_label']}:** {c.get('pricing', L['pricing_default'])}

## {L['metrics']}

{bullets(c.get('metrics', []), na)}

## {L['competitors']}

| {L['competitor_col']} |
|---|
{competitor_rows}

## {L['events']}

{bullets(c.get('events', []), na)}

## {L['angle']}

{c.get('angle', L['angle_default'])}

## {L['links']}

- {L['links_segment']}: {segment_link(c['segment'])}
- {L['links_index']}: [02-Companies](README.md)

## {L['checks']}

{bullets(checks, na)}
"""
        (out / f"{c['file']}.md").write_text("\n".join(fm) + "\n" + body, encoding="utf-8")

    seg_count = collections.Counter(c["segment"] for c in companies)
    status_count = collections.Counter(c["status"] for c in companies)
    regions = [r for r in cfg["region_values"] if any(r in c["regions"] for c in companies)]
    index_sources = cfg.get("company_index_sources") or ["https://www.crunchbase.com/", "https://dealroom.co/"]
    lines = ["---", f"title: {ac.q(LI['title'])}", "type: index", f"tags: {ac.yaml_list([tag, 'index', 'companies'])}",
             f"region: {ac.yaml_list(regions or cfg['regions'])}", f"updated: {updated}", "sources:",
             *[f"  - {u}" for u in index_sources], "---", "",
             f"# {LI['heading']}", "",
             "> " + LI["intro"].format(n=len(companies), segments=len(seg_count), date=updated, marker=marker), "",
             f"## {LI['how_to_use']}", "", *[f"- {item}" for item in LI["how_to_use_items"]], "",
             "```dataview", "TABLE country, founded, segment, status, last_valuation_usd",
             'FROM "02-Companies"', 'WHERE type = "company"', "SORT segment ASC", "```", "",
             f"## {LI['stats']}", "", f"| {LI['segment_col']} | {LI['count_col']} |", "|---|---|"]
    for key in (segments or seg_count):
        lines.append(f"| {segment_link(key)} | {seg_count.get(key, 0)} |")
    lines += ["", f"| {LI['status_col']} | {LI['count_col']} |", "|---|---|"]
    for key, name in statuses.items():
        lines.append(f"| {name} | {status_count.get(key, 0)} |")
    lines.append("")
    for group in groups:
        rows = sorted((c for c in companies if c["group"] == group["key"]), key=lambda c: c["name"].lower())
        if not rows:
            continue
        lines += [f"## {group['title']} ({len(rows)})", "",
                  "| " + " | ".join(LI["columns"]) + " |", "|" + "---|" * len(LI["columns"])]
        for c in rows:
            fact = (c.get("metrics") or c.get("why") or [L["na"]])[0].replace("|", "/")
            status = statuses[c["status"]] + (f" ({c['ticker']})" if c.get("ticker") else "")
            lines.append(f"| [{c['name']}]({c['file']}.md) | {c['country']} | {c['founded']} | "
                         f"{segment_name(c['segment'])} | {', '.join(x.upper() for x in c['customer_types'])} | "
                         f"{status} | {c.get('valuation', L['na'])} | {fact} |")
        lines.append("")
    lines += [f"## {LI['methodology']}", "", *[f"- {item}" for item in LI["methodology_items"]], "",
              f"## {LI['related']}", "",
              "- [01-Segments](../01-Segments/README.md) · [09-Competitor-Analysis](../09-Competitor-Analysis/README.md)", ""]
    (out / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{len(companies)} companies written;", dict(collections.Counter(c['group'] for c in companies)))


if __name__ == "__main__":
    main()
