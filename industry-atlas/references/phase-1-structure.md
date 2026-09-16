# Phase 1 — Structure and taxonomy

**Goal:** a repository skeleton that already reads as a coherent guide: conventions, an industry taxonomy, localized folder READMEs and templates, pushed to a private GitHub repo.

## Steps

1. **Config and scaffold.** Write `atlas.config.yaml` (intake), run `scaffold.py init`.
2. **Research the industry map** (one batch of searches): the industry's standard segmentations by analysts, investors and industry bodies; the largest companies per segment; how money flows through the value chain.
3. **Decide segments** (8–14) and add them to `segments:` in the config (`key` = segment tag, `name`, `folder`, `overview` = `<Name>-Overview.md`). Rerun `scaffold.py init` to create the segment folders (existing files are not overwritten).
4. **Write `00-Overview/Conventions.md`** from `references/conventions.md`: real industry tag, segment and sub-segment tags, monetization tags, examples from this industry, any adaptations (regions, regulation naming).
5. **Write `00-Overview/Industry-Taxonomy.md`** (type `map`):
   1. What the industry is: definition, boundaries, what is out of scope.
   2. Classification axes (4–6), each as a table.
   3. Segment tree: Mermaid flowchart + nested list with sub-segments.
   4. Summary table of segments: definition, customer type, maturity, regulatory load, example companies (names as text until cards exist).
   5. Stack or value-chain layers.
   6. Intersections between segments.
   7. The taxonomy through the user's purpose lens: for career, typical product problems, north-star metrics and interview questions per segment; for founders, entry barriers and wedges; for investors, where value accrues.
   8. Edge cases: how to classify hybrid companies.
6. **Rewrite every folder README** in the content language using the pattern in `structure.md`, with the planned files as `code` names and ⚪ status.
7. **Translate `99-Templates`** into the content language (headings, hints) and write `99-Templates/README.md` listing them. Keep frontmatter keys, tag values and `{{placeholders}}`.
8. **Fill `labels:`** in the config when the content language is not English, so generated cards match.
9. **Root README**: purpose, reading routes, structure table, roadmap, changelog (pattern in `structure.md`).
10. **Validate**, then create the repo and push:

```bash
python3 tools/validate_kb.py
git init -b main
git add -A
git commit -m "structure: phase 1 — structure, conventions, taxonomy, templates"
gh repo create <owner>/<repo> --private --source . --push
gh repo view <owner>/<repo> --json visibility -q .visibility   # expect PRIVATE
```

## Quality bar

- Every segment in the taxonomy has a folder, a tag and a config entry.
- No links to unwritten files; no English stubs left in a non-English atlas.
- Validator clean.

## Checkpoint message

Show the segment tree, the adaptation decisions (regions, regulation naming, depth) and the repo URL. Ask whether to continue with Phase 2A, unless running autonomously.
