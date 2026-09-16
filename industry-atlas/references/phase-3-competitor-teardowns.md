# Phase 3 — Competitor reverse-engineering

**Goal:** understand how the leaders win customers, and extract patterns, saturated tactics and gaps the user can exploit (as a candidate, founder or investor).

## Selection (standard: 10–20)

Cover every major segment, both self-serve and sales-led models, consumer and business, and at least two regions. Include one or two challengers, not only giants. Link each to its company card.

## 9-block framework

| # | Block | What to analyse | How |
|---|---|---|---|
| 1 | Navigation and structure | Menu groupings (product, size, industry, use case), depth | Fetch the homepage; list top-level menu items |
| 2 | Product collections | Lineup, what is featured first, bundles | Homepage and product pages |
| 3 | Pricing page | Model, transparency, anchors, plan ladder, enterprise path | Fetch the pricing page; record prices with the date |
| 4 | SEO structure | Titles, hubs, programmatic pages, comparisons, glossaries, calculators | `site:domain` searches, sitemap if public, URL patterns |
| 5 | Content marketing | Blog, guides, reports, tools, events, newsletters | Content hub pages |
| 6 | Social media | Platforms and formats (no invented follower counts) | Official links from the site footer |
| 7 | Channels and funnels | PLG, sales, partners, referrals, marketplaces | CTAs, signup flow, partner pages |
| 8 | Conversion tactics | CTAs, social proof, incentives, demos, trials, trust badges | Homepage and landing pages |
| 9 | Monetization | How the site reveals the revenue model | Pricing, terms, investor materials |

Finish each teardown with **3 lessons**, **what to borrow**, and an **angle** (for career: "what would you change on their homepage?").

## Method notes

- Many sites block automated fetches (403) or render client-side. Try alternate pages (pricing, newsroom, help center); otherwise use search results and archived descriptions, and mark the teardown ⚠️ with "recheck manually in a browser".
- Record prices and plans with the check date.
- Do not use paid SEO tools' data unless the user provides it; describe structure, not traffic numbers.

## Files

| File | Content |
|---|---|
| `README.md` | Method, data date, blocked sites, table (company, segment, main lesson, link), the 9-block framework |
| `<Company>-Teardown.md` | Type `report`, from `Teardown-Template` |
| `Pricing-Pages-Comparison.md` | Model, entry price, plan ladder, transparency score, enterprise path, date |
| `Patterns-Summary.md` | Recurring patterns (navigation, trust, SEO, conversion), what works, what is saturated, **gaps** (link to opportunities), how to use for the user's purpose |

## Checkpoint

Share the top patterns and gaps. Commit `add(competitors): phase 3 — N teardowns, pricing comparison, patterns`.
