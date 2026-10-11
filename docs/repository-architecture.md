# Repository Architecture

**Purpose:** Explain why the repo looks the way it does, so changes stay consistent.

## Design decisions

| Decision | Reason |
|---|---|
| Group by domain, not by project stage | People search by discipline ("how do we do APIs?"). The stage view lives in [workflow-overview.md](workflow-overview.md). |
| One worked example instead of many | A single complete example teaches more than several shallow ones. |
| Root `CLAUDE.md`, with rules, skills, and agents under `.claude/` | Claude Code reads a root `CLAUDE.md`. One entry point avoids conflicting instructions. |
| Python standard library only for scripts | Runs on any studio laptop and in CI with no install step. |
| No generator framework | `scripts/new_project.py` copies one folder. A generator adds maintenance before there is a need. |
| Folders from the target architecture without content were not created | Empty folders imply coverage that does not exist. See the deferral list below. |

## Deferred directories

These appear in the original target architecture but have no content yet. Create them when a real need appears.

- `ai/documentation/`: documentation prompts live in [ai/prompt-engineering/lifecycle-prompts.md](../ai/prompt-engineering/lifecycle-prompts.md).
- `ai/code-review/`: code review prompts live in the lifecycle prompts and [engineering/code-review/](../engineering/code-review/review-checklist.md).
- `assets/`: the studio's own logo and brand files belong here once they exist. Client assets stay in the client drive.
- `client-operations/retrospective/`: retrospectives use [templates/retrospective.md](../templates/retrospective.md).
- `.claude/` agents for frontend and backend engineering: the main Claude Code session does implementation. Subagents are limited to four reviewers to keep instructions small. QA and accessibility share one reviewer.
- `studio/references/` holds only the evaluation method. Store actual reference images in the project folder.

## Requirement map

| Requirement | Where it lives |
|---|---|
| Anti-slop standard | [studio/creative-direction/anti-slop-audit.md](../studio/creative-direction/anti-slop-audit.md) |
| Google Stitch toolkit | [design/google-stitch/](../design/google-stitch/README.md) |
| Discovery and strategy | [studio/discovery/](../studio/discovery/discovery-process.md), [studio/strategy/](../studio/strategy/positioning.md) |
| Brand identity | [studio/brand-identity/brand-system.md](../studio/brand-identity/brand-system.md) |
| UI/UX method | [design/ui-ux/](../design/ui-ux/ux-method.md) |
| Frontend and backend | [engineering/](../engineering/architecture/stack-selection.md) |
| Prompt engineering | [ai/](../ai/prompt-engineering/prompt-framework.md) |
| Claude Code | [CLAUDE.md](../CLAUDE.md), [.claude/agents/](../.claude/agents/), [.claude/skills/](../.claude/skills/), [.claude/rules/](../.claude/rules/) |
| Client operations, EN and ID | [client-operations/](../client-operations/README.md) |
| Worked example | [projects/examples/kopi-laras/](../projects/examples/kopi-laras/README.md) |
| Validation | [scripts/](../scripts/README.md) |

## Known limitations

- Google Stitch has no verified public API documented here. The toolkit uses a manual, prompt-driven workflow. See [capabilities.md](../design/google-stitch/capabilities.md).
- Claude Code configuration follows conventions checked on 2026-10-12 against secondary documentation summaries, not by running Claude Code. Verify that skills and agents load (`/agents`, `/anti-slop-audit`) on first use, and recheck the official docs (https://code.claude.com/docs) after major releases.
- Legal and commercial templates are not jurisdiction-specific legal advice.
- The validator checks structure and links. It does not judge writing quality.
