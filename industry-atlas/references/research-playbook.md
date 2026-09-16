# Research playbook

Lessons from building a full atlas: where research goes wrong and how to keep the facts trustworthy without slowing down.

## 1. Work in parallel batches

- List the facts a file needs, then fire all independent searches and fetches in one turn (8–12 at a time). Write the file once the results are in.
- Search in English even for a non-English atlas; the best primary sources usually are.
- Add the year or month to queries ("… September 2026") to push fresh results up.

## 2. Prefer primary sources

| Need | Best source (A) | Acceptable (B) |
|---|---|---|
| Company metrics | Filings (10-K, annual report), investor letters, earnings releases | Reuters, Bloomberg, FT, trade press |
| Funding and valuation | Company or lead-investor announcement | TechCrunch, sector media; aggregators only as C |
| Regulation | Official journal, regulator site, bill text | Law-firm briefings (good for timelines) |
| Market size | Official statistics, operational data (volumes, deposits, installed base) | Large consultancies; market-research "market size" = C |
| Events and dates | Organizer site | Event aggregators ⚠️ |

## 3. Verify dates on every "news" item

Search engines resurface old articles. In one real week, two "new" funding rounds turned out to be from 2021 and 2024. Before including any event:

1. Check the publication date on the page or in the URL.
2. Confirm with a second source if the date is unclear.
3. Recompute totals from the verified list rather than copying a headline sum.

## 4. Handle blocked or partial pages

- A 403 or an empty page from WebFetch is common (banks, large consumer apps, paywalled media). Try the company newsroom, an investor-relations page, or a press-release wire; otherwise rely on two independent secondary sources and lower the confidence.
- If an article hides the key fact (for example "a listed company agreed to buy its long-time supplier"), search for the specific details (price, date) to find the named source.
- Never cite a URL you have not seen in search results or fetched.

## 5. Resolve conflicting numbers

- Classify each figure by **metric type**: `Rev` (revenue of companies), `Vol` (transaction volume, GMV, shipments), `Stock` (deposits, AUM, installed base, market cap), `MR` (market-research "market size"). Different types are not contradictions; put them side by side.
- For true conflicts, show both values with sources, explain the methodology difference, and add the marker.
- Note revisions: quarterly industry reports often revise earlier periods; say which edition you use.
- Operational numbers are usually the most reliable; agency "market size" figures are usually C.

## 6. Watch aggregate figures

Weekly or quarterly "sector totals" can be dominated by out-of-scope deals (an AI mega-round counted inside the sector). Recompute an in-scope total and state the method.

## 7. People, social and audiences

- Link social profiles through platform search pages unless the profile URL came from a verified source.
- Follower counts change daily and scrapes are unreliable: use audience tiers **S** (<10K), **M** (10–100K), **L** (100K–1M), **XL** (1M+) with the marker, and exact numbers only from a dated primary source.
- Public professional information only.

## 8. Feeds, events, prices, visas, deadlines

- Feeds: verify with `check_feeds.py`; many sites block scripts but work in readers, so report those separately.
- Event dates, programme deadlines, prices and visa thresholds: write "checked on YYYY-MM-DD" and link the official page. These go stale fastest.
- Immigration, legal, tax and investment topics: state that the content is not professional advice.

## 9. Memory vs research

Your training data has a cutoff; the atlas describes "now" (the environment date). Anything that may have changed (valuations, leaders, regulation stages, market shares, product lineups) must be researched. If research is impossible, write the fact from memory with the marker and the date it was last known.

## 10. Copyright

Summarize in your own words. At most one short quote per file, in quotation marks with attribution. Do not reproduce tables or charts from paid reports; cite the figure and the report.
