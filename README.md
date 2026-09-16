# Industry Atlas — Claude skill

A Claude skill that builds a **research-backed, continuously updatable knowledge base about any industry**: a private GitHub repository of interlinked Markdown files (works in Obsidian) with a market overview, taxonomy, segments, 100–200 company cards, products, customer pain points, keywords, regulation, trends, business models, competitor teardowns, a content ecosystem, a knowledge map with opportunity scoring, a weekly monitoring system and a personal action plan.

The method is a 7-phase build: structure and taxonomy, core databases, competitor teardowns, the content ecosystem, a knowledge map with opportunity scoring, a monitoring system, and an action plan for your own goal.

## Install

**Claude Code** (personal skill, available in every project):

```bash
git clone https://github.com/aliyabb/industry-atlas-skill.git
mkdir -p ~/.claude/skills
cp -R industry-atlas-skill/industry-atlas ~/.claude/skills/
```

Restart Claude Code and check that `industry-atlas` appears in the skill list. To update later: `git pull` and copy again.

**Claude.ai / Claude desktop:** download `industry-atlas.skill` from the [latest release](https://github.com/aliyabb/industry-atlas-skill/releases/latest) and upload it (Settings → Capabilities → Skills).

Requirements: `git`, GitHub CLI (`gh auth login`), Python 3.9+ with PyYAML (`pip install pyyaml`), and web search/fetch tools for research.

## Use

Just describe what you want; the skill triggers on requests like:

- "Build me a knowledge base about AI agents, in English, private repo, I want to become a PM."
- "Map the gaming industry end to end and push it to my GitHub. Pause after each phase."
- "I'm considering a healthtech startup. Build an industry atlas with a founder playbook."
- "Make this week's report for my cybersecurity atlas."

The skill runs an intake (industry, purpose, background, regions, language, repo, depth, autonomy), confirms the plan, scaffolds the repo, then works phase by phase:

| Phase | Output |
|---|---|
| 1 | Structure, conventions, taxonomy, templates, private repo |
| 2A–2D | Market and segments · companies · products, pain points, keywords · regulation, trends, business models, opportunities |
| 3 | Competitor teardowns, pricing comparison, patterns and gaps |
| 4 | Content ecosystem (100+ sources), classification, engagement patterns |
| 5 | Knowledge map, opportunity map, cross-industry links, content gaps |
| 6 | Top-50 follow list, verified RSS + OPML, weekly templates, update guide, baseline report |
| 7 | Action guide for your purpose (career, startup, investing) with a 30/60/90-day plan |

Each phase ends with validation, a commit and a push.

## Contents

```text
industry-atlas/
├── SKILL.md                      # workflow and principles
├── references/                   # intake, conventions, structure, research playbook,
│                                 # industry adaptation, phase guides, maintenance
├── scripts/                      # copied into the atlas tools/ folder
│   ├── scaffold.py               # repo skeleton; monitoring templates
│   ├── validate_kb.py            # frontmatter, links, anchors, dates, secrets
│   ├── gen_company_cards.py      # company cards + master table from YAML
│   ├── gen_knowledge_map.py      # node cards, knowledge map, opportunity map from YAML
│   ├── build_opportunity_map.py  # rebuild the opportunity map after re-scoring
│   ├── new_weekly_report.py      # weekly report draft for any ISO week
│   ├── check_feeds.py            # verify RSS feeds, export OPML
│   └── atlas_common.py           # shared config, labels (translations), frontmatter
└── assets/
    ├── atlas.config.example.yaml
    ├── gitignore.template
    └── templates/
        ├── cards/                # company, segment, product, trend, regulation, keyword,
        │                         # content source, opportunity, person, teardown
        └── monitoring/           # weekly industry report, competitor and content monitoring
evals/evals.json                  # test prompts for iterating on the skill
```

## Security

The skill never handles tokens (GitHub access goes through `gh auth login`), creates repositories as private by default, and `validate_kb.py` scans every text file for leaked secrets before commits.

## License

MIT — see [LICENSE](LICENSE). Contributions and issues are welcome.
