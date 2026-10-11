# Kopi Laras: Wholesale Website (Fictional Example)

> **FICTIONAL.** Kopi Laras, its people, data, and results are invented to demonstrate the workflow. Any resemblance to a real business is unintended. Numbers marked "illustrative" are not benchmarks.

**Created:** 2026-08-03 | **Lead:** Studio PM | **Client timezone:** WIB (UTC+7) | **Language:** ID (site in ID and EN)

## Why this example exists

It shows how each document feeds the next. Follow the links in order.

| Stage | Status | Gate evidence |
|---|---|---|
| 1 Onboarding | Done | [01-project-brief.md](01-project-brief.md) |
| 2 Discovery | Done | [02-discovery.md](02-discovery.md), client confirmed 2026-08-14 |
| 3 Proposal and SOW | Done | SOW signed 2026-08-19 (document kept in client drive) |
| 4 Strategy and direction | Done | [03-brand-strategy.md](03-brand-strategy.md), [04-creative-brief.md](04-creative-brief.md) |
| 5 Design | Done | [05-design.md](05-design.md) |
| 6 Engineering | Done | [06-technical-specification.md](06-technical-specification.md) |
| 7 QA and launch | Done | [07-test-plan.md](07-test-plan.md), [08-deployment-checklist.md](08-deployment-checklist.md) |
| 8 Handover and retro | Done | [09-handover.md](09-handover.md), [10-retrospective.md](10-retrospective.md) |

## How the documents connect

1. Discovery found that cafe owners, not home brewers, drive revenue **[Client]**, and that they ask about stock continuity and invoices before buying **[Client]**.
2. Positioning turned that into "consistent supply from named farms" instead of a lifestyle coffee brand.
3. The creative brief chose the "Field Ledger" direction because it makes supply data (harvest, roast date, stock) visible.
4. Stitch prompts used the brief's tokens and the UI requirement table, so outputs were reviewed against business needs, not taste.
5. The tech spec chose a static site plus a form service, because the client edits stock weekly and has no developer.
6. QA tested the wholesale inquiry journey first, because it is the success metric.

## Decision log

| Date | Decision | Reason | Decided by |
|---|---|---|---|
| 2026-08-14 | Primary audience: cafe owners in East Java | Discovery: wholesale is the main revenue line [Client] | Client owner + studio lead |
| 2026-08-28 | Direction "Field Ledger" over "Warm Ritual" | Supports supply-reliability message; differs from competitor lifestyle convention | Client owner |
| 2026-09-02 | Astro static site + headless form service, no e-commerce checkout | Wholesale orders are negotiated by WhatsApp; checkout adds cost without need | Studio lead, client agreed |
| 2026-09-15 | Stock status edited in a Markdown content file via CMS UI | Client staff update weekly; no developer on staff | Studio lead |

## Change requests

| CR | Summary | Status |
|---|---|---|
| CR-KL-001 | Add English version of product pages | Approved, +3 working days |
| CR-KL-002 | Add online card payment | Deferred to phase 2 |
