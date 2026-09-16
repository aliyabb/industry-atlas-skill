# Maintenance mode

Use this when the atlas exists and the user asks for the weekly report, an update, or a review.

## Weekly report

1. **Pick the week.** Check today's date (`date`). A report requested on Monday or early in the week usually covers the ISO week that just ended; one requested late in the week can cover the current week. If a baseline report already occupies the current week, report on the previous week. Say which week you chose.
2. **Create the draft:** `python3 tools/new_weekly_report.py <any date in that week>`.
3. **Research in parallel batches**, one query per section with the month and year:
   - funding rounds, acquisitions, IPOs in the industry;
   - regulation and policy news per focus region, plus items from the atlas calendar that fell due;
   - news of the companies in `09-Competitor-Analysis` and the top of the master table;
   - trend signals (the hottest nodes in the opportunity map);
   - layoffs and hiring; programme deadlines for the user's purpose;
   - notable content and debates.
4. **Verify** each item: publication date inside the week (old articles resurface), a named primary or reputable source, industry-only totals recomputed. Put earlier-week items needed for context in a separate "context" table.
5. **Fill every section**; be honest where data is missing (for example "no engagement measurement this week" rather than inventing viral posts). Mark analysis and inferences with the marker.
6. **Update the atlas** using the triggers table in `14-Monitoring/Auto-Update-Instructions.md`: company cards and master-table rows, trend signals, regulation statuses. Tick the report's checklist.
7. **Add the report** to `Reports/README.md`, validate, commit `monitor: weekly report YYYY-Www`, push.
8. **Reply** with the 3–5 headline items, what was updated, what remains open, upcoming deadlines, and the sources.

## Company or topic update

Research → edit the card (data, sources, `updated`, marker) → sync the master-table row and linked trend or node → validate → `update(<section>): …`.

## Quarterly review

- Re-score knowledge-map nodes from the quarter's evidence, show the before/after table to the user, then run `tools/build_opportunity_map.py`.
- Refresh the trend radar, market sizes from new quarterly reports, and public-company metrics after earnings.
- Run `python3 tools/validate_kb.py --stale 90` and refresh or re-mark stale cards.
- Commit `update(...)` per section and add a changelog row.

## Questions mid-run

If the user asks something while you are working (for example "what is an OPML file and how do I import it?"), answer it briefly and plainly, then continue the task.
