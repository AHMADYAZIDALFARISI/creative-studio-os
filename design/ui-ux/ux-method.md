# UI/UX Method

**Purpose:** A sequence from requirements to tested, buildable screens.
**Inputs:** Discovery summary, journeys, creative brief.
**Output:** Sitemap, flows, wireframes, high-fidelity screens, handoff kit, usability findings.

## Steps

1. **Information architecture.** List content objects and tasks. Group by user mental model, not company org chart. Test labels with 5 people via a quick card sort or tree test when budget allows.
2. **Sitemap.** Maximum three levels for marketing sites. Mark each page with its primary task.
3. **User flows.** One flow per priority journey. Include entry points, decisions, errors, and exits.
4. **Wireframes.** Grayscale, real content length. Decide order and priority here, not in visual design.
5. **Visual exploration.** Use the [Stitch workflow](../google-stitch/workflows/stitch-workflow.md) or manual design.
6. **High-fidelity review.** Run [templates/design-review.md](../../templates/design-review.md) and the [anti-slop audit](../../studio/creative-direction/anti-slop-audit.md).
7. **Responsive strategy.** Design mobile and desktop for every key screen. Specify tablet behavior in the handoff kit.
8. **Usability test.** Five participants per round on the priority journeys. Record task success, time, and errors. Fix, then retest if a task failed for two or more people.
9. **Handoff.** Fill the [handoff kit](../google-stitch/handoff/handoff-kit.md).

## Pattern guidance

| Area | Rules |
|---|---|
| Navigation | 5-7 top-level items maximum. Current location always visible. Mobile menu has a visible label "Menu" or equivalent. |
| Tables and data | Left-align text, right-align numbers. Sticky header for long tables. Provide a card layout or horizontal scroll container on mobile, decided per table. |
| Search and filtering | Show active filters as removable chips. Show result count. Empty result offers "Clear filters". Keep filter state in the URL. |
| Forms | See [states-and-forms.md](states-and-forms.md). |

## Common mistakes

- Designing desktop only and "letting dev handle mobile".
- Testing with colleagues instead of target users.
- Skipping wireframes, then debating structure during visual review.
