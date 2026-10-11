# Stitch Iteration Prompts

**Purpose:** Improve an existing Stitch output with targeted edits.
**Rule:** One goal per prompt. Name what must stay unchanged. State how you will judge the result.

Template for every iteration:

```
KEEP: {{WHAT_MUST_NOT_CHANGE}}
CHANGE: {{ONE_GOAL}}
BECAUSE: {{PROBLEM_OBSERVED}}
DONE WHEN: {{CHECK}}
```

| ID | Goal | Prompt |
|---|---|---|
| I-01 | Improve visual hierarchy | `KEEP: layout structure, colors, copy. CHANGE: make "{{PRIMARY_ELEMENT}}" the first thing the eye lands on; reduce visual weight of {{COMPETING_ELEMENTS}} through size and weight, not color. BECAUSE: three elements compete for attention. DONE WHEN: a viewer names the primary element first in a 5-second look.` |
| I-02 | Fix generic patterns | `KEEP: content and brand colors. CHANGE: replace the {{GENERIC_PATTERN}} (for example centered hero with device mockup) with a layout driven by {{CLIENT_CONTENT}}; remove decorative {{BLOBS/GRADIENTS/GLASS}}. BECAUSE: it fails the competitor swap test. DONE WHEN: the section could not belong to {{COMPETITOR}}.` |
| I-03 | Refine typography | `KEEP: layout and colors. CHANGE: set headings in {{HEADING_FONT}} and body in {{BODY_FONT}}; use a type scale of {{SCALE}} (for example 16/20/28/40/64); body line length 60-75 characters; line height 1.5 for body. BECAUSE: hierarchy is flat. DONE WHEN: H1 is at least 2.5x body size and headings are distinguishable without color.` |
| I-04 | Adjust information density | `KEEP: components and style. CHANGE: {{INCREASE/DECREASE}} density: {{SPECIFIC_CHANGES}} (for example 8 rows per screen instead of 4, compact row height 44px). BECAUSE: users {{TASK_CONTEXT}}. DONE WHEN: {{N}} records visible at 1440x900 without losing readability.` |
| I-05 | Strengthen art direction | `KEEP: content and structure. CHANGE: apply the concept "{{CONCEPT}}" more consistently through {{TOOLS}} (for example rule lines, dated labels, monospace metadata). BECAUSE: the screen reads as neutral template. DONE WHEN: three concept cues are visible on the screen and each has a function.` |
| I-06 | Improve responsive behavior | `KEEP: desktop design. CHANGE: create a 390px version where content order follows {{TASK_PRIORITY}}; collapse {{ELEMENTS}} into {{PATTERN}}; keep tap targets at least 44px. BECAUSE: desktop columns stack into a confusing order. DONE WHEN: primary action is visible without scrolling and no horizontal scroll exists.` |
| I-07 | Increase accessibility | `KEEP: visual direction. CHANGE: raise text contrast to at least 4.5:1 and UI boundaries to 3:1; add visible focus states; add text labels to icon-only buttons; ensure form fields have persistent labels. BECAUSE: {{FAILED_CHECKS}}. DONE WHEN: all listed checks pass in manual review.` |
| I-08 | Improve conversion section | `KEEP: brand style. CHANGE: rebuild the {{SECTION}} so it answers {{USER_QUESTION}} before asking for {{ACTION}}; show real proof {{PROOF}} or none; one primary CTA. BECAUSE: the CTA appears before the offer is clear. DONE WHEN: the section reads as question, answer, proof, action.` |
| I-09 | Maintain consistency across screens | `KEEP: everything in the approved screen "{{APPROVED_SCREEN}}". CHANGE: design "{{NEW_SCREEN}}" using the same tokens: colors {{HEXES}}, fonts {{FONTS}}, spacing scale {{SCALE}}, radius {{RADIUS}}, button styles and navigation unchanged. BECAUSE: new screens drift. DONE WHEN: no new color, font size, or radius appears that is not in the token list.` |
| I-10 | Refine interaction states | `KEEP: default state design. CHANGE: add {{STATES}} (hover, focus, active, disabled, loading, empty, error, success) for {{COMPONENT_OR_SCREEN}}. Error messages say what happened and what to do next. BECAUSE: only the happy path exists. DONE WHEN: every listed state is shown and labeled.` |
| I-11 | Compare two creative directions | `KEEP: identical content and screen type. CHANGE: produce direction A ({{A_CONSTRAINTS}}) and direction B ({{B_CONSTRAINTS}}) side by side. BECAUSE: the client needs to choose an idea, not a color. DONE WHEN: A and B differ on at least two axes: density, typographic voice, structure, image role, tone.` |
| I-12 | Critique and improve without rebuilding | `KEEP: overall layout, palette, and content. CHANGE: first list the five weakest details in this screen (hierarchy, spacing, alignment, contrast, consistency), then fix only those five. BECAUSE: the design is close; a rebuild would lose approved decisions. DONE WHEN: the five fixes are visible and nothing else changed.` |

## Common mistakes

- "Make it more premium." Name the property: type contrast, spacing, image quality, restraint in color.
- Stacking five goals in one prompt.
- Forgetting the KEEP line, which invites Stitch to redesign approved parts.
