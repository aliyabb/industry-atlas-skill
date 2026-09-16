# Adapting the method to any industry

The folders are universal; what changes is emphasis, data sources and vocabulary. Decide the adaptations in Phase 1 and record them in `00-Overview/Conventions.md` and the folder READMEs.

## 1. Universal vs adaptable sections

| Section | Universal core | Adapt |
|---|---|---|
| Taxonomy | Axes, segment tree, value chain, edge cases | Choose 4–6 axes that really split the industry |
| Segments | Definition, size, players, models, economics, pains, trends | 8–14 segments; merge tiny ones into "Other" |
| Companies | Card schema, master table, failures as case studies | Groups: regions by default; use sub-regions if the industry is concentrated (for example China, US, rest of world) |
| Products | JTBD, features, pricing, reviews | For hardware or services, "pricing" becomes price ranges, contracts, total cost of ownership |
| Pain points | Scored matrix, thematic files, common questions | Data sources (section 3) |
| Keywords | Intent types, clusters, top results | B2B-heavy industries: buyer and comparison queries matter more than volume; ASO only if apps matter |
| Regulation | Calendar, regions, themes, directory | Intensity (section 2); rename to "Policy and Standards" where law is light |
| Trends | Radar and cards | Horizon scales differ (deep tech: 3–10 years) |
| Business models | Catalog, formulas, valuation | Metric set (section 4) |
| Teardowns | 9 blocks | For sales-led B2B add sales process and partner ecosystem; for consumer add app-store presence |
| Content | Platforms, classification, patterns | Platform mix (industrial B2B: LinkedIn, trade media, conferences; consumer: TikTok, YouTube) |
| Knowledge map | Nodes, scores, opportunity map | Nothing specific |
| Monitoring | Follow list, RSS, weekly reports | Replace regulators with the bodies that move the industry (standards bodies, platform policies, agencies) |
| Action guide | Purpose-specific | See `phase-7-action-guide.md` |

## 2. Regulatory intensity

| Intensity | Examples | What `06-Regulations` contains |
|---|---|---|
| High (licences, product approval) | Finance, healthcare and pharma, energy, aviation, telecom, gambling, defence, food | Full treatment: licensing matrix, regional files, calendar, enforcement cases |
| Medium (sector rules, data, safety) | Mobility and EV, edtech, HR tech, cybersecurity, AI products, e-commerce | Cross-cutting themes (privacy, consumer protection, AI rules, product safety), fewer licences |
| Light (general law, platform rules) | Gaming, creator economy, devtools, marketing tech | "Policy and Standards": app-store and platform policies, age ratings, loot-box rules, open standards, industry bodies |

## 3. Pain-point data sources

| Industry type | Structured complaint and review data | Qualitative signals |
|---|---|---|
| Consumer finance | Regulator complaint databases (CFPB, Financial Ombudsman) | Reddit, app stores, Trustpilot |
| Healthcare | FDA adverse-event databases (MAUDE, FAERS), CMS data, patient-experience surveys | Patient forums, clinician communities |
| B2B software | G2, Capterra, TrustRadius ("what do you dislike") | Reddit, Hacker News, vendor community forums |
| Consumer apps and gaming | App Store and Google Play reviews, Steam reviews | Reddit, Discord, YouTube comments |
| Mobility and energy | Safety recall databases, utility complaint data | Owner forums, installer communities |
| Industrial and supply chain | Procurement surveys, trade-association reports | Trade forums, LinkedIn groups |
| Education | Government education statistics, course reviews | Student and teacher communities |

## 4. Business-model metrics

| Model | Core metrics |
|---|---|
| SaaS | ARR, NRR, gross margin, CAC payback, logo churn |
| Marketplace | GMV, take rate, liquidity, repeat rate |
| Payments or transaction | Volume, take rate, cost per transaction, loss rate |
| Lending or insurance | Yield, loss or loss ratio, cost of funds, combined ratio |
| Hardware | Units, ASP, gross margin, attach rate, warranty cost |
| Consumer subscription | Subscribers, ARPU, churn, LTV/CAC |
| Advertising and media | MAU/DAU, ARPU, CPM, engagement time |
| Games | DAU, ARPDAU, retention D1/D7/D30, payer conversion |
| Healthcare services | Patients, reimbursement per episode, utilization, outcomes |
| Energy and infrastructure | Capacity, LCOE, capacity factor, PPA price, capex per unit |
| Biotech and deep tech | Pipeline stage, burn, runway, milestones, licensing deals |

## 5. Taxonomy axes that work

- **Function** (what the product does for the customer).
- **Customer type** (B2C, B2B, B2B2C, B2G).
- **Stack layer** (infrastructure → platforms → applications → services).
- **Monetization model.**
- **Maturity × regulatory load.**
- Industry-specific axes: modality (hardware/software/service), value-chain stage, care setting, energy source, platform (console/PC/mobile), deployment (cloud/on-prem).

## 6. Seed examples

Starting points only; research and adjust.

| Industry | Possible segments |
|---|---|
| Climate tech | Renewable generation, storage, grid and flexibility, EV and charging, building decarbonization, industrial decarbonization, carbon removal and markets, climate data and software, agri-food tech, circularity |
| Healthtech | Telehealth and virtual care, digital therapeutics, health data and interoperability, AI diagnostics, remote monitoring and wearables, provider operations and RCM, payer tech, pharma and clinical-trial tech, consumer health, mental health |
| Gaming | Mobile, PC and console, cloud gaming, engines and tools, live-ops and analytics, monetization and ad tech, esports, UGC platforms, publishing, community and creator tools |
| Cybersecurity | Identity and access, endpoint, network and SASE, cloud security, application security, data security and privacy, security operations, threat intelligence, OT and IoT security, GRC |
| AI infrastructure | Compute and chips, cloud and GPU clouds, foundation models, model tooling and MLOps, data infrastructure, inference and serving, agents and orchestration, evaluation and safety, vertical AI applications |
