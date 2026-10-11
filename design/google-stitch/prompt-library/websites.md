# Stitch Prompt Library: Websites

**Use:** Copy a prompt, fill every `{{PLACEHOLDER}}` from the creative brief, delete lines that do not apply. Paste blocks 1-4 into Stitch. Keep block 5 for the reviewer.

Shared avoid list (paste into any prompt unless the brief justifies an item):
`Avoid: purple-blue gradients, glassmorphism, floating blobs or orbs, emoji icons, fake testimonials, invented client logos, invented statistics, identical three-card rows, pill buttons everywhere.`

---

## W-01 Premium corporate website: home

```
CONTEXT
Company: {{COMPANY}}, a {{INDUSTRY}} firm serving {{AUDIENCE}} in {{MARKETS}}.
Goal of this page: help {{PRIMARY_VISITOR}} decide to {{PRIMARY_ACTION}}.
Visual concept: {{TWO_SENTENCE_CONCEPT}}

SCREEN
Responsive desktop home page, 1440px wide. Sections in priority order:
1. Statement of what the company does, in one line: "{{VALUE_LINE}}"
2. Three to five services with a one-line outcome each: {{SERVICES}}
3. How engagements work, as a numbered process of {{N}} steps
4. Selected work: {{N}} case summaries with problem, approach, result (use "Result pending" if none)
5. Leadership or team credibility: {{CREDIBILITY_CONTENT}}
6. Contact with {{CONTACT_METHOD}}

CONSTRAINTS
Typography: {{HEADING_FONT}} for headings, {{BODY_FONT}} for body. Strong size contrast between H1 and body.
Color: {{HEX_PRIMARY}} ink, {{HEX_SURFACE}} background, {{HEX_ACCENT}} accent used only for actions.
Layout: {{GRID_RULE}}. Generous margins. Left-aligned text.
{{SHARED_AVOID_LIST}}

EXPECTED OUTPUT
One full page. Real copy above. Placeholder images labeled "PHOTO: {{DESCRIPTION}}". Visible focus styles on links and buttons.
```

**Evaluation:** value line readable in 5 seconds; services describe outcomes; no fabricated proof; accent reserved for actions; passes swap test.

---

## W-02 Editorial or creative portfolio

```
CONTEXT
Portfolio for {{PERSON_OR_STUDIO}}, a {{DISCIPLINE}} practice. Visitors are {{AUDIENCE}} who want to judge {{QUALITY_THEY_JUDGE}}.
Visual concept: {{CONCEPT}}

SCREEN
Desktop index page listing {{N}} projects. Each project shows: title, year, discipline, one-line description, one image.
Then a project detail page: hero image, context, role, process with 3-4 images, outcome, credits.

CONSTRAINTS
Work is the focus. Interface elements stay quiet.
Typography: {{TYPE_CHOICE}}; use size and weight, not color, for hierarchy.
Layout: {{LIST_OR_ASYMMETRIC_GRID}}. Image ratios vary with the work; do not force identical crops.
{{SHARED_AVOID_LIST}}

EXPECTED OUTPUT
Index and detail page. Captions under images. Next-project navigation at the end of detail.
```

**Evaluation:** images dominate; navigation never competes with work; detail page tells problem-process-outcome.

---

## W-03 Agency website

```
CONTEXT
Agency: {{AGENCY}}. Specialization: {{SPECIALIZATION}}. Ideal client: {{IDEAL_CLIENT}}.
Differentiator: {{DIFFERENTIATOR}}.

SCREEN
Home page with: positioning line, capabilities grouped by client problem (not by service name), 3 case studies with measurable results only where real, working model and pricing approach, contact.

CONSTRAINTS
Show method and evidence, not adjectives. Typography: {{TYPE}}. Color: {{COLORS}}.
{{SHARED_AVOID_LIST}}

EXPECTED OUTPUT
Desktop and mobile versions. Case studies use "Result: to be confirmed" if no verified result exists.
```

**Evaluation:** a prospect can tell in one scroll whether the agency fits their problem.

---

## W-04 Campaign landing page

```
CONTEXT
Campaign: {{CAMPAIGN}} for {{BRAND}}. Runs {{START_DATE}} to {{END_DATE}} ({{TIMEZONE}}).
Traffic source: {{SOURCE}}. Single conversion goal: {{CONVERSION}}.

SCREEN
Mobile-first landing page, 390px wide, then desktop. Order: offer and deadline, what you get, how it works in 3 steps, terms summary, FAQ (5 real questions: {{QUESTIONS}}), form or CTA.

CONSTRAINTS
One primary CTA repeated at most 3 times. No navigation menu. Form fields: {{FIELDS}} only.
Countdown only if the deadline is real.
{{SHARED_AVOID_LIST}}

EXPECTED OUTPUT
Include form validation error state and success state.
```

**Evaluation:** offer understood above the fold on mobile; form has visible labels; terms are not hidden.

---

## W-05 E-commerce storefront: product listing and detail

```
CONTEXT
Store: {{STORE}} selling {{PRODUCT_CATEGORY}} to {{AUDIENCE}}. Average catalog size: {{N}} products.
Buyer's main decision factor: {{FACTOR}} (for example size, origin, compatibility).

SCREEN
1. Category listing: filters for {{FILTERS}}, sort, product cards showing name, price in {{CURRENCY}}, {{KEY_ATTRIBUTE}}, stock status.
2. Product detail: gallery, name, price, variant selector, quantity, add to cart, delivery estimate, {{KEY_ATTRIBUTE}} explained, returns summary.

CONSTRAINTS
Price format: {{PRICE_FORMAT}} (for example "Rp 125.000" or "$12.50").
Product cards are identical in structure; this is a justified grid.
{{SHARED_AVOID_LIST}}

EXPECTED OUTPUT
Mobile and desktop. States: out of stock, variant unavailable, empty filter result with a reset action.
```

**Evaluation:** decision factor visible on cards; filters usable on mobile; stock and delivery clear before cart.

---

## W-06 Experimental or art-directed experience

```
CONTEXT
Purpose: {{PURPOSE}} (for example exhibition microsite, launch story). Audience: {{AUDIENCE}}.
Concept: {{CONCEPT}}. The experience must still let users {{ESSENTIAL_TASK}}.

SCREEN
Opening screen and one content screen that express the concept through {{EXPRESSIVE_TOOL}} (type, layout, image sequencing).

CONSTRAINTS
Expressive layout is allowed. Navigation and essential information stay findable within one action.
Body text remains at least 16px and meets contrast.
Any motion must have a static fallback.

EXPECTED OUTPUT
Desktop and mobile. Annotate any intended motion in text.
```

**Evaluation:** concept is legible; essential task completes without instructions; reduced-motion version exists.
