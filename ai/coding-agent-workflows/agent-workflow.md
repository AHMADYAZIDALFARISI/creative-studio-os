# Coding Agent Workflow

**Purpose:** Get reliable results from Claude Code and similar coding agents on studio projects.

## Before the session

1. Make sure the project has a `CLAUDE.md` with stack, commands, and conventions. Start from this repo's [CLAUDE.md](../../CLAUDE.md).
2. Attach or point to the spec, handoff kit, and API contract.
3. Work on a branch.

## Session loop

1. **Read.** Ask the agent to read relevant files and summarize conventions before editing.
2. **Plan.** For multi-file changes, ask for a plan with the files it will touch. Approve or correct.
3. **Implement in small steps.** One feature or fix per step.
4. **Verify.** Agent runs type check, lint, tests, and build, and reports actual output.
5. **Review the diff yourself.** The human reviewer owns the merge.
6. **Document.** Update README, `.env.example`, and changelog when behavior changes.

## Use subagents when they help

This repo defines subagents in [.claude/agents/](../../.claude/agents/). Delegate focused reviews (UI/UX, accessibility, security) to keep the main context clean. If subagents are unavailable in your setup, run the same checklists in sequence.

## Rules

- No secrets in prompts or files. Use `.env.example` with names only.
- The agent must report incomplete work and checks that did not run.
- Reject changes that add dependencies without a stated reason.
- Do not let an agent run destructive commands (dropping databases, force pushes, deleting folders) without explicit human approval.
