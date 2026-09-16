#!/usr/bin/env python3
"""Rebuild 11-Knowledge-Map/Opportunity-Map.md from node card frontmatter.

Scores live in each node card (competition, growth, content_gap, supply_gap,
1-5) together with `parent` (branch title) and `label` (short quadrant label).
Edit a card, then run:

    python3 tools/build_opportunity_map.py
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import atlas_common as ac  # noqa: E402


def load_nodes(km):
    nodes = []
    for path in sorted((km / "Nodes").glob("*.md")):
        fm = ac.read_frontmatter(path)
        if "competition" not in fm:
            continue
        nodes.append({
            "key": path.stem, "title": fm["title"], "parent": fm.get("parent") or "",
            "label": fm.get("label"), "sources": fm.get("sources") or [],
            "comp": int(fm["competition"]), "growth": int(fm["growth"]),
            "content": int(fm["content_gap"]), "supply": int(fm["supply_gap"]),
        })
    return nodes


def attractiveness(n):
    return n["growth"] + n["content"] + n["supply"] - n["comp"]


def quadrant_label(text):
    """Mermaid quadrant labels break on punctuation; keep letters, digits and spaces."""
    return re.sub(r"\s+", " ", re.sub(r"[^\w ]", " ", text)).strip()[:40]


def build(root, cfg):
    km = pathlib.Path(root) / "11-Knowledge-Map"
    L = ac.labels(cfg, "opportunity_map")
    marker = cfg["verification_marker"]
    nodes = load_nodes(km)
    subs = sorted((n for n in nodes if n["parent"]), key=lambda n: (-attractiveness(n), n["title"]))

    def link(n):
        return f"[{n['title']}](Nodes/{n['key']}.md)"

    sources = []
    for n in subs:
        for url in n["sources"][:1]:
            if url not in sources:
                sources.append(url)
    lines = ["---", f"title: {ac.q(L['title'])}", "type: map",
             f"tags: {ac.yaml_list([cfg['industry_tag'], 'knowledge-map', 'opportunities'])}",
             f"region: {ac.yaml_list(cfg['regions'])}", f"updated: {ac.as_of(cfg)}",
             "sources:" if sources else "sources: []", *[f"  - {u}" for u in sources[:4]], "---", "",
             f"# {L['heading']}", "", L["intro"].format(marker=marker), "", L["formula"], "",
             f"## {L['ranking']}", "", "| " + " | ".join(L["columns"]) + " |", "|" + "---|" * len(L["columns"])]
    for i, n in enumerate(subs, 1):
        lines.append(f"| {i} | {link(n)} | {n['parent']} | {n['comp']} | {n['growth']} | "
                     f"{n['content']} | {n['supply']} | **{attractiveness(n)}** |")
    crowded = [n for n in subs if n["comp"] >= 5]
    fastest = [n for n in subs if n["growth"] >= 5]
    gaps = [n for n in subs if n["content"] >= 4 and n["supply"] >= 4]
    lines += ["", f"## {L['conclusions']}", "",
              f"### {L['crowded']}", "", ", ".join(map(link, crowded)) or "—", "", L["crowded_note"], "",
              f"### {L['fastest']}", "", ", ".join(map(link, fastest)) or "—", "",
              f"### {L['gaps']}", "", ", ".join(map(link, gaps)) or "—", "",
              f"## {L['quadrants']}", "", "```mermaid", "quadrantChart",
              "    title Competition vs Growth",
              "    x-axis Low competition --> High competition",
              "    y-axis Low growth --> High growth",
              "    quadrant-1 Crowded and growing",
              "    quadrant-2 Open and growing",
              "    quadrant-3 Niche or early",
              "    quadrant-4 Mature battlegrounds"]
    for n in subs:
        label = quadrant_label(n["label"] or n["title"].split(" (")[0])
        x = (n["comp"] - 1) / 4 * 0.9 + 0.05
        y = (n["growth"] - 1) / 4 * 0.9 + 0.05
        lines.append(f"    {label}: [{x:.2f}, {y:.2f}]")
    lines += ["```", "", f"## {L['usage']}", "", *[f"- {item}" for item in L["usage_items"]], ""]
    (km / "Opportunity-Map.md").write_text("\n".join(lines), encoding="utf-8")
    return len(subs)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root")
    args = parser.parse_args()
    root = ac.find_root(args.root)
    count = build(root, ac.load_config(root))
    print(f"Opportunity-Map.md rebuilt from {count} sub-nodes")


if __name__ == "__main__":
    main()
