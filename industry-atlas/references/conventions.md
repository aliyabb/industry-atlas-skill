# Conventions

In Phase 1, write a localized version of this file to `00-Overview/Conventions.md` with the real industry tag, segment tags and examples. The validator enforces the machine-checkable parts.

## Contents

1. Frontmatter
2. Document types
3. Regions
4. Tags
5. File and folder names
6. Links
7. Data and confidence
8. Markers
9. Updates and commits
10. Security and ethics

## 1. Frontmatter

Every `.md` file starts with:

```yaml
---
title: "Stripe"
type: company
tags: [aiagents, tooling, b2b, private]
region: [global, us]
updated: 2026-09-14
sources:
  - https://stripe.com/
  - https://www.sec.gov/...
---
```

| Field | Rule |
|---|---|
| `title` | Quoted string. Company names in original spelling; topics in the content language |
| `type` | One value from section 2 |
| `tags` | List of 3–8 kebab-case English tags; **the first tag is always the industry tag** |
| `region` | List, even with one value: `[us]` |
| `updated` | `YYYY-MM-DD` of the last substantive change (not in the future) |
| `sources` | List of URLs; primary sources first (company, regulator, filing), then secondary |

Optional extended fields go after the required ones (for Obsidian Dataview): `country`, `founded`, `segment`, `status`, `ticker`, `last_valuation_usd`, `market_size_usd`, `effective_date`, `competition`, `growth`… Each template lists its own.

## 2. Document types

| `type` | Describes | Lives in |
|---|---|---|
| `company` | One company | `02-Companies/` |
| `segment` | Segment, sub-segment or knowledge-map node | `01-Segments/*/`, `11-Knowledge-Map/Nodes/` |
| `product` | Product category | `03-Products/` |
| `trend` | Trend or shift | `07-Trends/` |
| `regulation` | Law, regime, regulator, licence, policy | `06-Regulations/` |
| `keyword` | Keyword cluster | `05-Keywords-SEO-ASO/` |
| `content-source` | Content source | `10-Content-Ecosystem/` |
| `opportunity` | Opportunity, niche, pain-point analysis | `12-Opportunities/`, `04-Customer-Pain-Points/` |
| `person` | Public figure | optional `02-Companies/People/` |
| `index` | Folder index (every `README.md`) | everywhere |
| `guide` | Method, rules, how-to | `00-Overview/`, action guide, monitoring |
| `template` | Template description or weekly template | `99-Templates/`, `14-Monitoring/` |
| `map` | Map, matrix, overview table | `00-Overview/`, `11-Knowledge-Map/` |
| `report` | Periodic report or comparative teardown | `14-Monitoring/Reports/`, `09-Competitor-Analysis/` |

Add industry-specific types only if really needed, via `extra_types` in the config.

## 3. Regions

| Value | Covers |
|---|---|
| `global` | Real presence on 3+ continents; not a default |
| `us` | United States (Canada noted in text unless you add a value) |
| `eu` | EU/EEA and Switzerland |
| `uk` | United Kingdom |
| `asia` | Asia-Pacific incl. India, Australia; add country tags (`india`, `singapore`) for detail |
| `latam` | Latin America incl. Mexico |
| `mena` | Middle East and North Africa |
| `africa` | Sub-Saharan Africa |

Change `region_values` in the config if the industry needs another split, and document it here.

## 4. Tags

Lowercase kebab-case, English, singular. Region goes in `region`, not tags (country tags are the exception). Define in Phase 1:

- **Segment tags**, one per segment (equal to the segment `key` in the config), plus sub-segment tags.
- **Customer type:** `b2c`, `b2b`, `b2b2c`, `b2g`.
- **Company status:** `private`, `public`, `acquired`, `defunct`, `unicorn`.
- **Monetization:** industry-specific (`saas`, `take-rate`, `subscription`, `usage-based`, `hardware-margin`, `advertising`, `licensing`…).
- **Cross-cutting:** `ai`, `market`, `funding`, `m-and-a`, `ipo`, `regulation`, `case-study`, `failure`.
- **Action guide:** `career`, `pm`, `interview`, `skills`, `networking`, `job-board`, `certification` (or founder/investor equivalents).
- **Service:** `index`, `meta`, `template`, `monitoring`, `weekly`, `needs-verification`.

## 5. File and folder names

| Object | Rule | Example |
|---|---|---|
| Folder index | Always `README.md` | `02-Companies/README.md` |
| Company | Official brand, spaces → hyphens, no legal form, no dots | `Checkout-com.md`, `N26.md` |
| Topic or segment | English `Title-Case-With-Hyphens` | `Real-Time-Payments.md` |
| Regulation | Official abbreviation plus qualifier | `EU-AI-Act.md` |
| Knowledge-map node | `Branch--Sub-Node.md` | `Payments--Wallets.md` |
| Weekly report | ISO week | `2026-W38.md` |
| Folders | Number prefix only at top level | `01-Segments/Payments/` |

English file names keep links stable in terminals, on GitHub and across languages.

## 6. Links

- Relative links only; they survive renames and work in Obsidian.
- Case matters on GitHub.
- Never link to a file that does not exist yet; write the name as `code`.
- Anchors follow GitHub slugs (lowercase, punctuation dropped, spaces → hyphens) and depend on the heading language, so avoid anchors in reusable templates.

## 7. Data and confidence

### 7.1 Numbers

| What | Format | Example |
|---|---|---|
| Money | Currency, number, scale K/M/B/T, period | `$1.4T volume (2025)` |
| Growth | CAGR with years | `CAGR 18% (2024–2030, forecast)` |
| Users | Say which users and who claims it | `50M+ customers (company, Q2 2026)` |
| Currency conversion | Rate and date | `≈$3.2B at the 2026-06-30 rate` |

### 7.2 Confidence

| Level | Source |
|---|---|
| **A** | Filings, regulator data, official statistics, company press release about its own deal |
| **B** | Reputable media and analysts (Reuters, Bloomberg, FT, sector trade press, large consultancies) |
| **C** | Aggregator estimates, market-research "market size" figures, undisclosed methodology, leaks |

Write it next to the number: `(A, 10-K 2025)`, `(C, estimate) ⚠️`.

### 7.3 Verification marker

Use the marker when data is older than 12 months, confidence is C, sources differ by >20%, or the status is moving. Format: **⚠️ NEEDS VERIFICATION:** *what* → *where to check*.

## 8. Markers

| Marker | Meaning |
|---|---|
| ⚠️ | Needs verification |
| 📌 | Key insight |
| 💡 | Opportunity or idea |
| 🎯 | Angle for the user's purpose (career, founder, investor) |
| ❓ | Open question |
| 🔄 | Outdated or replaced |
| 🟢 / 🟡 / ⚪ | Section status: done / in progress / scaffold |

## 9. Updates and commits

On every change: update data, add the source, bump `updated`, adjust ⚠️, and for big changes add a changelog row in the root README.

Commit format `type(section): summary`:

| Type | When | Example |
|---|---|---|
| `add` | New cards or files | `add(companies): phase 2B — 180 company cards` |
| `update` | Data refresh | `update(companies): Stripe valuation 2026` |
| `fix` | Errors, broken links | `fix(segments): broken link in Payments` |
| `structure` | Structure, templates, conventions | `structure: phase 1 — taxonomy and conventions` |
| `monitor` | Weekly report or monitoring | `monitor: weekly report 2026-W37` |

End commit messages with the attribution line the environment requires, if any.

## 10. Security and ethics

- Never commit tokens, API keys, passwords or `.env` files; `.gitignore` lists the patterns and `validate_kb.py` scans for leaks.
- People: public professional information only; no private contacts or personal life.
- Copyright: summarize in your own words and link the source; no full articles or reports.
- Personal job-search trackers and contact lists stay outside the repository.
