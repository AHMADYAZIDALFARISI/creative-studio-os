# Quality Standards

**Purpose:** Define the minimum bar for any deliverable leaving the studio.
**Use when:** Before every client review, launch, and handover.

## Universal bar

1. **Traceable:** every major design or technical decision links to a goal, user need, or constraint.
2. **Honest:** no invented metrics, testimonials, logos, or research. Fictional content carries a label.
3. **Accessible:** WCAG 2.2 AA is the default target. See [accessibility checklist](../design/accessibility/accessibility-checklist.md).
4. **Complete states:** loading, empty, error, success, and disabled states exist for every interactive surface.
5. **Verified:** tests, checks, and builds were actually run. Reports state what ran and what did not.
6. **Original:** passes the [anti-slop audit](../studio/creative-direction/anti-slop-audit.md).

## Documents

A document is complete when it answers: what it is for, when to use it, required inputs, steps, expected output, quality check, common mistakes, and where to go next.

## Design

- Typography, color, and layout choices each have a one-line rationale.
- Responsive behavior is specified at a minimum of 360px, 768px, and 1280px widths.
- Contrast meets 4.5:1 for body text and 3:1 for large text and UI boundaries.

## Engineering

- No secrets in code, docs, or history.
- Production build passes locally and in CI.
- Lighthouse or equivalent checks run on key pages. Targets live in [performance budget](../engineering/performance/performance-budget.md).
- Every auth, payment, or personal-data feature gets a security review against the [security baseline](../engineering/authentication-security/security-baseline.md).

## Reporting

Status reports separate **done**, **in progress**, **blocked**, and **not started**. A blocked item names the blocker and the owner.
