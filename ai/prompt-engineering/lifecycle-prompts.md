# Lifecycle Prompts

**Use:** Copy, fill placeholders, attach inputs. Each prompt states inputs, output, and verification. Review every output before use.

## Discovery

**P-01 Discovery summary from notes**
```
You are a strategist preparing a discovery summary.
Inputs: interview notes (attached), intake form (attached). These are the only sources of client facts.
Task: produce a discovery summary using the section order in templates/client-discovery.md.
Rules: label every claim [Client], [Verified], [Hypothesis], or [Recommendation]. Do not add market statistics. List missing information under "Open questions" with who should answer.
Output: Markdown, max 900 words.
```

## Research

**P-02 Competitor observation table**
```
Inputs: my notes and screenshots from {{N}} competitor sites (attached).
Task: fill the table in studio/research/competitor-analysis.md and list category conventions.
Rules: observations only from the inputs. Do not estimate traffic, revenue, or market share. Mark anything inferred as [Hypothesis].
```

## Brand strategy

**P-03 Positioning drafts**
```
Inputs: confirmed discovery summary, competitor findings.
Task: write 3 positioning statements using the template in studio/strategy/positioning.md. Each must use a different reason to believe drawn from the inputs.
Quality: a competitor could not sign the statement unchanged. For each, explain in one line why.
```

## Art direction

**P-04 Creative direction options**
```
Inputs: positioning, audience cards, competitor conventions.
Task: propose 3 creative directions using the 10-part structure in studio/creative-direction/creative-direction-method.md. Directions must differ on at least two axes (density, typographic voice, structure, image role, tone).
Rules: no purple-blue gradients, glassmorphism, or generic SaaS layouts unless you justify them from the inputs. Name real typefaces with license type.
```

## Google Stitch

**P-05 Stitch prompt from creative brief**
```
Inputs: approved creative brief, UI requirement table, screen content.
Task: write a Stitch prompt for screen {{SCREEN}} using the five-block anatomy in design/google-stitch/README.md.
Rules: use only tokens from the brief. Include the avoid list. Max 250 words for blocks 1-4.
```

## UI/UX critique

**P-06** See [design critique prompts](../design-critique/critique-prompts.md).

## Frontend implementation

**P-07 Implement a component**
```
Context: repo uses {{STACK}}. Read {{FILES}} first and follow their conventions.
Task: implement {{COMPONENT}} per the handoff kit entry (attached).
Requirements: semantic HTML, tokens only, all listed states, keyboard support, reduced motion.
Output: code plus a short note listing any spec ambiguity you resolved and how.
Verification: run type check, lint, and tests; report actual results.
```

## Backend implementation

**P-08 Implement an endpoint**
```
Context: API contract (attached), existing service code in {{PATH}}.
Task: implement {{METHOD}} {{PATH}}.
Requirements: schema validation, authorization check, error format from engineering/api-design/rest-guidelines.md, integration tests for success, validation failure, unauthorized, not found.
Rules: no new dependencies without stating why. No secrets in code.
```

## Refactoring

**P-09**
```
Task: refactor {{FILE}} to {{GOAL}} without changing behavior.
Workflow: list current behavior and existing tests first; add tests if coverage is missing; refactor in small steps; run tests after each.
Output: diff summary and test results.
```

## Debugging

**P-10**
```
Symptom: {{SYMPTOM}}. Expected: {{EXPECTED}}. Steps to reproduce: {{STEPS}}. Logs: attached.
Task: list hypotheses ranked by likelihood with the evidence for each, then the smallest experiment to confirm the top one. Do not change code until a hypothesis is confirmed.
```

## Testing

**P-11**
```
Inputs: spec section and code for {{FEATURE}}.
Task: write a test plan table (case, input, expected, type) covering happy path, edge cases, error paths, and permissions. Then implement the unit and integration tests.
```

## Accessibility

**P-12**
```
Inputs: page HTML or component code.
Task: review against design/accessibility/accessibility-checklist.md build-stage items. For each issue: element, problem, WCAG criterion, fix.
Rule: state that automated review cannot confirm full conformance.
```

## Security

**P-13**
```
Inputs: code for {{FEATURE}} (auth, payments, uploads, or personal data).
Task: review against engineering/authentication-security/security-baseline.md. Report findings with severity, location, and fix.
Rule: do not declare the feature secure. Report what you reviewed and what you could not review.
```

## Performance

**P-14**
```
Inputs: Lighthouse report JSON or trace (attached), page code.
Task: identify the three changes with the largest expected impact on LCP, INP, and CLS. Cite the specific report entries.
```

## Documentation

**P-15**
```
Task: write {{DOC}} for {{AUDIENCE}}. It must answer: purpose, when to use, inputs, steps, output, quality check, common mistakes, next step.
Rules: active voice, short sentences, no claims beyond the attached sources.
```

## Code review

**P-16**
```
Inputs: diff (attached), ticket.
Task: review using engineering/code-review/review-checklist.md. Prefix comments with blocker, should, or nit. Point to file and line.
```

## Deployment

**P-17**
```
Inputs: deployment checklist, release notes, environment list.
Task: produce a release runbook with commands, owners, timing in {{TIMEZONE}}, smoke tests, and rollback triggers and steps.
```

## Handover

**P-18**
```
Inputs: project docs folder, credentials inventory (names only, no values).
Task: draft the handover document using templates/project-handover.md in {{LANGUAGE}}. Flag any missing items.
```
