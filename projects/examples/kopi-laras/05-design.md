# Design: Kopi Laras (Fictional)

Covers the Stitch work, reviews, and handoff summary. Process: [stitch-workflow.md](../../../design/google-stitch/workflows/stitch-workflow.md).

## UI requirement table (Stitch step 2)

| Business requirement | UI requirement | Screen |
|---|---|---|
| Buyers must see continuity of supply | Stock status and roast date on every origin entry | Home, Origin detail |
| Buyers ask MOQ and invoicing first | Terms table above the inquiry form | Wholesale |
| Inquiries must be qualified | Form requires cafe name, city, monthly volume | Wholesale |

## Stitch prompt used (W-05 adapted, desktop home)

```
CONTEXT
Store: Kopi Laras, a coffee roaster in Malang, Indonesia, selling 1kg wholesale bags to cafe owners in East Java.
Buyer's main decision factor: stock continuity and roast date.
Visual concept: A roaster's working ledger. Each origin reads like a dated, measured entry with clear status.

SCREEN
Responsive home page, 1280px. Sections in order:
1. Line: "Coffee you can plan your menu around." with a link "See wholesale terms".
2. Origin ledger: a table with 3 rows. Columns: Origin, Farm group, Tasting notes, Roast date, Stock (kg), Status.
   Rows: "Arjuno Natural | Sumber Wangi group | jackfruit, cacao | 2 Oct | 18 | Low stock",
   "Dampit Robusta | Tirto group | dark chocolate, clove | 30 Sep | 64 | In stock",
   "Bromo Honey | Lereng group | brown sugar, orange | 1 Oct | 40 | In stock"
3. Short farm section: 3 farm names with one moderate-size photo each, labeled "PHOTO: farm terraces".
4. Wholesale terms summary: MOQ 5kg, delivery East Java 2-4 working days, business invoice available.
5. Inquiry call to action.

CONSTRAINTS
Typography: Fraunces for headings, Source Sans 3 for body, IBM Plex Mono for dates and numbers.
Color: #1d1b19 ink, #f6f1ea background, #a4522e only for links and buttons, #3f5a3c "In stock" text, #8a5a00 "Low stock" text with a text label.
Layout: left-aligned 12-column grid, thin rules between rows, no cards, no full-bleed hero.
Avoid: gradients, glass effects, floating shapes, emoji, testimonials, logos of partners, statistics.

EXPECTED OUTPUT
One page. Status shown as text plus color. Visible focus styles.
```

All names and figures in the prompt are fictional sample content.

## Iteration log

| Output | Review result | Next prompt |
|---|---|---|
| D1-home-v1 | A4 Fail: farm photos dominated; C2 Fail: H1 too close to H2 | I-01 then I-03 |
| D1-home-v2 | Pass A1-A9 | I-06 for 390px |
| D1-home-mobile-v1 | Table overflowed at 390px | I-06 with "convert table to stacked rows with label-value pairs" |
| D1-home-mobile-v2 | Pass | I-09 to generate Wholesale page |
| D1-wholesale-v1 | Missing error and success states | I-10 |

## Anti-slop audit (Wholesale page, final)

Reviewer: second designer | Date: 2026-09-08
Fails: none. Justified: B2 (no card grid used). D4: sample stock figures marked "SAMPLE" in design files until the client supplies live data.

## Handoff summary

Full kit followed [handoff-kit.md](../../../design/google-stitch/handoff/handoff-kit.md). Key entries:

| Token | Value | Code name |
|---|---|---|
| color.ink | #1d1b19 | `--color-ink` |
| color.paper | #f6f1ea | `--color-surface` |
| color.action | #a4522e | `--color-action` |
| color.status-ok | #3f5a3c | `--color-success` |
| color.status-low | #8a5a00 | `--color-warning` |

Contrast ratios for these pairs were measured with a contrast checker during design review and recorded in the client's design file. Re-measure if any value changes.

| Component | Decision | Reason |
|---|---|---|
| Origin ledger table | Create | Expresses the concept; responsive stacked rows on mobile |
| Status label | Compose (text + color token) | Meaning must not rely on color |
| Inquiry form | Reuse studio form pattern | Standard fields and states |

Export path: Figma export for refinement, then rebuilt by hand in Astro. Stitch code used as reference only.
