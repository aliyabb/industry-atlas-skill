"""Shared helpers for the Industry Atlas scripts: config, labels, frontmatter.

Every script in this folder imports this module, so keep the files together
(scaffold.py copies the whole set into the atlas repo's tools/ folder).
"""
import copy
import datetime as dt
import pathlib
import re

import yaml

CONFIG_NAME = "atlas.config.yaml"
BASE_TYPES = {"company", "segment", "product", "trend", "regulation", "keyword",
              "content-source", "opportunity", "person",
              "index", "guide", "template", "map", "report"}
DEFAULT_REGION_VALUES = ["global", "us", "eu", "uk", "asia", "latam", "mena", "africa"]
TEMPLATES_DIR = "99-Templates"
ACTION_GUIDE_FOLDERS = {
    "career": "13-How-to-Enter",
    "founder": "13-Startup-Playbook",
    "investor": "13-Investor-Playbook",
}

# English defaults for every generated heading and sentence. Override any key
# in atlas.config.yaml under `labels:` to produce the atlas in another language.
DEFAULT_LABELS = {
    "company": {
        "snapshot": "📇 Snapshot",
        "field": "Field",
        "value": "Value",
        "country": "Country (HQ)",
        "founded": "Founded",
        "segment": "Segment / sub-segment",
        "customers": "Customer type",
        "status": "Status",
        "website": "Website",
        "social": "Social",
        "social_search": "(search)",
        "why": "🧭 Why it matters",
        "people": "👥 Founders and key people",
        "funding": "💰 Funding and valuation",
        "raised": "Raised",
        "valuation": "Valuation / market cap",
        "investors": "Key investors / owners",
        "products": "🧩 Products and services",
        "target": "🎯 Target customers",
        "model": "💵 Business model and pricing",
        "model_label": "Model",
        "pricing_label": "Pricing",
        "pricing_default": "see the company website",
        "metrics": "📊 Key metrics",
        "competitors": "⚔️ Competitors",
        "competitor_col": "Company",
        "events": "🗓️ Recent events",
        "angle": "🎯 Career angle",
        "angle_default": "Check the company careers page; typical roles: product, operations, growth, risk, sales.",
        "links": "🔗 Links",
        "links_segment": "Segment",
        "links_index": "Master table",
        "checks": "⚠️ What to verify",
        "checks_default": "Freshness of valuation, metrics and leadership → company website, filings, Crunchbase",
        "na": "n/a",
        "status_values": {"private": "Private", "public": "Public",
                          "acquired": "Acquired", "defunct": "Defunct"},
    },
    "company_index": {
        "title": "02-Companies — company database",
        "heading": "🏢 02-Companies — company database",
        "intro": ("**{n} companies** across {segments} segments. Every card follows the "
                  "[template](../99-Templates/Company-Card-Template.md). Data as of {date}; private "
                  "valuations and metrics go stale quickly, so every number carries a period and "
                  "doubtful values are marked {marker}."),
        "how_to_use": "How to use",
        "how_to_use_items": [
            "**Interview or meeting prep:** company card → angle block → segment card → competitors.",
            "**Target list:** filter the tables below by region and segment; companies with recent funding rounds usually hire.",
            "**Obsidian Dataview:**",
        ],
        "stats": "Database statistics",
        "segment_col": "Segment",
        "count_col": "Companies",
        "status_col": "Status",
        "columns": ["Company", "Country", "Founded", "Segment", "Customers", "Status",
                    "Valuation / market cap", "Key fact"],
        "methodology": "⚠️ Methodology and limits",
        "methodology_items": [
            "**Sources:** filings of public companies (A), press releases and business media (B), valuation aggregators (C). The primary source is listed in each card's frontmatter.",
            "**Social links** point to LinkedIn and X search pages so that unverified profile URLs are never published.",
        ],
        "related": "Related sections",
    },
    "node": {
        "overview": "🧭 Overview",
        "companies": "🏢 Key companies",
        "tech": "🛠️ Tools and technologies",
        "trends": "📈 Trends",
        "opportunities": "💡 Opportunities",
        "regulation": "⚖️ Regulation",
        "metrics": "📊 Key metrics",
        "score": "🗺️ Node score (1–5)",
        "score_columns": ["Competition", "Growth", "Content gap", "Supply gap", "Attractiveness*"],
        "score_note": ("\\* Attractiveness = growth + content gap + supply gap − competition "
                       "(expert estimate {marker}). Summary: [Opportunity-Map](../Opportunity-Map.md)."),
        "links": "🔗 Links",
        "parent": "Parent",
        "children": "Child nodes",
        "related": "Related nodes",
        "more": "Read more",
    },
    "knowledge_map": {
        "title": "Industry knowledge map",
        "heading": "🧠 Industry knowledge map",
        "intro": ("> A hierarchical tree of **{n} nodes** ({roots} branches and {subs} sub-nodes). "
                  "Every node has a card: overview, companies, technologies, trends, opportunities, "
                  "regulation, metrics and a score."),
        "top": "Top level",
        "tree": "Tree (links to cards)",
        "how_to_use": "How to use",
        "how_to_use_items": [
            "Start from the branch of the segment you care about, then read its sub-nodes.",
            "From each card, follow the links to trends, regulation and opportunities: the map connects every section of the atlas.",
            "To pick a niche, open [Opportunity-Map](Opportunity-Map.md).",
        ],
    },
    "opportunity_map": {
        "title": "Opportunity map: competition, growth, gaps",
        "heading": "🗺️ Opportunity map",
        "intro": ("> Where competition is highest, where growth is fastest, and where content or supply "
                  "is missing. Scores 1–5 are expert estimates {marker}, grounded in funding data, player "
                  "counts, trends and customer pain points from this atlas."),
        "formula": "**Attractiveness** = growth + content gap + supply gap − competition.",
        "ranking": "Sub-node ranking",
        "columns": ["#", "Node", "Branch", "Competition", "Growth", "Content gap", "Supply gap",
                    "Attractiveness"],
        "conclusions": "Conclusions",
        "crowded": "🔴 Highest competition (5/5)",
        "crowded_note": "Scale, licences and distribution win here; a newcomer needs a narrow wedge (niche, region, vertical).",
        "fastest": "🚀 Fastest growth (5/5)",
        "gaps": "🕳️ Biggest gaps (content ≥ 4 and supply ≥ 4)",
        "quadrants": "Competition × growth quadrants",
        "usage": "🎯 How to use",
        "usage_items": [
            "**Personal brand:** high-growth nodes with a content gap are the fastest topics to become visible in.",
            "**Product ideas:** nodes with a supply gap → cards in [12-Opportunities](../12-Opportunities/README.md).",
            "**Updates:** re-score nodes quarterly ([14-Monitoring](../14-Monitoring/README.md)), then rerun `python3 tools/build_opportunity_map.py`.",
        ],
    },
    "report": {
        "title": "Weekly report {week}",
        "source_hint": "replace with this week's primary sources",
    },
}


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def q(text):
    """Double-quoted YAML scalar."""
    return '"' + str(text).replace('"', "'") + '"'


def yaml_list(items):
    return "[" + ", ".join(str(i) for i in items) + "]"


def find_root(explicit=None):
    """Atlas root: --root if given, else the nearest folder with atlas.config.yaml."""
    if explicit:
        return pathlib.Path(explicit).resolve()
    for start in (pathlib.Path.cwd(), pathlib.Path(__file__).resolve().parent):
        for folder in [start, *start.parents]:
            if (folder / CONFIG_NAME).exists():
                return folder
    return pathlib.Path(__file__).resolve().parent.parent


def load_config(root):
    path = pathlib.Path(root) / CONFIG_NAME
    cfg = (yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else None) or {}
    cfg.setdefault("industry", "Industry")
    cfg.setdefault("industry_tag", slugify(cfg["industry"]))
    cfg.setdefault("content_language", "en")
    cfg.setdefault("purpose", "career")
    cfg.setdefault("regions", ["global"])
    cfg.setdefault("region_values", DEFAULT_REGION_VALUES)
    cfg.setdefault("verification_marker", "⚠️")
    cfg.setdefault("segments", [])
    cfg.setdefault("mixed_script_check", False)
    cfg.setdefault("mixed_script_allow", [])
    cfg.setdefault("extra_types", [])
    return cfg


def as_of(cfg):
    return str(cfg.get("as_of") or dt.date.today().isoformat())


def labels(cfg, section):
    merged = copy.deepcopy(DEFAULT_LABELS.get(section, {}))
    merged.update(((cfg.get("labels") or {}).get(section) or {}))
    return merged


def action_guide_folder(cfg):
    return cfg.get("action_guide_folder") or ACTION_GUIDE_FOLDERS.get(cfg.get("purpose"), "13-Action-Plan")


FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def split_frontmatter(text):
    """Return (frontmatter dict or None, raw frontmatter text, body)."""
    match = FRONTMATTER.match(text)
    if not match:
        return None, "", text
    return (yaml.safe_load(match.group(1)) or {}), match.group(1), text[match.end():]


def read_frontmatter(path):
    fm, _, _ = split_frontmatter(pathlib.Path(path).read_text(encoding="utf-8"))
    return fm or {}


def http_sources(path, limit=None):
    """URLs from a file's `sources` list (used to give generated cards real sources)."""
    path = pathlib.Path(path)
    if not path.exists():
        return []
    urls = [s for s in read_frontmatter(path).get("sources") or []
            if isinstance(s, str) and s.startswith("http")]
    return urls[:limit] if limit else urls
