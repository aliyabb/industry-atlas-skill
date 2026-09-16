# Repository structure

File plan per folder, with targets for the `standard` depth. Adjust names to the industry (see `industry-adaptation.md`), but keep the numbering: phases, scripts and cross-links rely on it.

```text
<industry>-atlas/
├── README.md                 # purpose, reading routes, structure, roadmap, changelog
├── atlas.config.yaml
├── .gitignore
├── 00-Overview/
├── 01-Segments/<Segment>/
├── 02-Companies/
├── 03-Products/
├── 04-Customer-Pain-Points/
├── 05-Keywords-SEO-ASO/
├── 06-Regulations/
├── 07-Trends/
├── 08-Business-Models/
├── 09-Competitor-Analysis/
├── 10-Content-Ecosystem/
├── 11-Knowledge-Map/Nodes/
├── 12-Opportunities/
├── 13-<Action-Guide>/        # 13-How-to-Enter, 13-Startup-Playbook, 13-Investor-Playbook or 13-Action-Plan
├── 14-Monitoring/Reports/
├── 99-Templates/
└── tools/
```

## Folder plans

| Folder | Files (standard depth) | Phase |
|---|---|---|
| `00-Overview` | `README`, `Conventions`, `Industry-Taxonomy` (1); `Market-Overview`, `Regional-Breakdown`, `Subsector-Market-Sizes`, `Funding-VC-Exits`, `Glossary` (2A) | 1, 2A |
| `01-Segments` | `README` + one folder per segment with `README` and `<Segment>-Overview.md`; 3–5 deep-dive explainers where the economics are non-obvious (value chain, unit economics) | 2A |
| `02-Companies` | 100–200 cards + master `README` grouped by region, with stats | 2B |
| `03-Products` | `README` + 15–25 product-category files | 2C |
| `04-Customer-Pain-Points` | `README`, `Pain-Points-Matrix`, 4–6 thematic files by customer type, `Common-Questions` | 2C |
| `05-Keywords-SEO-ASO` | `README`, `Keyword-Strategy-Overview`, one file per segment group, `ASO-Keywords` if apps matter, audience keywords (career, buyer or investor queries) | 2C |
| `06-Regulations` | `README` with a 2–3-year calendar, one file per region, 5–9 cross-cutting themes, `Licensing-Matrix` (or `Standards-and-Certifications`), `Regulators-Directory` | 2D |
| `07-Trends` | `README` with a radar table and a Mermaid dependency graph + 12–20 trend cards | 2D |
| `08-Business-Models` | `README`, `Revenue-Models-Catalog`, `Unit-Economics-Formulas`, 3–5 model deep dives, `Valuation-Basics`, `Business-Model-Canvas-Examples` | 2D |
| `09-Competitor-Analysis` | `README` (method + table) + 10–20 `<Company>-Teardown.md`, `Pricing-Pages-Comparison`, `Patterns-Summary` | 3 |
| `10-Content-Ecosystem` | `README`, one file per platform (newsletters, podcasts, YouTube, X, LinkedIn, TikTok or Instagram, blogs and media, communities and events), `Content-Classification`, `Engagement-Patterns` | 4 |
| `11-Knowledge-Map` | `README`, `Knowledge-Map`, `Nodes/*.md`, `Opportunity-Map`, `Cross-Industry-Connections` | 5 |
| `12-Opportunities` | `README` (scoring framework), `Opportunities-Overview`, 6–10 opportunity cards (2D); `Content-Gaps` (5); project or portfolio ideas (7) | 2D, 5, 7 |
| `13-<Action-Guide>` | See `phase-7-action-guide.md` | 7 |
| `14-Monitoring` | `README`, `Follow-List-Top-50`, `RSS-Setup`, `feeds.opml`, `Weekly-Competitor-Monitoring`, `Weekly-Content-Monitoring`, `Weekly-Industry-Report`, `Auto-Update-Instructions`, `Reports/README`, `Reports/<baseline week>.md` | 6 |
| `99-Templates` | `README` + card templates | 1 |

## Folder README pattern

Every folder `README.md` (type `index`) has:

1. H1 with emoji and folder name, one-paragraph purpose.
2. A **files table**: file (link, or `code` if not written yet), content, status (🟢 phase / ⚪ planned).
3. Method or scoring notes if the folder uses a framework.
4. **Related sections** links.

Update the table in the same commit that adds files.

## Root README pattern

1. Title and one-sentence description.
2. **Owner · Status · Last update** line; the status names completed phases and key counts.
3. **Why this atlas** (3–4 bullets tied to the user's purpose).
4. **How to use**: reading routes table (goal → path → time).
5. **Repository structure**: table `№ | Folder | What is inside | Phase | Status` + tree.
6. **Roadmap**: phase checkboxes (Phase 2 with 2A–2D sub-items).
7. **Changelog**: `Date | Phase | Change`, one row per phase or big update.

Keep status, table row, roadmap and changelog in sync after every phase.
