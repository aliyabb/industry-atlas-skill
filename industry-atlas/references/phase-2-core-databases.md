# Phase 2 — Core databases

The biggest phase, split into four commits. Read `research-playbook.md` first.

## Contents

- 2A Market and segments
- 2B Companies
- 2C Products, pain points, keywords
- 2D Regulation, trends, business models, opportunities

---

## 2A — Market and segments

### Files

| File | Content |
|---|---|
| `00-Overview/Market-Overview.md` | Industry size (revenue, volume, profitability), growth, share of public vs private leaders, key structural shifts, funding climate; 3–5 📌 takeaways |
| `00-Overview/Regional-Breakdown.md` | One section per region: size, leaders, regulation style, specifics; comparison table |
| `00-Overview/Subsector-Market-Sizes.md` | One table: segment, metric, value, year, **metric type** (Rev/Vol/Stock/MR), source, confidence; notes on discrepancies |
| `00-Overview/Funding-VC-Exits.md` | VC funding by year and quarter (name the sources and their methodology differences and revisions), top rounds, IPOs, M&A, valuation benchmarks |
| `00-Overview/Glossary.md` | 100+ terms: term (English) — definition in the content language — link to the section |
| `01-Segments/<Seg>/<Seg>-Overview.md` | One per segment, from `Segment-Card-Template` |
| Explainers | 3–5 files where money flow or unit economics are non-obvious (value chain walkthrough, unit economics per model with a worked example) |

### Segment card essentials

Definition and boundaries → sub-segments → value chain (Mermaid) → size and growth (metric types) → global and regional leaders → incumbents → business models → unit economics with a worked example → regulation → trends → customer pains → opportunities and threats → success and failure cases → angle for the user's purpose → links → open questions.

---

## 2B — Companies

### Selection (standard: 100–200)

- Leaders of every segment in every focus region.
- Fast risers funded in the last 24 months.
- Incumbents that shape the market.
- 3–6 notable failures as case studies.
- Balance: at least 5 companies per segment; regions weighted by the user's focus.

### Data → cards

Write YAML records in batches of about 30, outside the repo, then generate:

```yaml
- file: Checkout-com
  name: Checkout.com
  group: UK                     # key from company_groups
  country: United Kingdom
  founded: 2012
  regions: [global, uk, eu]
  segment: payments             # key from config segments
  subsegment: Enterprise acquiring
  customer_types: [b2b]
  status: private               # private | public | acquired | defunct
  ticker: ""
  status_note: ""
  website: https://www.checkout.com
  summary: One sentence on what it does and for whom.
  why: ["Position with a dated metric", "What makes the model distinctive"]
  people: "Founder: … (CEO)"
  funding: "~$1.8B ⚠️"
  valuation: "$12B (internal valuation, 2025) (B)"
  investors: "Tiger Global, Coatue ⚠️"
  products: ["Acquiring", "Payouts"]
  customers: "Enterprise merchants"
  model: "Take rate on processed volume"
  pricing: "Custom, IC++"
  metrics: ["Revenue: $X (FY2025) (A)"]
  competitors: [Stripe, Adyen]  # names or file names; linked when a card exists
  events: ["2026-03: …"]
  angle: "Roles hired, product problems, what to read before an interview"
  sources: [https://www.checkout.com/newsroom/...]
  checks: ["Latest valuation after secondary sales"]
  tags: [acquiring]
```

```bash
python3 tools/gen_company_cards.py /path/to/data/companies-*.yaml
```

The script validates the records, writes one card per company, links competitors, and rebuilds `02-Companies/README.md` with stats and group tables. Rerun after fixing data. Once the cards are committed, edit cards directly and update the matching master-table row by hand.

### Quality bar

Every company has at least one dated metric or a clearly marked `n/a`; private valuations have a date and confidence; social links are search links.

---

## 2C — Products, pain points, keywords

### 03-Products (15–25 categories)

From `Product-Card-Template`: job to be done, features by tier, pricing models, a brand comparison with **public prices and review scores with dates**, pros and cons, what users say (paraphrased), MVP checklist, angle.

### 04-Customer-Pain-Points

| File | Content |
|---|---|
| `Pain-Points-Matrix.md` | 25–35 pains scored 1–5 on **Frequency (F)**, **Severity (S)**, **Willingness to pay (W)**, **Gap (G)**; **Priority = F × S × (W + G)**; evidence column with data sources |
| 4–6 thematic files | By customer type or segment: structured complaint data first (see `industry-adaptation.md`), then review themes and community signals |
| `Common-Questions.md` | 80+ real questions customers ask, grouped, with the section that answers them |

### 05-Keywords-SEO-ASO

| File | Content |
|---|---|
| `Keyword-Strategy-Overview.md` | Industry SEO specifics, a 7-step process, prioritization formula (for example demand × intent value × winnability), page types and the queries they serve, metrics |
| Cluster files | One per segment group: commercial, informational, comparison, local queries; volumes as ranges marked as estimates unless taken from a named tool |
| `ASO-Keywords.md` | Only if apps matter |
| Audience keywords | Career queries and Boolean job-search strings (career), buyer queries (founder), deal and data queries (investor) |

---

## 2D — Regulation, trends, business models, opportunities

### 06-Regulations

- `README.md` with a **calendar** for the next 2–3 years: date, jurisdiction, event, status (✅ in force / ⚠️ scheduled or uncertain).
- One file per focus region: regulators, key laws, licences, current changes.
- 5–9 cross-cutting themes (for example data privacy, AI rules, consumer protection, product safety, cross-border).
- `Licensing-Matrix.md` or `Standards-and-Certifications.md`; `Regulators-Directory.md` (body, jurisdiction, remit, official site).
- Stage words matter: proposed, agreed, adopted, in force, applies from. Mark anything not final.

### 07-Trends (12–20 cards)

`README.md` with a **radar table**: trend, maturity (emerging / early growth / scaling / mature), speed 1–5, impact 1–5, relevance to the user's purpose 1–5, horizon; a Mermaid graph of how trends connect; the 3 trends to study first. Cards follow `Trend-Card-Template` (signals with dates, drivers, players, numbers, winners and losers, counter-arguments, opportunities, angle).

### 08-Business-Models

`Revenue-Models-Catalog` (model, mechanics, typical margin, examples), `Unit-Economics-Formulas` (formula, benchmark, why it matters), 3–5 deep dives on the dominant models, `Valuation-Basics` (multiples by model with dated benchmarks), `Business-Model-Canvas-Examples` (3–5 companies).

### 12-Opportunities

`README.md` with the scoring framework:

| Criterion | Weight |
|---|---|
| Market size | 20% |
| Growth | 20% |
| Competition (inverted) | 15% |
| Regulatory or entry barrier (inverted) | 15% |
| Pain severity and willingness to pay | 20% |
| Fit with the user's profile | 10% |

`Opportunities-Overview.md` ranks 10–15 opportunities; write cards (`Opportunity-Card-Template`) for the top 6–10, each tied to a pain from the matrix and a trend or regulatory change ("why now").

## Checkpoints

After each of 2A, 2B, 2C and 2D: validate, update the root README, commit, push, and summarize the most important findings (with ⚠️ items) before continuing.
