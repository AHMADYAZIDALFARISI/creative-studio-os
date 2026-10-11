# Color Guide

**Purpose:** Build a palette with roles, tested contrast, and a business reason.

## Steps

1. Derive the core color from the brand strategy or existing equity. Write the reason.
2. Build a tonal scale (for example 50-900) for core and neutral colors.
3. Assign semantic roles (see [design tokens](../design-systems/design-tokens.md)).
4. Test every text-on-background pair. Record ratios in a table.
5. Define status colors that work for color-vision deficiencies. Pair color with icon or text.
6. If dark mode is in scope, map roles, do not invert values.

## Contrast table format

| Text | Background | Ratio | Allowed use |
|---|---|---|---|
| ink #1d1b19 | surface #f6f1ea | {{RATIO}} | All text |
| action #a4522e | surface #f6f1ea | {{RATIO}} | Large text and buttons only if below 4.5:1 |

Measure ratios with a contrast checker. Do not estimate.

## Proportion

Write a rough proportion: for example 70% surface, 20% ink, 8% secondary, 2% action. Action color stays rare so it signals interactivity.

## Common mistakes

- Using the accent for both links and decoration, so users cannot tell what is clickable.
- Gradients added for "depth" with no brand reason.
