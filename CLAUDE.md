# Creative Studio OS: Claude Code Instructions

This repository is a studio operating system: Markdown guides, templates, and small Python scripts. It is not an application. Client work lives in `projects/<slug>/` (private copies only).

## Before editing
1. Read the files you will change and the guide they link to. Domain map: `docs/repository-architecture.md`.
2. For changes touching more than two files, state a short plan listing the files first.
3. Follow existing structure: every guide answers purpose, when to use, inputs, steps, output, quality check, common mistakes, next step.

## Writing rules
- Active voice, short sentences, no em dashes.
- Placeholders use `{{UPPER_SNAKE_CASE}}`.
- Never invent statistics, testimonials, client logos, research, or tool capabilities. Label fictional content as fictional.
- Tool claims (Google Stitch, Claude Code) must match `design/google-stitch/capabilities.md` or official docs. Mark anything unconfirmed as "Reported" or "Unknown".

## Commands
```bash
python3 scripts/validation/validate_repo.py --public        # add --public in the public repo; omit in private studio copies
python3 -m unittest discover -s scripts -p "test_*.py"      # script tests
python3 scripts/new_project.py <slug> --client "Name" --dry-run
```
Run both checks after any change. Report the actual output. If a check did not run, say so.

## Safety
- Never write secrets, credentials, or personal data into any file.
- Do not delete or overwrite files without understanding their purpose. Prefer edits over rewrites.
- Do not add dependencies. Scripts use the Python standard library only.

## When working on a client project folder
- Use the evidence labels [Client], [Verified], [Hypothesis], [Recommendation].
- Run the anti-slop audit (`/anti-slop-audit`) on design deliverables.
- Write Stitch prompts with `/stitch-prompt`, only after `04-creative-brief.md` has an approved direction.

## Reviewers available
Subagents in `.claude/agents/`: `creative-director`, `ux-accessibility-reviewer`, `security-code-reviewer`, `client-delivery-reviewer`. They review and report; they do not edit files. If subagents are unavailable, apply the same checklists in sequence.

## Finishing a task
Summarize: files changed, checks run with results, anything incomplete or unverified.
