# Stitch Output Review and Visual QA

**Purpose:** Part A reviews Stitch output before we keep it. Part B checks the built interface against the approved design.

## Part A: Generated output review

| # | Check | Pass / Fail / Note |
|---|---|---|
| A1 | Matches the UI requirement table for this screen | |
| A2 | Uses only tokens from the creative brief (colors, fonts, radius) | |
| A3 | Content is ours or clearly marked placeholder; nothing invented as fact | |
| A4 | Hierarchy: primary element identified in 5 seconds | |
| A5 | Text contrast plausibly meets 4.5:1 (verify with a checker after export) | |
| A6 | Interactive elements look interactive; focus state exists | |
| A7 | States requested were produced | |
| A8 | Mobile layout keeps task order | |
| A9 | Passes the anti-slop audit sections B, C, D | |

Decision: **Keep**, **Iterate** (name the iteration prompt), or **Discard**.

## Part B: Implementation vs design

Check at 360px, 768px, 1280px in at least two browsers.

| # | Check | Result |
|---|---|---|
| B1 | Spacing and alignment match within 4px | |
| B2 | Font families, sizes, weights, line heights match tokens | |
| B3 | Colors use tokens, not hard-coded near-matches | |
| B4 | All states implemented and reachable | |
| B5 | Keyboard: every action reachable, focus order logical, focus visible | |
| B6 | Images use correct sizes and alt text | |
| B7 | Motion matches spec and respects reduced motion | |
| B8 | Long text, empty data, and error data do not break layout | |

Log each difference as **Bug** (fix) or **Accepted deviation** (with reason and approver).
