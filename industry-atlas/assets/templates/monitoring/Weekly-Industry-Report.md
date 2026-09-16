---
title: "Template: weekly industry report"
type: template
tags: [__INDUSTRY_TAG__, monitoring, weekly, report]
region: __REGIONS__
updated: __AS_OF__
sources:
  - https://www.google.com/alerts
---

# 📰 Weekly industry report template

> The main artifact of the monitoring system: once a week (1.5–2 hours) collect what happened, what took off, deals, new signals, regulation and opportunities, then update the atlas. Archive: [Reports](Reports/README.md).

## How to use

1. **Create a draft:** `python3 tools/new_weekly_report.py [YYYY-MM-DD]` (any date inside the target ISO week; on a Monday, use a date from last week).
2. **During the week:** add links to section 0 (one line: link and why it matters).
3. **At the end of the week:** fill sections 1–10 using [competitor monitoring](Weekly-Competitor-Monitoring.md) and [content monitoring](Weekly-Content-Monitoring.md).
4. **Update the atlas** with the checklist in section 9, validate, commit `monitor: weekly report YYYY-Www`.

## Rules

- Every fact has a link; check that the publication date falls inside the week.
- **Significance:** ● good to know · ●● affects a segment · ●●● changes the game.
- At most 10 events in section 2: a report is a selection, not a feed.

<!-- REPORT-START -->

# 📰 Weekly report {{WEEK}} · {{DATE_FROM}}–{{DATE_TO}}

> Draft created from the [template](Weekly-Industry-Report.md). Replace the `{{...}}` hints and delete empty rows.

## 0. Draft notes

- {{link — one line on why it matters}}

## 1. TL;DR

1. {{main event and why it matters}}
2. {{second story}}
3. {{signal to watch}}

## 2. What happened

| Date | Event | Region | Knowledge-map node | Significance | Source |
|---|---|---|---|---|---|
| {{DD.MM}} | {{event}} | {{US}} | {{node}} | {{●●}} | {{URL}} |

Nodes: [Knowledge-Map](../11-Knowledge-Map/Knowledge-Map.md).

## 3. What took off

| Post or discussion | Platform | Why it took off | Link |
|---|---|---|---|
| {{…}} | {{…}} | {{pattern}} | {{URL}} |

## 4. Funding, M&A, IPOs

| Company | Deal | Amount / valuation | Investors or acquirer | Segment | Source |
|---|---|---|---|---|---|
| {{…}} | {{Series B}} | {{$50M / $400M}} | {{…}} | {{…}} | {{URL}} |

Week summary: {{number of in-scope deals, total recomputed from the verified list, concentration}}. Context: [02-Companies](../02-Companies/README.md).

## 5. New trends and signals

| Signal | Trend or node | Strength (weak / medium / strong) | What would confirm it |
|---|---|---|---|
| {{…}} | {{…}} | {{…}} | {{…}} |

Trend radar: [07-Trends](../07-Trends/README.md).

## 6. Regulation and policy

| Date | Jurisdiction | What came into force, was published or is debated | Who is affected | Source |
|---|---|---|---|---|
| {{…}} | {{…}} | {{…}} | {{…}} | {{URL}} |

Upcoming dates from the [calendar](../06-Regulations/README.md): {{2–3 dates for the next 4 weeks}}.

## 7. Opportunities

- {{new pain, gap or change that opens a niche}} → {{existing card or new idea}}

Register: [12-Opportunities](../12-Opportunities/README.md) · [Opportunity-Map](../11-Knowledge-Map/Opportunity-Map.md).

## 8. For your plan

| Company or item | Signal (hiring, layoffs, deadline, event) | Relevance | Link |
|---|---|---|---|
| {{…}} | {{…}} | {{…}} | {{URL}} |

Plan: [__ACTION_GUIDE__](../__ACTION_GUIDE__/README.md).

## 9. Atlas updates

- [ ] Company cards and master-table rows
- [ ] Regulation files and the calendar
- [ ] Trend cards
- [ ] Knowledge-map scores, then `python3 tools/build_opportunity_map.py`
- [ ] Added or removed ⚠️
- [ ] Root README changelog (if the change is big)
- [ ] `python3 tools/validate_kb.py` clean, commit `monitor: weekly report {{WEEK}}`

## 10. Questions for next week

- {{what to check or watch}}
