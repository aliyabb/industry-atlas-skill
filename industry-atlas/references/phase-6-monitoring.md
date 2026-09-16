# Phase 6 — Monitoring system

**Goal:** a routine that keeps the atlas current in about 20–30 minutes a day and 2 hours a week.

## 1. Follow-List-Top-50.md

Distil the content ecosystem plus institutions into 50 sources with priorities:

| Priority | Frequency | Count |
|---|---|---|
| A | Daily | ~5 |
| B | Weekly | ~20 |
| C | When published / monthly | ~25 |

Categories: newsletters, media and research, podcasts, YouTube, X, LinkedIn, Reddit and communities, **regulators or standards bodies**, **investors (VC funds, analysts)**, company blogs. Columns: #, source, region, priority, why, link, RSS status (✅ verified / 📧 email only / ❌ no RSS / ⚠️ blocked or not found). Add a coverage-by-region table and a "bench" of extra sources per user goal.

## 2. RSS

1. Collect candidate feed URLs into `feeds.yaml` (outside the repo): common patterns are `/feed`, `/rss`, `/rss.xml`, `/feed.xml`, Substack `/feed`, Reddit `/r/<name>/.rss`, YouTube `https://www.youtube.com/feeds/videos.xml?channel_id=<ID>`.
2. Verify and export:

```bash
python3 tools/check_feeds.py feeds.yaml --opml 14-Monitoring/feeds.opml --markdown /tmp/feeds-table.md
```

3. Write `RSS-Setup.md`: reader options (Inoreader, Feedly, NetNewsWire, Readwise Reader; mark plan prices ⚠️), a 60-minute quick start (import OPML), the verified-feeds table with the check date, sources without working RSS and what to do (email subscription, Google Alerts RSS, page-change monitoring), keyword filter groups (deals, regulation, trends, competitors, audience keywords), and a security note: never commit personal feed URLs containing tokens.

## 3. Weekly templates

```bash
python3 <skill-dir>/scripts/scaffold.py monitoring --root .
```

This installs `Weekly-Industry-Report.md`, `Weekly-Competitor-Monitoring.md` and `Weekly-Content-Monitoring.md`. Then:

- Translate them into the content language (keep `<!-- REPORT-START -->`, `{{WEEK}}`, `{{DATE_FROM}}`, `{{DATE_TO}}`).
- Fill the competitor watch list (from Phase 3) with verified newsroom, pricing and changelog URLs.
- Map the "100 accounts" in the content template to the platform files from Phase 4.

`scaffold.py` stays in the skill (it needs the bundled templates), so call it from the skill directory with `--root`.

## 4. Auto-Update-Instructions.md

- **Principles:** one place of truth, source plus date on every change, marker removed only after verification, small commits.
- **Rhythm table:** daily, weekly, monthly (⚠️ review, `--stale 90`), quarterly (reports, re-scoring), yearly (market sizes, taxonomy).
- **Triggers table:** event → files to update (funding round, M&A, IPO, shutdown, product launch, price change, new regulation or deadline, enforcement, new market data, trend signal, score change, new complaints data, new content source, new segment).
- **Card update steps** with git commands.
- **Automation levels:** L0 manual templates, L1 RSS and page monitoring, L2 scripts in `tools/`, L3 AI-assistant prompts (weekly report, company update, quarterly re-score), L4 scheduling (cron, GitHub Actions validation workflow; note it needs the `workflow` token scope to push).
- **Quality control commands** and **security rules**.

## 5. Reports

- `Reports/README.md`: archive table (week, dates, file, headline), newest first.
- A **baseline report** for the current week: the state of the market from the atlas, a regulatory calendar for the next 6–10 weeks, signals to watch, and a checklist. Label it a baseline; do not present old events as this week's news.

## Checkpoint

Commit `add(monitoring): phase 6 — follow list, N verified feeds, weekly templates, update guide`. Tell the user how to import the OPML and when the first real weekly report is due.
