---
title: "Template: weekly competitor monitoring"
type: template
tags: [__INDUSTRY_TAG__, monitoring, weekly, competitors]
region: __REGIONS__
updated: __AS_OF__
sources:
  - https://github.com/dgtlmoon/changedetection.io
---

# 🏢 Weekly competitor monitoring

> A 30–45-minute weekly routine: new products, price changes, landing pages, content and keywords of the companies from [09-Competitor-Analysis](../09-Competitor-Analysis/README.md). Results go into section 2 of the [weekly report](Weekly-Industry-Report.md) and into the company cards.

## 1. Watch list

Fill from the Phase 3 teardowns. Verify every URL before adding it (write "checked on YYYY-MM-DD"); mark pages that block scripts with ⚠️.

| Company | Status | News / blog | Pricing | Changelog / docs | Teardown |
|---|---|---|---|---|---|
| {{Company}} | {{public / private}} | {{URL}} | {{URL}} | {{URL or —}} | {{link to the Company-Teardown.md file}} |

💡 Put pricing pages into a page-change monitor (changedetection.io, Visualping) and blogs into an RSS folder.

## 2. Weekly checklist

| Category | What to check | Where |
|---|---|---|
| 🚀 Product | New products, features, markets, partnerships | Newsroom, changelog, founders' posts |
| 💲 Pricing | New plans, fee changes, promotions | Pricing pages, change alerts |
| 🖥️ Landing pages | H1, CTAs, social proof, new menu items | Homepage, change alerts |
| ✍️ Content and SEO | New articles, guides, landing pages for queries | Blog, `site:domain` search for the past week |
| 🔎 Keywords | 3–5 queries per company from [05-Keywords-SEO-ASO](../05-Keywords-SEO-ASO/README.md): position (incognito) and trend | Search engine, Google Trends |
| 👥 People | Key hires and departures, layoffs, open roles | LinkedIn, careers page |
| ⚖️ Regulators | Licences, enforcement, fines | Regulator feeds |
| 💰 Money | Rounds, M&A, earnings, valuation | Deal feeds, investor relations |

## 3. Weekly block

```markdown
### Competitors — week {{WEEK}}

#### Changes
| Company | Category | What changed | Source | Significance (●/●●/●●●) | Atlas file to update |
|---|---|---|---|---|---|
| {{company}} | {{product / price / landing / content / SEO / people / regulation / money}} | {{one line}} | {{URL}} | {{●●}} | {{file}} |

#### Price changes
| Company | Plan or service | Before | After | Source |
|---|---|---|---|---|

#### Content and SEO
| Company | New articles or landing pages | Target queries | Observation |
|---|---|---|---|

#### Takeaways
- Move of the week: {{…}}
- Pattern across competitors: {{…}}
- Idea for your portfolio, pitch or thesis: {{…}}
```

**Significance:** ● small change · ●● new feature or price change · ●●● new product, market, M&A, licence, business-model change.

## 4. Quarterly: public-company results

After each earnings release, update revenue, profit, customers, the segment's key metrics and guidance in the company card and teardown.
