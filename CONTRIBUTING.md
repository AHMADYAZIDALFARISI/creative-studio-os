# Contributing

Thank you for helping improve Creative Studio OS. Everyone who participates follows the [Code of Conduct](CODE_OF_CONDUCT.md).

## What we welcome

- Fixes for errors, broken links, outdated tool information, and unclear wording.
- Improvements to workflows, templates, and prompts backed by real project experience (no client names or data).
- Translations or improvements of the Indonesian and English client documents.

For larger changes, open an issue first so we can agree on the direction before you write.

## Review

- The maintainer reviews every pull request.
- Changes to workflows, quality gates, client-facing templates, or `.claude/` need a short reason in the pull request description.
- Tool capability updates (Google Stitch, Claude Code) need a source link and access date.

## Rules

1. Edit existing documents before adding new ones. A new file needs a clear purpose that no current file serves.
2. Every important document answers: purpose, when to use, inputs, steps, output, quality check, common mistakes, next step.
3. Write in active voice. Use short sentences. Do not use em dashes.
4. Never add fabricated statistics, testimonials, client logos, or awards. Label fictional material as fictional.
5. Never commit secrets, client credentials, signed contracts, personal data, or client folders. Real client work lives in private repositories.
6. Templates use `{{UPPER_SNAKE_CASE}}` placeholders. Do not leave `TODO` or `TBD` in finished guidance documents.
7. Run the validator before opening a pull request.

## Workflow

```bash
# fork the repository, then:
git checkout -b docs/short-description
# edit
python3 scripts/validation/validate_repo.py --public
python3 -m unittest discover -s scripts -p "test_*.py"
git commit -m "docs: short description"
```

Commit prefixes: `docs`, `template`, `design`, `eng`, `ai`, `ops`, `scripts`, `fix`.

Add a line to `CHANGELOG.md` under `Unreleased` for any change that alters a workflow or template.
