# Anti-Slop Audit

**Purpose:** Detect generic, unjustified, or fabricated output before a client sees it.
**Use when:** On every creative direction, every Stitch output you plan to keep, every design review, and before launch.
**Who:** Someone who did not make the work.

Generic patterns are not banned. They are banned **as defaults**. A pattern passes when the audit records a brief-specific reason for it.

## Scoring

Mark each item **Pass**, **Justified** (pattern present, reason written), or **Fail**. Any Fail blocks the review.

## A. Concept

| # | Check | Fail signal |
|---|---|---|
| A1 | The direction links to a written business goal | Rationale is "it looks modern" |
| A2 | Swap test: replace the logo with a competitor's | The design still works for them unchanged |
| A3 | Name test: describe the concept in two sentences without "clean", "modern", "premium", "sleek" | You cannot |

## B. Layout

| # | Check | Fail signal |
|---|---|---|
| B1 | Hero is built from this client's content | Centered headline + subline + two buttons + device mockup with no reason |
| B2 | Card grids carry content that is truly parallel | Three icon cards used for unrelated ideas |
| B3 | Section rhythm varies with content importance | Every section has the same height and structure |
| B4 | Density fits the audience task | Dashboard with large empty cards; editorial page packed like a dashboard |

## C. Visual language

| # | Check | Fail signal |
|---|---|---|
| C1 | Typeface choice has a rationale | Inter or system default with no reason given |
| C2 | Type scale has visible contrast | All headings within 1.25x of each other |
| C3 | Color comes from the brand strategy | Purple-blue gradient with no brand link |
| C4 | Decoration has a job | Floating blobs, orbs, noise, or glows that carry no meaning |
| C5 | Surface treatment fits | Glassmorphism on every container |
| C6 | Radius and shape follow a rule | Every element is a pill or a heavily rounded card |
| C7 | Icons are a consistent, professional set | Emoji used as icons in a professional interface |

## D. Content and honesty

| # | Check | Fail signal |
|---|---|---|
| D1 | No fabricated testimonials | Quotes with invented names or stock avatars |
| D2 | No invented logos or partners | "Trusted by" row of logos without permission |
| D3 | No invented metrics | "10,000+ happy customers" without a source |
| D4 | Placeholder copy is visibly marked | Realistic fake copy that could ship by accident |
| D5 | Copy speaks to the audience's real question | Generic benefit statements ("Boost your productivity") |

## E. Interaction

| # | Check | Fail signal |
|---|---|---|
| E1 | Every animation has a purpose (feedback, orientation, continuity) | Scroll-triggered fades on every block |
| E2 | Motion respects `prefers-reduced-motion` | No reduced-motion handling |
| E3 | All states exist | Only the happy path is designed |

## F. Code and documents

| # | Check | Fail signal |
|---|---|---|
| F1 | Dependencies have a reason | Animation or UI library added for one effect |
| F2 | Documents marked complete contain real guidance | Headings with empty sections |
| F3 | Prompts have no contradictions | "Minimal and bold, colorful and muted" |

## Recording the result

```markdown
Anti-slop audit: {{SCREEN_OR_DELIVERABLE}} | Reviewer: {{NAME}} | Date: {{YYYY-MM-DD}}
Fails: C3 (gradient not tied to brand), D3 (metric without source)
Justified: B2 (three cards = three real service tiers)
Action: replace gradient with brand clay/ink palette; remove metric until client supplies source
```

**Next:** use the [Claude Code skill](../../.claude/skills/anti-slop-audit/SKILL.md) to run this audit with an agent, then confirm by hand.
