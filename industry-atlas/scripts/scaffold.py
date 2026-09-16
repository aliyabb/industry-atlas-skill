#!/usr/bin/env python3
"""Create the skeleton of an Industry Atlas repository.

    python3 scaffold.py init --config atlas.config.yaml --root ~/code/ai-agents-atlas
    python3 scaffold.py monitoring --root ~/code/ai-agents-atlas      # Phase 6

`init` creates the numbered folders with README stubs, segment sub-folders,
card templates (99-Templates), the tools/ scripts, .gitignore, the config and
a root README with roadmap and changelog. Existing files are never
overwritten unless --force is given, so it is safe to rerun after adding
segments to the config.

`monitoring` installs the weekly monitoring templates into 14-Monitoring.
Run it in Phase 6, once the sections they link to exist.

Stub text is English; rewrite stubs in the atlas content language during
Phase 1.
"""
import argparse
import pathlib
import shutil
import sys

import yaml

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import atlas_common as ac  # noqa: E402

SKILL = HERE.parent
ASSETS = SKILL / "assets"

# (folder, short name, what it holds, phase)
FOLDERS = [
    ("00-Overview", "Overview", "Taxonomy, conventions, market overview, regions, market sizes, funding and exits, glossary", "1, 2"),
    ("01-Segments", "Segments", "One folder per segment: definition, size, players, business models, unit economics, regulation", "2"),
    ("02-Companies", "Companies", "100–200 company cards and a master table by region", "2"),
    ("03-Products", "Products", "Product categories: jobs to be done, features, public pricing, reviews", "2"),
    ("04-Customer-Pain-Points", "Customer pain points", "Pain-points matrix, complaints data, unmet needs, common questions", "2"),
    ("05-Keywords-SEO-ASO", "Keywords", "Search demand: commercial, informational, comparison, local, app-store and career queries", "2"),
    ("06-Regulations", "Regulation and policy", "Regulatory calendar, regions, cross-cutting themes, licences, regulators", "2"),
    ("07-Trends", "Trends", "Trend radar and trend cards", "2"),
    ("08-Business-Models", "Business models", "Revenue models, unit-economics formulas, valuation basics", "2"),
    ("09-Competitor-Analysis", "Competitor teardowns", "Reverse-engineering of 10–20 leaders: site, pricing, SEO, content, funnels, patterns", "3"),
    ("10-Content-Ecosystem", "Content ecosystem", "100+ newsletters, podcasts, channels, creators, media and communities, classification, engagement patterns", "4"),
    ("11-Knowledge-Map", "Knowledge map", "Hierarchical map with node cards, cross-industry links, opportunity map", "5"),
    ("12-Opportunities", "Opportunities", "Scored opportunities, content gaps, portfolio or project ideas", "2, 5"),
    (None, "Action guide", "Personal action guide for the user's purpose, with a 30/60/90-day plan", "7"),
    ("14-Monitoring", "Monitoring", "Follow list, RSS, weekly competitor, content and industry reports, update instructions", "6"),
    ("99-Templates", "Templates", "Card templates for every document type", "1"),
]


def write(path, text, force, created):
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    created.append(path)


def frontmatter(cfg, title, type_, tags, region=None, sources=None):
    lines = ["---", f"title: {ac.q(title)}", f"type: {type_}",
             f"tags: {ac.yaml_list([cfg['industry_tag'], *tags])}",
             f"region: {ac.yaml_list(region or cfg['regions'])}",
             f"updated: {ac.as_of(cfg)}"]
    if sources:
        lines += ["sources:"] + [f"  - {s}" for s in sources]
    else:
        lines.append("sources: []")
    return "\n".join(lines + ["---", ""]) + "\n"


def folder_list(cfg):
    return [(name or ac.action_guide_folder(cfg), short, desc, phase) for name, short, desc, phase in FOLDERS]


def fill_tokens(text, cfg):
    return (text.replace("__INDUSTRY_TAG__", cfg["industry_tag"])
                .replace("__INDUSTRY__", cfg["industry"])
                .replace("__REGIONS__", ac.yaml_list(cfg["regions"]))
                .replace("__AS_OF__", ac.as_of(cfg))
                .replace("__ACTION_GUIDE__", ac.action_guide_folder(cfg)))


def root_readme(cfg):
    folders = folder_list(cfg)
    rows = "\n".join(f"| {name[:2]} | [{name}]({name}/README.md) | {desc} | {phase} | ⚪ Scaffold |"
                     for name, _, desc, phase in folders)
    title = cfg.get("atlas_title") or f"{cfg['industry']} Atlas"
    return frontmatter(cfg, title, "index", ["index", "knowledge-base"]) + f"""# 🧭 {title}

> A structured, continuously updated knowledge base about the {cfg['industry']} industry: segments, companies, products, regulation, trends, content ecosystem, knowledge map, monitoring and a personal action plan.

**Owner:** {cfg.get('owner', '—')} · **Status:** ⚪ Phase 1 in progress · **Last update:** {ac.as_of(cfg)}

## 🗂️ Repository structure

| № | Folder | What is inside | Phase | Status |
|---|---|---|---|---|
{rows}
| — | [tools](tools/) | Validation, generators, weekly report, feed checker | 1 | 🟢 Installed |

## 🛣️ Roadmap

- [ ] **Phase 1.** Structure, taxonomy, conventions, templates
- [ ] **Phase 2.** Core databases (2A market and segments · 2B companies · 2C products, pain points, keywords · 2D regulation, trends, business models, opportunities)
- [ ] **Phase 3.** Competitor teardowns
- [ ] **Phase 4.** Content ecosystem
- [ ] **Phase 5.** Knowledge map and opportunity map
- [ ] **Phase 6.** Monitoring system
- [ ] **Phase 7.** Action guide and 30/60/90-day plan

## 📝 Changelog

| Date | Phase | Change |
|---|---|---|
| {ac.as_of(cfg)} | 1 | Repository scaffold created |
"""


def cmd_init(args):
    root = pathlib.Path(args.root).resolve()
    if args.config:
        cfg = yaml.safe_load(pathlib.Path(args.config).read_text(encoding="utf-8")) or {}
        root.mkdir(parents=True, exist_ok=True)
        target = root / ac.CONFIG_NAME
        if not target.exists() or args.force:
            shutil.copyfile(args.config, target) if pathlib.Path(args.config).resolve() != target else None
    cfg = ac.load_config(root)
    created = []

    for name, short, desc, phase in folder_list(cfg):
        write(root / name / "README.md",
              frontmatter(cfg, f"{name} — {short}", "index", ["index"]) +
              f"# {name} — {short}\n\n> {desc}\n\n**Status:** ⚪ Scaffold — filled in phase {phase}.\n",
              args.force, created)

    for seg in cfg["segments"]:
        write(root / "01-Segments" / seg["folder"] / "README.md",
              frontmatter(cfg, f"{seg['name']}", "index", ["index", seg["key"]]) +
              f"# {seg['name']}\n\n> Segment folder. The overview card (`{seg.get('overview', 'README.md')}`) is written in Phase 2A.\n",
              args.force, created)

    write(root / "14-Monitoring" / "Reports" / "README.md",
          frontmatter(cfg, "Weekly reports archive", "index", ["index", "monitoring", "report"]) +
          "# 🗄️ Weekly reports archive\n\n> One file per ISO week: `YYYY-Www.md`. Create a draft with `python3 tools/new_weekly_report.py`.\n",
          args.force, created)

    for tpl in sorted((ASSETS / "templates" / "cards").glob("*.md")):
        write(root / ac.TEMPLATES_DIR / tpl.name, fill_tokens(tpl.read_text(encoding="utf-8"), cfg), args.force, created)

    tools = root / "tools"
    tools.mkdir(exist_ok=True)
    for script in sorted(HERE.glob("*.py")):
        if script.name != "scaffold.py":
            dest = tools / script.name
            if not dest.exists() or args.force:
                shutil.copyfile(script, dest)
                created.append(dest)

    write(root / ".gitignore", (ASSETS / "gitignore.template").read_text(encoding="utf-8"), args.force, created)
    write(root / "README.md", root_readme(cfg), args.force, created)

    print(f"scaffolded {root} ({len(created)} files written)")
    for path in created:
        print("  +", path.relative_to(root))
    print("\nnext: write 00-Overview/Conventions.md and Industry-Taxonomy.md (Phase 1), then run tools/validate_kb.py")


def cmd_monitoring(args):
    root = ac.find_root(args.root)
    cfg = ac.load_config(root)
    created = []
    for tpl in sorted((ASSETS / "templates" / "monitoring").glob("*.md")):
        write(root / "14-Monitoring" / tpl.name, fill_tokens(tpl.read_text(encoding="utf-8"), cfg), args.force, created)
    print(f"installed {len(created)} monitoring templates into {root / '14-Monitoring'}")
    for path in created:
        print("  +", path.relative_to(root))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_init = sub.add_parser("init")
    p_init.add_argument("--config", help="path to atlas.config.yaml (copied into the root)")
    p_init.add_argument("--root", required=True)
    p_init.add_argument("--force", action="store_true")
    p_init.set_defaults(func=cmd_init)
    p_mon = sub.add_parser("monitoring")
    p_mon.add_argument("--root")
    p_mon.add_argument("--force", action="store_true")
    p_mon.set_defaults(func=cmd_monitoring)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
