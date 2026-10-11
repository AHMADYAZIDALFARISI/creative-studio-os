# Code Review Checklist

**Use when:** Every pull request. Reviewers comment with a severity prefix: `blocker:`, `should:`, `nit:`.

## Correctness
- [ ] Does what the ticket or spec says. Edge cases handled: empty, null, long, duplicate, concurrent.
- [ ] Errors handled and surfaced to users with a next step.

## Security
- [ ] No secrets. Input validated. Authorization checked server-side.

## Accessibility
- [ ] Semantic elements, labels, keyboard access, focus management.

## Performance
- [ ] No unnecessary re-renders or N+1 queries. Images sized. No new heavy dependency without reason.

## Maintainability
- [ ] Follows existing conventions. Names explain intent. No dead code. Abstractions earn their place.

## Tests
- [ ] New logic has tests. Tests fail without the change.

## Docs
- [ ] README, env example, and API docs updated when behavior changes.

## Review the diff, not the description
Run the branch when the change affects UI or a journey.
