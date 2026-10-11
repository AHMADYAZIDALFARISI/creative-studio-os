# Stack Selection Guide

**Purpose:** Choose a stack per client based on needs, not team habit.
**Use when:** Before the technical specification.
**Output:** Stack decision with rationale in [templates/technical-specification.md](../../templates/technical-specification.md).

## Inputs to collect

1. Project type and complexity (pages, dynamic features, user accounts, payments).
2. Who edits content after launch, and how often.
3. Existing infrastructure (hosting, domain, CMS, CRM, ERP).
4. Who maintains the site after handover, and their skills.
5. Budget for hosting and services, per month, in the client's currency.
6. Performance and audience network conditions.
7. Data residency or regulatory constraints.

## Decision table

| Situation | Usually fits | Avoid when |
|---|---|---|
| Brochure site, rare edits, no accounts | Static site (Astro, Eleventy, or plain HTML/CSS) on static hosting | Client must edit daily without a developer |
| Marketing site with frequent edits by non-developers | Static or hybrid site + headless CMS, or WordPress with a lean custom theme | Team cannot maintain the CMS updates |
| Content-heavy site in a team already on WordPress | WordPress with a custom block theme | Complex app logic is required |
| Web app with accounts and dashboards | React with Next.js, or another full-stack framework the maintainer knows | The site is mostly static content |
| Small store, standard checkout | Hosted commerce platform (for example Shopify) or a local marketplace-integrated solution | Highly custom pricing or B2B logic |
| Custom commerce or B2B logic | Framework + commerce API or custom backend | Budget cannot cover ongoing maintenance |
| Internal tool, few users | Simple server-rendered app or low-code tool | Public scale or complex permissions |

## Rules

- The person who maintains the system after handover has a vote. A stack they cannot run becomes the client's problem.
- Prefer boring, well-documented tools for client work.
- Every dependency needs a reason in the spec.
- Record rejected options and why. It prevents re-litigating later.

## Common mistakes

- Choosing a framework for a three-page site because the team likes it.
- Ignoring monthly costs of managed services after the free tier.
