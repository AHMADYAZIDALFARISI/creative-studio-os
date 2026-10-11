# Test Plan: Kopi Laras (Fictional)

**Environment:** staging preview | **Tester:** studio QA | **Dates:** 2026-10-06 to 2026-10-09

All results below are illustrative.

| ID | Journey or feature | Expected | Type | Result | Notes |
|---|---|---|---|---|---|
| T-01 | Submit wholesale inquiry with valid data | Success message; email received | Functional | Pass | |
| T-02 | Submit with missing cafe name | Inline error linked to field; data kept | Functional, A11y | Fail, then Pass | Error was not announced; added `aria-describedby` |
| T-03 | Stock status shows text, not only color | "Low stock" text visible | A11y | Pass | |
| T-04 | Origin ledger at 360px | Stacked rows, no horizontal scroll | Responsive | Pass | |
| T-05 | Keyboard through home and wholesale | All actions reachable; focus visible | A11y | Pass | |
| T-06 | Screen reader on wholesale form (NVDA + Firefox) | Labels and errors announced | A11y | Pass | |
| T-07 | Lighthouse mobile, home, 3 runs median | LCP within budget | Performance | Pass | Measured values recorded in QA sheet |
| T-08 | Language switch ID to EN | Same page in EN, `hreflang` present | Functional | Pass | |
| T-09 | iOS Safari form autofill | Phone field accepts +62 format | Functional | Not run | Device unavailable; ran on simulator only; flagged to client |

Exit decision: no open Critical or High defects; T-09 documented as not run.
