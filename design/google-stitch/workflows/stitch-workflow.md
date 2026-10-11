# Stitch Workflow: Brief to Validated Implementation

**Purpose:** A repeatable 12-step process for using Stitch on client work.
**Inputs:** Approved creative brief, sitemap, content inventory, priority user journeys.
**Output:** Approved screens, handoff kit, and a visual QA record.

## Step 1. Prepare the Stitch brief

Condense the creative brief into a one-page Stitch brief. Stitch responds to specifics. Include:

- Product type and platform (responsive web, mobile-first web, desktop dashboard).
- Audience and the one task this screen supports.
- Visual concept in two sentences.
- Typography: named families or a precise description ("high-contrast serif for headings, neutral grotesk for body").
- Color: hex values with roles.
- Density and layout rule.
- Explicit avoid list from the anti-slop audit.
- Real content, or clearly marked placeholder content.

## Step 2. Translate business requirements into UI requirements

| Business requirement | UI requirement | Screen |
|---|---|---|
| Wholesale buyers need a quote in one visit | Quote form reachable from every product page; shows MOQ and lead time | Product detail, Quote form |

Write this table before prompting. It becomes the review checklist.

## Step 3. Define journeys to cover

Pick one to three priority journeys. List screens per journey. Stitch work follows journeys, not pages in isolation.

## Step 4. Create initial screens

Start with the screen that carries the most decisions, usually the home or main dashboard view. Use a prompt from the [prompt library](../prompt-library/websites.md).

## Step 5. Explore directions

Run the same screen prompt with each direction's constraints from the creative brief. Keep content identical so the comparison is fair. Save each output with a name: `D1-home-v1`, `D2-home-v1`.

## Step 6. Refine hierarchy, type, spacing, composition, interactions

Use [iteration prompts](../iteration-prompts/iteration-prompts.md). Change one dimension per prompt. Multi-goal prompts produce unpredictable edits.

## Step 7. Extend across screens

Once one screen is approved, generate the next screens with the consistency prompt (iteration prompt I-09). Reference the approved screen and list its tokens.

## Step 8. Handle states

For each interactive screen, request empty, loading, success, and error states. Use iteration prompt I-10.

## Step 9. Responsive check

Request mobile (360-414px) and desktop (1280px+) versions for every key screen. Check that content order on mobile follows task priority, not desktop column order.

## Step 10. Review generated output

Run [stitch-output-review.md](../qa/stitch-output-review.md) and the [anti-slop audit](../../../studio/creative-direction/anti-slop-audit.md). Record fails.

## Step 11. Export and transfer

Use an export path listed in [capabilities.md](../capabilities.md). Most are **Reported**, not yet verified by the studio. The first time you use one, confirm it works and update its status in that file.

- **Figma path (default for client-facing refinement):** export to Figma, rename layers, apply the token names from the handoff kit, build components.
- **Code path (prototypes and internal tools):** export code, then treat it as reference. Engineering rebuilds with project conventions, semantic HTML, and accessibility fixes.

Fill the [handoff kit](../handoff/handoff-kit.md) either way.

## Step 12. Validate implementation against design

After build, run the visual QA section of [stitch-output-review.md](../qa/stitch-output-review.md). Compare at the three breakpoints. Log differences as bug or accepted deviation.

## Common mistakes

- Prompting before the brief exists.
- Accepting the first output because it looks polished.
- Shipping exported code without semantic and accessibility fixes.
- Letting Stitch invent content that later ships.
