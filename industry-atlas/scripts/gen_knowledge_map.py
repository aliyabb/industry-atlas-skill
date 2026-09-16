#!/usr/bin/env python3
"""Generate knowledge-map node cards, Knowledge-Map.md and Opportunity-Map.md.

    python3 tools/gen_knowledge_map.py nodes.yaml

nodes.yaml is a list of nodes. Branches have no `parent`; sub-nodes point to
their branch key. Keys become file names (`Payments`, `Payments--Wallets`).

    - key: Payments
      title: "Payments"
      short: "moving money between payers and payees"
      tags: [payments]              # first tag = segment key
      regions: [global]
      overview: "2-4 sentences with dated numbers."
      companies: [Stripe, Adyen]    # 02-Companies file names; unknown names stay plain text
      tech: ["Card networks", "Real-time rails"]
      trends: [["Real-time payments", "07-Trends/Real-Time-Payments.md"]]
      trends_extra: ["free-text trend without a card"]
      opportunities: [["Label", "12-Opportunities/File.md"]]
      opportunities_extra: []
      regulation: [["Label", "06-Regulations/File.md"]]
      regulation_extra: []
      metrics: ["TPV", "Take rate"]
      scores: {competition: 5, growth: 3, content_gap: 2, supply_gap: 2}
      label: "Payments PSPs"        # short quadrant label (sub-nodes)
      related: [Open-Banking]
      more: [["Payments overview", "01-Segments/Payments/Payments-Overview.md"]]
      sources: []                   # optional; otherwise taken from `more` and `trends` files

Paths are relative to the atlas root. Links to files that do not exist yet are
rendered as plain text and reported, so the map never contains broken links.
"""
import argparse
import pathlib
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import atlas_common as ac  # noqa: E402
import build_opportunity_map  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("data")
    parser.add_argument("--root")
    args = parser.parse_args()

    root = ac.find_root(args.root)
    cfg = ac.load_config(root)
    L, LK = ac.labels(cfg, "node"), ac.labels(cfg, "knowledge_map")
    tag, marker, updated = cfg["industry_tag"], cfg["verification_marker"], ac.as_of(cfg)
    nodes = yaml.safe_load(pathlib.Path(args.data).read_text(encoding="utf-8")) or []
    by_key = {n["key"]: n for n in nodes}
    missing = []

    for n in nodes:
        if n.get("parent") and n["parent"] not in by_key:
            sys.exit(f"{n['key']}: unknown parent {n['parent']}")

    km = root / "11-Knowledge-Map"
    (km / "Nodes").mkdir(parents=True, exist_ok=True)

    def path_link(label, rel):
        if (root / rel).exists():
            return f"[{label}](../../{rel})"
        missing.append(f"{rel} (from {current['key']})")
        return label

    def node_link(key):
        if key not in by_key:
            missing.append(f"node {key} (from {current['key']})")
            return key
        return f"[{by_key[key]['title']}]({key}.md)"

    def company_link(key):
        card = root / "02-Companies" / f"{key}.md"
        if card.exists():
            return f"[{ac.read_frontmatter(card).get('title', key)}](../../02-Companies/{key}.md)"
        return key

    def bullets(items):
        return "\n".join(f"- {x}" for x in items) if items else "- —"

    def children(key):
        return [n for n in nodes if n.get("parent") == key]

    for current in nodes:
        n = current
        parent = by_key.get(n.get("parent"))
        s = n["scores"]
        attr = s["growth"] + s["content_gap"] + s["supply_gap"] - s["competition"]
        sources = list(n.get("sources") or [])
        for _, rel in list(n.get("more", [])) + list(n.get("trends", [])):
            for url in ac.http_sources(root / rel):
                if url not in sources:
                    sources.append(url)
        sources = sources[:4]
        tags = [tag, "knowledge-map", *n.get("tags", [])]
        fm = ["---", f"title: {ac.q(n['title'])}", "type: segment", f"tags: {ac.yaml_list(tags)}",
              f"region: {ac.yaml_list(n.get('regions', cfg['regions']))}", f"updated: {updated}",
              "sources:" if sources else "sources: []", *[f"  - {u}" for u in sources],
              f"parent: {ac.q(parent['title'] if parent else '')}",
              f"competition: {s['competition']}", f"growth: {s['growth']}",
              f"content_gap: {s['content_gap']}", f"supply_gap: {s['supply_gap']}"]
        if n.get("label"):
            fm.append(f"label: {ac.q(n['label'])}")
        fm += ["---", ""]
        crumbs = cfg["industry"] + (f" → {node_link(parent['key'])}" if parent else "") + f" → **{n['title']}**"
        linked = lambda key: [path_link(label, rel) for label, rel in n.get(key, [])] + list(n.get(f"{key}_extra", []))  # noqa: E731
        kids = ", ".join(node_link(k["key"]) for k in children(n["key"])) or "—"
        related = ", ".join(node_link(k) for k in n.get("related", [])) or "—"
        more = ", ".join(path_link(label, rel) for label, rel in n.get("more", [])) or "—"
        body = f"""# {n['title']}

> {crumbs}

## {L['overview']}

{n['overview']}

## {L['companies']}

{', '.join(company_link(c) for c in n.get('companies', [])) or '—'}

## {L['tech']}

{bullets(n.get('tech', []))}

## {L['trends']}

{bullets(linked('trends'))}

## {L['opportunities']}

{bullets(linked('opportunities'))}

## {L['regulation']}

{bullets(linked('regulation'))}

## {L['metrics']}

{bullets(n.get('metrics', []))}

## {L['score']}

| {' | '.join(L['score_columns'])} |
|---|---|---|---|---|
| {s['competition']} | {s['growth']} | {s['content_gap']} | {s['supply_gap']} | **{attr}** |

{L['score_note'].format(marker=marker)}

## {L['links']}

- **{L['parent']}:** {node_link(parent['key']) if parent else '—'}
- **{L['children']}:** {kids}
- **{L['related']}:** {related}
- **{L['more']}:** {more}
"""
        (km / "Nodes" / f"{n['key']}.md").write_text("\n".join(fm) + "\n" + body, encoding="utf-8")

    roots = [n for n in nodes if not n.get("parent")]
    lines = ["---", f"title: {ac.q(LK['title'])}", "type: map",
             f"tags: {ac.yaml_list([tag, 'knowledge-map', 'taxonomy'])}",
             f"region: {ac.yaml_list(cfg['regions'])}", f"updated: {updated}"]
    map_sources = []
    for n in roots:
        for _, rel in n.get("more", [])[:1]:
            map_sources += [u for u in ac.http_sources(root / rel, 1) if u not in map_sources]
    lines += (["sources:"] + [f"  - {u}" for u in map_sources[:4]]) if map_sources else ["sources: []"]
    lines += ["---", "", f"# {LK['heading']}", "",
              LK["intro"].format(n=len(nodes), roots=len(roots), subs=len(nodes) - len(roots)), "",
              f"## {LK['top']}", "", "```mermaid", "flowchart LR", f'    ROOT(("{cfg["industry"]}"))']
    for i, r in enumerate(roots):
        lines.append(f'    ROOT --> N{i}["{r["title"]}"]')
    lines += ["```", "", f"## {LK['tree']}", ""]
    for r in roots:
        lines.append(f"- **[{r['title']}](Nodes/{r['key']}.md)** — {r.get('short', '')}")
        for child in children(r["key"]):
            lines.append(f"  - [{child['title']}](Nodes/{child['key']}.md) — {child.get('short', '')}")
    lines += ["", f"## {LK['how_to_use']}", "", *[f"{i}. {t}" for i, t in enumerate(LK["how_to_use_items"], 1)], ""]
    (km / "Knowledge-Map.md").write_text("\n".join(lines), encoding="utf-8")

    count = build_opportunity_map.build(root, cfg)
    print(f"{len(nodes)} nodes written; opportunity map ranks {count} sub-nodes")
    if missing:
        print("\nnot linked (target missing — create it or fix the path, then rerun):")
        print("\n".join(f"  - {m}" for m in sorted(set(missing))))


if __name__ == "__main__":
    main()
