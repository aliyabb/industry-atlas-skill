---
name: industry-atlas
description: Build a research-backed, continuously updatable knowledge base about any industry as a Markdown vault in a private GitHub repo (works in Obsidian) - taxonomy, market sizes, segments, 100-200 company cards, products, customer pain points, keywords, regulation, trends, business models, competitor teardowns, content ecosystem, a knowledge map with opportunity scoring, weekly monitoring, and a personal action plan (career entry, startup or investing). Use this skill whenever someone wants to deeply learn, map or research an industry end to end, build an industry atlas, market map, competitive landscape or research vault, prepare to break into a new industry, set up industry monitoring, or produce the weekly report or updates for an atlas built this way - even if they never say knowledge base (for example "map the AI agents market for me and push it to GitHub" or "help me understand the gaming industry before I job hunt").
---

# Industry Atlas

Build a structured, sourced and maintainable knowledge base about one industry: a Git repository of interlinked Markdown files that reads well on GitHub and in Obsidian, grows phase by phase, and stays current through a weekly monitoring routine.

The method is industry-agnostic: the phases, conventions, quality gates and scripts carry the work, and every industry-specific choice is made during intake.

## What gets built

| Folder | Content | Phase |
|---|---|---|
| `00-Overview` | Conventions, taxonomy, market overview, regions, market sizes, funding and exits, glossary | 1–2 |
| `01-Segments` | 8–14 segment cards plus explainers (value chain, unit economics) | 2A |
| `02-Companies` | 100–200 company cards and a master table by region | 2B |
| `03-Products`, `04-Customer-Pain-Points`, `05-Keywords-SEO-ASO` | Product categories with public pricing, scored pain-points matrix, search demand | 2C |
| `06-Regulations`, `07-Trends`, `08-Business-Models`, `12-Opportunities` | Regulatory calendar, trend radar, revenue models and formulas, scored opportunities | 2D |
| `09-Competitor-Analysis` | 10–20 teardowns, pricing comparison, patterns and gaps | 3 |
| `10-Content-Ecosystem` | 100+ sources, content classification, engagement patterns | 4 |
| `11-Knowledge-Map` | Node cards, knowledge map, cross-industry links, opportunity map | 5 |
| `14-Monitoring` | Top-50 follow list, verified RSS + OPML, weekly templates, update instructions, reports | 6 |
| `13-…` action guide | Career entry, startup or investor playbook with a 30/60/90-day plan | 7 |
| `99-Templates`, `tools` | Card templates; validation, generators, report and feed scripts | 1 |

## Principles

These exist because the atlas is used for real decisions (interviews, niche selection, investments). Keep them in mind in every phase.

1. **Evidence over fluency.** Every number carries a period, a source and a confidence level (A filings/regulators, B reputable media and analysts, C estimates). Research with web search and fetch tools instead of memory; treat the environment's current date as "now" and assume your training data is stale for anything recent.
2. **Mark uncertainty instead of guessing.** Use the verification marker (default `⚠️`, localized, for example `⚠️ NEEDS VERIFICATION`) when data is older than 12 months, confidence is C, sources disagree by more than 20%, or the status is moving (bills, lawsuits, deals, private valuations). Say what to check and where.
3. **Never invent identifiers.** No made-up URLs, social handles, follower counts, feed addresses or quotes. Link social profiles through search pages, express audiences as tiers (S/M/L/XL), and list a feed as working only after `check_feeds.py` confirms it.
4. **No broken links.** Links are relative and case-sensitive. A file that does not exist yet is written as `code` with "comes in phase N", never as a link. The validator enforces this.
5. **One schema for every file.** Each `.md` starts with frontmatter: `title`, `type`, `tags` (first tag = industry tag), `region`, `updated`, `sources`. See `references/conventions.md`.
6. **Language split.** Prose and headings use the atlas content language. File names, tags and frontmatter keys stay in English. Company, product and regulator names stay original; in a non-English atlas add the English term in parentheses on first use.
7. **Phases, not one dump.** Each phase ends with validation, a root README update, a commit and a push, then a checkpoint. Big phases are split (2A–2D) so each commit stays reviewable.
8. **Safety.** Never commit secrets or tokens (the validator scans for them). Repos are private by default. Only public professional information about people. Summarize sources in your own words; at most one short quote.

## Workflow

### Step 0 — Intake

Read `references/intake.md`. Collect only what is missing from the conversation: industry and boundaries, purpose (career / founder / investor / consultant / learning), the user's background, focus regions, content language, GitHub owner and repo name, depth, and whether to pause after each phase or run autonomously. Summarize the plan in one message and get a yes before creating the repository, since that publishes to the user's account. Then write `atlas.config.yaml` (example: `assets/atlas.config.example.yaml`).

### Step 1 — Scaffold

```bash
python3 <skill-dir>/scripts/scaffold.py init --config atlas.config.yaml --root <atlas-dir>
cd <atlas-dir>
python3 tools/validate_kb.py
```

This creates the folders, README stubs, card templates, `tools/`, `.gitignore` and the root README. Stubs are English; Phase 1 rewrites them in the content language. Check prerequisites first (`git`, `gh auth status`, Python 3.9+ with PyYAML). If `gh` is not authenticated, ask the user to run `gh auth login` themselves; never handle tokens.

### Step 2 — Run the phases

| Phase | Read first | Produces | Commit |
|---|---|---|---|
| 1 | `references/phase-1-structure.md`, `references/industry-adaptation.md` | Conventions, taxonomy, localized READMEs and templates, repo on GitHub | `structure: phase 1 — …` |
| 2A–2D | `references/phase-2-core-databases.md` | Market, segments, companies, products, pain points, keywords, regulation, trends, business models, opportunities | `add(<section>): phase 2X — …` |
| 3 | `references/phase-3-competitor-teardowns.md` | Teardowns, pricing comparison, patterns | `add(competitors): phase 3 — …` |
| 4 | `references/phase-4-content-ecosystem.md` | Content sources, classification, engagement patterns | `add(content): phase 4 — …` |
| 5 | `references/phase-5-knowledge-map.md` | Node cards, knowledge map, opportunity map, cross-industry links, content gaps | `add(knowledge-map): phase 5 — …` |
| 6 | `references/phase-6-monitoring.md` | Follow list, RSS + OPML, weekly templates, update guide, baseline report | `add(monitoring): phase 6 — …` |
| 7 | `references/phase-7-action-guide.md` | Action guide for the user's purpose, 30/60/90-day plan, project ideas | `add(guide): phase 7 — …` |

Read `references/research-playbook.md` before the first research-heavy phase (2A) and whenever sources conflict or block you.

### The loop inside every phase

1. **Read** the phase reference.
2. **Research** in parallel batches (many searches and fetches in one turn), verifying publication dates.
3. **Write** the files; use the generators for bulk content (companies, knowledge-map nodes).
4. **Validate** with `python3 tools/validate_kb.py` (add `--mixed-script` for Cyrillic content) and fix everything; also reread a sample of generated files, since the validator cannot judge content.
5. **Update the root README**: status line, structure-table row, roadmap checkbox, changelog row.
6. **Commit and push** only the phase's paths, with the message format from `references/conventions.md`.
7. **Checkpoint**: summarize what was built, key findings and anything marked ⚠️. If the user asked for an autonomous run, continue to the next phase; otherwise ask whether to continue. Stop anyway for decisions only the user can make.

### Working at scale

- Treat the repository as memory: in a long session, the root README roadmap and changelog show where the work stands. Reread them before resuming after a context reset.
- Generate large sets from structured data: `gen_company_cards.py` for 100–200 companies, `gen_knowledge_map.py` for the map. Keep the YAML data outside the repo (a scratch folder, or `_data/`, which is git-ignored). After generation, the cards are the source of truth.
- Split data files by region or segment (about 30 records each) so a mistake is cheap to fix.
- Prefer many small verified facts over long unverified prose.

### Maintenance mode

When the user asks for the weekly report, an update to a company, or a quarterly review of an existing atlas, read `references/maintenance.md`. On a Monday, "this week's report" usually means the week that just ended.

## Scripts

All scripts read `atlas.config.yaml` from the atlas root and are copied into the atlas `tools/` folder by `scaffold.py init`. Run them from the atlas root or pass `--root`.

| Script | Purpose |
|---|---|
| `scaffold.py init` / `monitoring` | Create the skeleton; install weekly monitoring templates (Phase 6) |
| `validate_kb.py` | Frontmatter, types, regions, tags, dates, links, anchors, secrets; `--stale N`, `--expect-date`, `--mixed-script` |
| `gen_company_cards.py` | Company cards and master table from YAML records |
| `gen_knowledge_map.py` | Node cards, Knowledge-Map.md and Opportunity-Map.md from YAML nodes |
| `build_opportunity_map.py` | Rebuild the opportunity map after editing node scores |
| `new_weekly_report.py` | Weekly report draft for any ISO week |
| `check_feeds.py` | Verify RSS/Atom feeds and export OPML plus a Markdown table |

Generated headings default to English; translate them by setting `labels:` in `atlas.config.yaml` (keys in `scripts/atlas_common.py`).

## Reference files

| File | When to read |
|---|---|
| `references/intake.md` | Before anything else |
| `references/conventions.md` | Phase 1 (localize it into `00-Overview/Conventions.md`) and whenever unsure about format |
| `references/structure.md` | Phase 1 and when planning files for any section |
| `references/industry-adaptation.md` | Phases 1–2, to fit the method to the chosen industry |
| `references/research-playbook.md` | Before Phase 2A and whenever sources conflict, block access or look stale |
| `references/phase-*.md` | At the start of each phase |
| `references/maintenance.md` | Weekly reports, updates, quarterly reviews |
| `assets/templates/cards/` | Card templates (copied to `99-Templates` by the scaffold) |
| `assets/templates/monitoring/` | Weekly templates (installed in Phase 6) |
