# Testing Strategy

**Purpose:** Test what matters for each project size.

## Levels

| Level | What | When required |
|---|---|---|
| Static | Type check, lint, format | All code projects |
| Unit | Pure logic: pricing, validation, formatting | Any non-trivial logic |
| Integration | API endpoints with database, external service adapters | Any backend |
| End-to-end | Priority journeys in a real browser | Apps and stores; one smoke test for marketing sites |
| Accessibility | Automated scan + manual keyboard and screen reader | All projects |
| Visual QA | Implementation vs design | All projects with design handoff |
| Cross-browser and device | Latest Chrome, Safari, Firefox, Edge; iOS Safari; Android Chrome | All projects |

## Rules

- Write the [test plan](../../templates/test-plan.md) before QA starts.
- Every bug fix adds a test when the bug was in logic.
- Report what ran, what passed, what failed, and what did not run.

## Bug severity

| Severity | Definition | Launch impact |
|---|---|---|
| Critical | Data loss, security issue, payment failure, site down | Blocks launch |
| High | Priority journey broken for a user group | Blocks launch |
| Medium | Workaround exists | Fix or schedule with client agreement |
| Low | Cosmetic | Schedule |
