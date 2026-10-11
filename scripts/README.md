# Scripts

Python 3.9+ standard library only. No install step.

## validation/validate_repo.py

Checks the repository and exits with code 1 if any problem is found.

```bash
python3 scripts/validation/validate_repo.py
python3 scripts/validation/validate_repo.py --public   # public repo: also blocks client folders and legal placeholders
python3 scripts/validation/validate_repo.py --root /path/to/private-copy
```

| Check | What it catches |
|---|---|
| required files | Core docs, templates, and scripts that the README promises |
| internal links | Relative Markdown links to files that do not exist (code blocks and `{{PLACEHOLDER}}` links skipped) |
| empty directories | Folders that imply coverage with no content |
| unfinished markers | `TODO`, `TBD`, `FIXME`, `lorem ipsum` outside code blocks |
| fictional example | Missing FICTIONAL label or unfilled placeholders in `projects/examples/` |
| prompt duplicates | Reused prompt IDs and identical prompt bodies in `ai/` and `design/google-stitch/` |
| em dashes | Violations of the writing rule |
| Claude Code frontmatter | Agents and skills missing `name` or `description`, or names that do not match file or folder |
| secret patterns | Private keys, common API token formats, hard-coded secret assignments |
| public release (`--public` only) | Any folder in `projects/` other than `_template/` and `examples/`; placeholders in LICENSE, SECURITY.md, CODE_OF_CONDUCT.md |

Limits: it does not judge writing quality, check external URLs, or replace a dedicated secret scanner. Enable your Git host's secret scanning as well.

## new_project.py

Creates `projects/<slug>/` from `projects/_template/` and `templates/`. See [projects/README.md](../projects/README.md).

```bash
python3 scripts/new_project.py acme-coffee --client "Acme Coffee" --dry-run
python3 scripts/new_project.py acme-coffee --client "Acme Coffee"
```

Safety: refuses to touch an existing folder, rejects invalid slugs, writes nothing in `--dry-run`. It rewrites relative links in copied templates so they resolve from the new folder.

## Tests

```bash
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

CI runs both the tests and the validator: `.github/workflows/validate.yml`.
