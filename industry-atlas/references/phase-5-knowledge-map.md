# Phase 5 — Knowledge map and opportunity map

**Goal:** one navigable tree that connects every section, with node scores that show where competition is highest, where growth is fastest and where content or supply is missing.

## Nodes

- 8–14 **branches** (usually the segments) and 3–6 **sub-nodes** per branch: 40–60 nodes in total.
- Each node card: overview with dated numbers, key companies (linked cards), tools and technologies, trends, opportunities, regulation, key metrics, scores, parent, children, related nodes, read-more links.

### Scoring rubric (1–5, expert estimate)

| Score | 1 | 3 | 5 | Evidence |
|---|---|---|---|---|
| Competition | Few players | Several funded players | Dominated by scaled leaders, commoditized | Company counts in `02-Companies`, consolidation |
| Growth | Flat or shrinking | Steady | Fastest-growing, capital flowing in | `Funding-VC-Exits`, trend cards, operating metrics |
| Content gap | Well explained everywhere | Some good explainers | Interest outruns quality explanations | `10-Content-Ecosystem`, teardown patterns |
| Supply gap | Pains well served | Partial solutions | Strong pains nobody solves well | `04-Customer-Pain-Points` |

**Attractiveness = growth + content gap + supply gap − competition.** Keep scores comparable across nodes; justify extremes (1 or 5) in the overview.

## Generate

Write `nodes.yaml` outside the repo (schema in the `gen_knowledge_map.py` docstring); give every sub-node a short `label` for the quadrant chart. Then:

```bash
python3 tools/gen_knowledge_map.py /path/to/nodes.yaml
```

It writes `Nodes/*.md`, `Knowledge-Map.md` and `Opportunity-Map.md`, pulls sources from linked files, and lists any link targets that do not exist. Fix paths or create the missing files, then rerun. Later score changes: edit the card frontmatter and run `tools/build_opportunity_map.py`.

## Hand-written files

| File | Content |
|---|---|
| `11-Knowledge-Map/README.md` | Node count, files, how the map differs from the taxonomy, scoring scales, how to update |
| `Cross-Industry-Connections.md` | Links between branches (Mermaid + table with mechanism, example, nodes) and with adjacent industries (how this industry embeds into them, examples, opportunities); 3 key takeaways |
| `12-Opportunities/Content-Gaps.md` | 10–15 thematic gaps tied to high content-gap nodes (why it is a gap, best format, priority) + format and audience gaps + saturated topics to avoid |

Also review the generated `Opportunity-Map.md` conclusions: they should make sense to a domain expert. If they do not, the scores are wrong, not the formula.

## Checkpoint

Share the top 5 by attractiveness, the most crowded nodes and the biggest gaps. Commit `add(knowledge-map): phase 5 — N nodes, opportunity map, cross-industry links`.
