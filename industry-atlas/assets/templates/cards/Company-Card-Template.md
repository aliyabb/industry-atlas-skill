---
title: "{{Company name}}"
type: company
tags: [__INDUSTRY_TAG__, "{{segment-tag}}", "{{subsegment-tag}}", "{{b2c|b2b|b2b2c}}", "{{private|public|acquired|defunct}}"]
region: ["{{us}}"]
updated: "{{YYYY-MM-DD}}"
sources:
  - "{{https://official-site}}"
  - "{{https://filing-or-announcement}}"
# --- extended fields (Dataview) ---
country: "{{HQ country}}"
founded: "{{YYYY}}"
segment: "{{segment-key}}"
subsegment: "{{sub-segment}}"
status: "{{private|public|acquired|defunct}}"
ticker: "{{EXCHANGE:TICKER or empty}}"
website: "{{https://...}}"
last_valuation_usd: "{{$X.XB (YYYY-MM, source)}}"
employees: "{{~N (YYYY, source)}}"
---

# {{Company name}}

> {{One sentence: what the company does and for whom.}}

<!-- Every number has a period and a source; doubtful data gets ⚠️ with what to check and where. Links are relative: [Competitor](Competitor.md) -->

## 📇 Snapshot

| Field | Value |
|---|---|
| Country (HQ) | {{country, city}} |
| Founded | {{YYYY}} |
| Segment / sub-segment | {{[Segment](../01-Segments/Folder/Segment-Overview.md)}} / {{sub-segment}} |
| Customer type | {{B2C / B2B / B2B2C}} |
| Status | {{Private / Public (exchange: ticker) / Acquired (by whom, when) / Defunct}} |
| Employees | {{~N (YYYY)}} |
| Website | {{https://...}} |
| Social | {{LinkedIn and X search links}} |
| Key markets | {{US, EU…}} |

## 🧭 Why it matters

- {{Market position with a dated metric}}
- {{What is distinctive about the model or technology}}
- {{What this case teaches}}

## 👥 Founders and key people

| Name | Role | Background |
|---|---|---|
| {{Name}} | {{Co-founder & CEO}} | {{previous companies, education}} |

## 💰 Funding and valuation

| Date | Round | Amount | Valuation | Lead investors | Source |
|---|---|---|---|---|---|
| {{YYYY-MM}} | {{Seed … IPO / tender}} | {{$XM}} | {{$XB}} | {{investor}} | {{link}} |

## 🧩 Products and services

| Product | What it does | For whom | Launched |
|---|---|---|---|
| {{Product}} | {{…}} | {{…}} | {{YYYY}} |

## 🎯 Target customers

- **Ideal customer profile:** {{…}}
- **Geography and size segments:** {{…}}

## 💵 Business model and pricing

| Revenue stream | Mechanics | Share of revenue |
|---|---|---|
| {{stream}} | {{how it earns}} | {{X% (FY, source)}} |

- **Public pricing:** {{…}}, [pricing page]({{https://...}})

## 📊 Key metrics

| Metric | Value | Period | Source | Confidence |
|---|---|---|---|---|
| Revenue | {{$X}} | {{FY2025}} | {{filing}} | {{A/B/C}} |
| Customers / users | {{X}} | {{Q2 2026}} | {{…}} | {{…}} |

## ⚔️ Competitors

| Competitor | Type | Key difference | Card |
|---|---|---|---|
| {{Company}} | {{direct / indirect / incumbent}} | {{…}} | {{[Company](Company.md) or "coming"}} |

## 🏛️ Regulation and licences

| Jurisdiction | Licence / status | Regulator |
|---|---|---|
| {{…}} | {{…}} | {{…}} |

## 🗓️ Timeline

| Date | Event |
|---|---|
| {{YYYY-MM}} | {{launch / round / M&A / IPO}} |

## ⚠️ Risks and weak spots

- {{concentration, regulation, partners, competition}}

## 🎯 Angle for you

| Question | Answer |
|---|---|
| Roles they hire | {{…}}, [careers page]({{https://...}}) |
| Product problems they likely work on | {{…}} |
| Metrics that matter | {{…}} |
| What to read before an interview or meeting | {{annual report, blog, recent launches}} |

## 🔗 Links

- **Segment:** {{link}} · **Products:** {{link}} · **Trends:** {{link}} · **Teardown:** {{link if any}}

## ✅ Verification checklist

- [ ] Status current (not acquired or closed)
- [ ] Latest valuation or market cap with a date
- [ ] Key metrics not older than 12 months
- [ ] Leadership current
- [ ] Every ⚠️ says what to check and where
