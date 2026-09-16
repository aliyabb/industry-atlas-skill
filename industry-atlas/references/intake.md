# Intake

The goal of intake is a short, confirmed plan and an `atlas.config.yaml`. Extract answers from the conversation first; ask only for what is missing, in one message, offering defaults so the user can simply say "yes".

## Questions and defaults

| Topic | Question | Default |
|---|---|---|
| Industry and boundaries | Which industry, and what is in or out of scope? | Ask; propose boundaries yourself (for example "AI agents: platforms, tooling, evaluation, vertical agents; not general ML infrastructure") |
| Purpose | What is the atlas for? | `career` if the user mentions jobs; else `learning` |
| Background | Education, experience, target role or thesis | Ask if the purpose is career, founder or investor |
| Regions | Which regions matter most? | `[global, us, eu, uk, asia]` |
| Content language | Language of prose and headings | The language the user writes in |
| GitHub | Owner, repo name, visibility | Owner from `gh api user`; repo `<industry>-atlas`; **private** |
| Depth | How big? | `standard`: 100–200 companies, 10–20 teardowns, 100+ sources |
| Autonomy | Pause after each phase or run through? | Pause after each phase |

Depth presets:

| Preset | Segments | Companies | Teardowns | Content sources | Nodes | Typical use |
|---|---|---|---|---|---|---|
| `lite` | 6–8 | 40–60 | 5–8 | 40+ | 20–30 | Quick orientation |
| `standard` | 8–14 | 100–200 | 10–20 | 100+ | 40–60 | Job search, market entry |
| `deep` | 12–18 | 200–300 | 20–30 | 150+ | 60–90 | Investment thesis, consulting |

## Prerequisites to check

```bash
git --version
gh auth status          # if not logged in, ask the user to run `gh auth login` themselves
python3 -c "import yaml; print('pyyaml ok')"   # otherwise: pip install pyyaml
```

Web search and web fetch tools are needed for research. Without them, say so plainly: the atlas would be built from memory, every number would need the verification marker, and the value drops sharply.

## Confirm before publishing

Creating a GitHub repository publishes to the user's account, so confirm once, in one message, before `gh repo create`:

> Plan: **AI Agents Atlas**, content in English, purpose: career (target: product manager), regions global/US/EU/UK/Asia, standard depth, private repo `your-account/ai-agents-atlas`, pausing after each phase. OK?

## atlas.config.yaml

Start from `assets/atlas.config.example.yaml`. Fields:

| Key | Meaning |
|---|---|
| `industry`, `atlas_title` | Display names |
| `industry_tag` | First tag of every file; lowercase, no spaces (`aiagents`) |
| `content_language` | ISO code of the prose language |
| `purpose` | `career`, `founder`, `investor`, `consultant` or `learning`; decides the Phase 7 folder name |
| `profile` | Free text about the user, used in Phases 1 and 7 |
| `regions` | Focus regions used as defaults in generated files |
| `region_values` | Allowed `region` values for the validator |
| `as_of` | Snapshot date written into `updated` during the initial build (today) |
| `owner`, `repo`, `visibility` | GitHub target |
| `verification_marker` | Marker text shown in generated sentences |
| `segments` | Filled in Phase 1: `key`, `name`, `folder`, `overview` file name |
| `company_groups` | Optional grouping for the master table (defaults: regions + failures) |
| `mixed_script_check`, `mixed_script_allow` | Turn on for Cyrillic atlases to catch words mixing Latin and Cyrillic letters |
| `labels` | Translations of generated headings (see `scripts/atlas_common.py` `DEFAULT_LABELS`); fill in Phase 1 when the content language is not English |
