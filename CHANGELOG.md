# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Dates use ISO 8601.

## Unreleased

## 0.2.0 - 2026-10-12

### Added
- Public release: README framing, Indonesian summary, disclaimers, CODE_OF_CONDUCT.md.
- `validate_repo.py --public`: fails on client folders in `projects/` and on placeholders in LICENSE, SECURITY.md, CODE_OF_CONDUCT.md. CI uses it.

### Changed
- LICENSE copyright holder set. SECURITY.md uses GitHub private vulnerability reporting instead of an email placeholder.
- CONTRIBUTING.md rewritten for outside contributors.

## 0.1.1 - 2026-10-12

### Fixed (independent audit)
- 31 broken internal links and 6 empty directories: added the missing client-operations documents, 12 templates, project workspace, worked example, scripts, and Claude Code configuration that 0.1.0 documents referenced.
- CHANGELOG 0.1.0 listed items that did not yet exist. All listed items now exist and are checked by the validator.
- `new_project.py`: links in copied templates now resolve from the project folder, and links between copied templates point to the numbered copies.
- Fictional example contained an unfilled `{{date}}` placeholder.
- Google Stitch capability table now cites sources with access dates; the workflow no longer calls reported features "confirmed".
- Evidence labels unified to [Client], [Verified], [Hypothesis], [Recommendation].
- REST guide: fixed 400 vs 422 ambiguity and the IDR currency-unit statement.
- Interview guide: added a language-support question.

### Changed
- Claude Code subagents reduced from seven proposed roles to four reviewers. Rationale in docs/repository-architecture.md.

## 0.1.0 - 2026-10-12

### Added
- Core docs: getting started, architecture, workflow, glossary, quality standards.
- Studio toolkit: discovery, research, positioning, brand system, creative direction, anti-slop audit.
- Google Stitch toolkit: workflow, capability notes, prompt library, iteration prompts, handoff kit, QA.
- Design guidance: UX method, states and forms, tokens, component decisions, typography, color, layout, motion, accessibility.
- Engineering handbook: stack selection, frontend, backend, API, database, security, performance, testing, deployment, code review.
- AI toolkit: prompt framework, lifecycle prompts, evaluation rubric, coding-agent workflow, design critique.
- Client operations in English and Indonesian.
- Twelve project templates and a project workspace template.
- Fictional worked example: Kopi Laras.
- Validation script, bootstrap script, unit tests, CI workflow.
- Claude Code configuration: CLAUDE.md, rules, skills, subagents.
