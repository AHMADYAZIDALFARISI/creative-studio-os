# Projects

**Purpose:** One workspace per client project, with the same structure every time.

**Privacy:** Real client work must live in a **private** fork or repository. This public process repo contains only `_template/` and the fictional example.

## Start a new project

```bash
python3 scripts/new_project.py <client-slug> --client "Client Display Name"
```

What it does:
1. Validates the slug (lowercase letters, numbers, hyphens).
2. Refuses to run if `projects/<client-slug>/` already exists. Nothing is overwritten.
3. Copies `projects/_template/README.md` and fills the client name and date.
4. Copies the stage templates from `templates/` into numbered files.

Preview without writing anything:

```bash
python3 scripts/new_project.py <client-slug> --client "Name" --dry-run
```

## Resulting structure

```
projects/<client-slug>/
├── README.md                    status, links, decision log
├── 01-project-brief.md
├── 02-discovery.md
├── 03-brand-strategy.md
├── 04-creative-brief.md
├── 05-design-review.md          plus the Stitch handoff kit you copy in during design
├── 06-technical-specification.md
├── 07-test-plan.md
├── 08-deployment-checklist.md
├── 09-handover.md
├── 10-retrospective.md
└── stitch/                      prompts used and output links (create when design starts)
```

Delete files that a project does not need (for example `03-brand-strategy.md` for a build-only job) and note the reason in the README decision log.

## Worked example

[examples/kopi-laras/](examples/kopi-laras/README.md) shows one fictional project through every stage. Copy its process, not its visual direction.
