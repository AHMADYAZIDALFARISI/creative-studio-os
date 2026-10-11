# Prompt Evaluation Rubric

**Use when:** Before adding a prompt to any library in this repo, and when a prompt gives poor results.

Score each criterion 0-2. A library prompt needs 13 or more out of 16, with no zero on Verifiability or Hallucination risk.

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Clarity | Goal unclear | Goal clear, wording loose | One unambiguous goal |
| Context sufficiency | No context | Some context, key facts missing | All facts the task needs, with source of truth named |
| Constraint quality | None or contradictory | Present but vague ("modern") | Specific, non-conflicting, testable |
| Actionability | Model must guess steps | Steps implied | Workflow or clear task order |
| Output specificity | Format unspecified | Format named | Format, length, sections defined |
| Verifiability | Output cannot be checked | Partly checkable | Quality criteria or checks stated |
| Hallucination risk (low = 2) | Invites invention | Some guardrails | Requires sources, labels, and open questions for gaps |
| Unnecessary complexity (low = 2) | Bloated or repetitive | Some excess | As short as the task allows |

## Weak vs improved

**Example 1: Landing page**

Weak:
> Make a modern, beautiful, premium landing page for a coffee brand.

Improved:
> Design a mobile-first landing page (390px, then 1280px) for Kopi Laras, a fictional single-origin roaster in Malang selling to home brewers and cafes. Goal: wholesale inquiry from cafe owners. Sections in order: origin statement, three single-origin products with tasting notes and wholesale MOQ, roasting schedule, inquiry form (name, cafe name, city, WhatsApp number, monthly volume). Typography: Fraunces for headings, Source Sans 3 for body. Colors: #1d1b19 ink, #f6f1ea surface, #a4522e action only. Avoid gradients, glass effects, emoji icons, invented testimonials or statistics. Include form error and success states.

Why better: names audience, goal, content, tokens, exclusions, and states. Score moves from 3 to 15.

**Example 2: Code review**

Weak:
> Review my code and make it better.

Improved:
> Review the attached diff for the order cancellation endpoint. Check authorization (only the order owner or an admin can cancel), status rules (only "pending" orders), and error format per our REST guidelines. Report issues as blocker, should, or nit with file and line. Do not rewrite the code. List anything you could not verify.

**Example 3: Research**

Weak:
> Give me statistics about the Indonesian coffee market.

Improved:
> List publicly available sources (government statistics agency, trade associations, peer-reviewed studies) that publish data on Indonesian specialty coffee consumption. For each: publisher, title, year, URL, what it measures. Do not state any figure you cannot attribute to a listed source. If you cannot access sources, say so instead of estimating.
