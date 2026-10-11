# Creative Studio OS

An open-source operating system template for multidisciplinary creative studios. It covers discovery, brand strategy, Google Stitch design exploration, UI/UX, engineering, AI prompting, and client operations for Indonesian and international clients.

Fork it, adapt it to your studio, and keep client work in a private copy.

This repository stores a **process**, not a visual style. Every client gets its own direction, architecture, and delivery plan.

## Start here

| You want to | Go to |
|---|---|
| Understand the repo in 10 minutes | [docs/getting-started.md](docs/getting-started.md) |
| See the end-to-end workflow | [docs/workflow-overview.md](docs/workflow-overview.md) |
| Start a new client project | [projects/README.md](projects/README.md) |
| Design with Google Stitch | [design/google-stitch/README.md](design/google-stitch/README.md) |
| Check work for generic AI output | [studio/creative-direction/anti-slop-audit.md](studio/creative-direction/anti-slop-audit.md) |
| Pick a tech stack | [engineering/architecture/stack-selection.md](engineering/architecture/stack-selection.md) |
| Send a proposal or SOW | [client-operations/README.md](client-operations/README.md) |
| See a full worked example | [projects/examples/kopi-laras/README.md](projects/examples/kopi-laras/README.md) |

## Domains

- `studio/`: discovery, research, positioning, brand identity, creative direction.
- `design/`: Google Stitch toolkit, UI/UX method, design systems, typography, color, layout, interaction, accessibility.
- `engineering/`: stack selection, frontend, backend, APIs, databases, security, performance, testing, deployment, code review.
- `ai/`: prompt framework, lifecycle prompts, coding-agent workflow, design critique, prompt evaluation.
- `client-operations/`: onboarding, questionnaires, proposals, SOW, planning, communication, change requests, QA, handover.
- `templates/`: copy-ready project documents.
- `projects/`: client workspaces and one fictional worked example.
- `scripts/`: validation and a safe project bootstrap.
- `.claude/` and `CLAUDE.md`: Claude Code instructions, rules, skills, and subagents.

## Validate the repository

```bash
python3 scripts/validation/validate_repo.py --public
python3 -m unittest discover -s scripts -p "test_*.py"
```

Requires Python 3.9+ and no third-party packages.

## Ringkasan (Bahasa Indonesia)

Template sistem operasional untuk studio kreatif: discovery, strategi merek, eksplorasi desain dengan Google Stitch, UI/UX, engineering, prompt AI, dan operasional klien. Dokumen untuk klien tersedia dalam bahasa Indonesia dan Inggris. Mulai dari [docs/getting-started.md](docs/getting-started.md). Simpan pekerjaan klien di repositori privat.

## Using this for client work

This public repository holds process and templates only. For real projects:

1. Create a **private** copy (GitHub "Use this template" or a private fork).
2. Run `python3 scripts/new_project.py <slug> --client "Name"` in the private copy.
3. Never open a pull request to this public repository from a branch that contains client folders.

## License and disclaimers

- Code and documentation: [MIT License](LICENSE).
- Commercial and legal templates are not legal advice. Have a qualified professional review contracts for your jurisdiction.
- Not affiliated with or endorsed by Google, Anthropic, Figma, or any other vendor named here. Product names are trademarks of their owners and appear only to describe compatibility.
- Tool capabilities change. Check [design/google-stitch/capabilities.md](design/google-stitch/capabilities.md) and official docs before relying on a feature.

## Contributing

Issues and pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Status

See [CHANGELOG.md](CHANGELOG.md). Known gaps are listed in [docs/repository-architecture.md](docs/repository-architecture.md#known-limitations).
