# Workflow Overview

**Purpose:** Show how every toolkit connects across a project.
**Use when:** Planning a project, onboarding a teammate, or checking what comes next.

## Stages, gates, and documents

| # | Stage | Main output | Gate to pass | Guides |
|---|---|---|---|---|
| 1 | Inquiry and onboarding | Intake record, NDA if needed | Fit confirmed, budget range known | [onboarding](../client-operations/onboarding/onboarding-checklist.md) |
| 2 | Discovery | Discovery summary with labeled evidence | Client confirms facts and goals | [discovery process](../studio/discovery/discovery-process.md) |
| 3 | Proposal and scope | Proposal, SOW, timeline | Signed scope and acceptance criteria | [proposals](../client-operations/proposals/proposal-en.md), [SOW](../client-operations/scope-of-work/sow-template.md) |
| 4 | Strategy and creative direction | Positioning, creative brief, direction rationale | Client approves one direction | [positioning](../studio/strategy/positioning.md), [creative direction](../studio/creative-direction/creative-direction-method.md) |
| 5 | Design | Stitch explorations, refined screens, handoff kit | Design review and anti-slop audit pass | [Stitch workflow](../design/google-stitch/workflows/stitch-workflow.md), [UX method](../design/ui-ux/ux-method.md) |
| 6 | Engineering | Tech spec, implementation, tests | Code review, test plan executed | [stack selection](../engineering/architecture/stack-selection.md), [frontend](../engineering/frontend/frontend-handbook.md), [backend](../engineering/backend/backend-handbook.md) |
| 7 | QA and launch | QA report, deployment checklist | Acceptance criteria met, rollback ready | [testing](../engineering/testing/testing-strategy.md), [deployment](../engineering/deployment/deployment-rollback.md) |
| 8 | Handover and retrospective | Handover pack, retro notes | Client sign-off | [handover](../client-operations/handover/handover-and-maintenance.md), [retro](../templates/retrospective.md) |

## Rules that hold across stages

- Label every claim as **[Client]**, **[Verified]**, **[Hypothesis]**, or **[Recommendation]**. See [evidence labels](../studio/discovery/discovery-process.md#evidence-labels).
- Do not skip a gate to save time. A skipped gate becomes a change request later.
- Record decisions with a one-line rationale in the project README decision log.
- Treat AI output as a draft that a named person reviews.

## Typical durations (planning defaults, adjust per project)

| Project type | Discovery | Design | Build | QA and launch |
|---|---|---|---|---|
| Landing page | 2-3 days | 3-5 days | 3-5 days | 2 days |
| Corporate site, 6-12 pages | 1 week | 2 weeks | 2-3 weeks | 1 week |
| Web app MVP | 1-2 weeks | 3-4 weeks | 6-10 weeks | 2 weeks |

These are internal planning defaults, not market benchmarks.

**Next:** [../projects/README.md](../projects/README.md)
