---
title: "Template: weekly content monitoring (100 accounts)"
type: template
tags: [__INDUSTRY_TAG__, monitoring, weekly, content]
region: __REGIONS__
updated: __AS_OF__
sources:
  - https://developers.google.com/youtube/v3/getting-started
---

# 📊 Weekly content monitoring

> In 45–60 minutes a week, find the fastest-growing posts across 100 tracked accounts, understand why they took off, and reuse the pattern. Built on the [content classification](../10-Content-Ecosystem/Content-Classification.md) and [engagement patterns](../10-Content-Ecosystem/Engagement-Patterns.md).

## 1. The 100 tracked accounts

Map them to the Phase 4 platform files so the total is about 100.

| Platform | Count | List | How to track |
|---|---|---|---|
| Newsletters | {{N}} | {{link to the platform file}} | RSS folder, email |
| Podcasts | {{N}} | {{…}} | Podcast app, charts ⚠️ |
| X | {{N}} | {{…}} | X List |
| LinkedIn | {{N}} | {{…}} | Follow + notifications, "Activity" tab |
| YouTube | {{N}} | {{…}} | Channel RSS, "Popular" tab |
| Other | {{N}} | {{…}} | {{…}} |

## 2. Measuring fast growth

Exact analytics for other people's posts do not exist, so use public signals and compare a post with the account's usual level.

| Metric | Formula | "Took off" threshold |
|---|---|---|
| **Engagement velocity** | (likes + 2 × comments + 3 × shares) ÷ hours since posting | Compare within one platform |
| **Outlier score** | Post engagement ÷ median engagement of the account's last 10 posts | ≥ 3 |
| **YouTube** | Views in 7 days ÷ median views of the last 10 videos | ≥ 2 |
| **Newsletters** | Likes and comments, citations by other authors | Cited by 3+ tracked authors |

⚠️ The weights are a heuristic; what matters is measuring the same way every week.

## 3. Process (45–60 minutes)

1. **Collect (20 min):** 20–30 candidates with clearly above-usual reactions.
2. **Score (10 min):** outlier score; keep the top 10.
3. **Analyse (15 min):** format, topic, hook, content type, pattern.
4. **Conclude (10 min):** rising topics, repeated patterns, what to reuse.
5. **Carry over:** topics → report section 3; ideas → personal content plan; demand shifts → content gaps.

🔒 Never commit API keys or tokens: keep them in environment variables or a git-ignored `.env`.

## 4. Weekly block

```markdown
### Content — week {{WEEK}}

#### Top 10 fastest-growing posts
| # | Account | Platform | Format | Topic | Hook (first line) | Engagement | Outlier score | Type (R/S/Sv/C/PB) | Pattern (#) | Link |
|---|---|---|---|---|---|---|---|---|---|---|

#### Topics of the week
| Topic | Posts in top 10 | Knowledge-map node | Change vs last week |
|---|---|---|---|

#### What to reuse
- [ ] Post idea 1 (topic + format + hook): {{…}}
- [ ] Post idea 2: {{…}}
```

## 5. Monthly summary (every 4th week)

| Question | Answer |
|---|---|
| Three topics with the most top-10 posts | |
| Best format per platform | |
| Authors most often in the top 10 | |
| Content gaps that closed | |
| Changes to your own content plan | |
