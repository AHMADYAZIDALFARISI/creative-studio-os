# Design Handoff Kit

**Purpose:** Give developers everything needed to build the approved design without guessing.
**Use when:** After design approval and before the technical specification is final.
**Output:** Copy this file into `projects/<client>/05-design-handoff.md` and fill it.

## 1. Screen inventory

| ID | Screen | Journey | Breakpoints designed | Source link | Status |
|---|---|---|---|---|---|
| S-01 | {{SCREEN}} | {{JOURNEY}} | 360 / 768 / 1280 | {{FIGMA_OR_STITCH_LINK}} | Approved {{YYYY-MM-DD}} |

## 2. Component inventory

| Component | Variants | States | Reuse decision | Notes |
|---|---|---|---|---|
| Button | primary, secondary, ghost | default, hover, focus, active, disabled, loading | Reuse from project library | Loading keeps width |

Reuse decision values: **Reuse**, **Compose**, **Customize**, **Create new**. See [component decisions](../../design-systems/component-decisions.md).

## 3. Design token mapping

| Token | Value | Used for | Code name |
|---|---|---|---|
| color.ink | {{HEX}} | body text | `--color-ink` |
| color.surface | {{HEX}} | page background | `--color-surface` |
| space.4 | 16px | default gap | `--space-4` |
| font.heading | {{FAMILY}}, fallback {{STACK}} | H1-H3 | `--font-heading` |

## 4. Responsive behavior

| Element | 360px | 768px | 1280px |
|---|---|---|---|
| Main nav | Menu button, full-screen sheet | Menu button | Inline links |

## 5. Interaction specification

| Trigger | Element | Behavior | Duration and easing | Reduced motion |
|---|---|---|---|---|
| Click | Add to cart | Button shows loading, then count updates in cart icon | 150-250ms, ease-out | No animation, instant update |

## 6. Asset inventory

| Asset | Format | Sizes | Source and license | Alt text |
|---|---|---|---|---|
| Hero photo | AVIF + JPG fallback | 640, 1280, 1920 | Client shoot, {{DATE}} | {{ALT}} |

## 7. Missing-state checklist

For each interactive screen confirm: [ ] loading [ ] empty [ ] error [ ] success [ ] disabled [ ] partial data [ ] long text [ ] permission denied (if auth).

## 8. Developer implementation notes

- Exported Stitch code is reference only. Rebuild with semantic HTML.
- Placeholder content that must not ship: {{LIST}}.
- Open questions with owners: {{LIST}}.

## 9. Visual QA checklist

Use [stitch-output-review.md](../qa/stitch-output-review.md) Part B after implementation.
