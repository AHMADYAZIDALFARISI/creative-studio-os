# Stitch Prompt Library: Applications

**Use:** Same rules as [websites.md](websites.md). Applications need states and data realism more than visual drama.

Shared app constraints (paste unless the brief says otherwise):
`Use realistic but clearly fictional sample data. Show table and form states. Visible focus styles. Minimum 44px touch targets on mobile. Avoid: decorative gradients, glass panels, emoji icons, oversized empty cards.`

---

## A-01 SaaS application: core workspace

```
CONTEXT
Product: {{PRODUCT}}, helps {{USER_ROLE}} to {{JOB}}. Most frequent task: {{FREQUENT_TASK}}, done {{FREQUENCY}}.

SCREEN
Desktop workspace at 1440px: navigation for {{NAV_ITEMS}}, main area for {{OBJECT}} list with search and filters, detail panel for the selected {{OBJECT}}, primary action "{{PRIMARY_ACTION}}".

CONSTRAINTS
Density: medium-high; the user works here for hours. Typography: {{TYPE}}. Neutral surfaces, one accent for primary actions, semantic colors for status only.
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
Default, empty (first use with guidance), and loading states.
```

**Evaluation:** frequent task reachable in two clicks; status readable without color alone.

---

## A-02 Admin dashboard

```
CONTEXT
Admins of {{SYSTEM}} need to answer: {{TOP_3_QUESTIONS}}. They act on: {{ACTIONS}}.

SCREEN
Overview with only the metrics that answer those questions: {{METRICS}} (label each with time range and comparison basis). Below, a table of {{RECORDS}} needing attention with bulk actions.

CONSTRAINTS
No metric without a defined time range. Charts only where trend matters; otherwise numbers. 
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
Default, no-data, and error-loading states. Table with sorting, pagination, and a selected-rows state.
```

**Evaluation:** each widget maps to one admin question; no vanity metrics.

---

## A-03 Fintech interface

```
CONTEXT
Product: {{PRODUCT}} for {{USER}} to {{FINANCIAL_TASK}} in {{CURRENCY}}. Regulator context: {{REGULATOR_OR_NONE}} (content only, no legal claims).

SCREEN
Mobile 390px: balance or position summary, recent transactions list, primary action {{ACTION}}. Then the confirmation screen for {{ACTION}} showing amount, fees, recipient, and final total before submit.

CONSTRAINTS
Numbers right-aligned with consistent decimals. Fees shown before confirmation. Destructive or irreversible actions need a confirmation step.
Do not display security badges or certifications the client does not hold.
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
States: pending, failed with reason and next step, success with reference number.
```

**Evaluation:** user sees total cost before committing; error tells how to recover.

---

## A-04 Educational platform

```
CONTEXT
Platform for {{LEARNERS}} learning {{SUBJECT}}. Sessions last about {{MINUTES}} minutes, often on {{DEVICE}}.

SCREEN
Learner home showing current course progress and next lesson; lesson page with content, progress indicator, and a short knowledge check.

CONSTRAINTS
Reading comfort first: 16-18px body, 60-75 character line length. Progress is honest (lessons completed, not invented percentages).
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
Correct and incorrect answer feedback states; offline or slow-network message.
```

**Evaluation:** learner knows what to do next within 3 seconds.

---

## A-05 AI-powered application

```
CONTEXT
App that uses AI to {{AI_TASK}} for {{USER}}. Input: {{INPUT_TYPE}}. Output: {{OUTPUT_TYPE}}.

SCREEN
Input area with guidance on what good input looks like; generating state; result view with edit, regenerate, copy or export, and feedback controls; history list.

CONSTRAINTS
Show that output can be wrong: a short note and an easy edit path. Never show a fabricated confidence percentage.
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
States: empty input, generating with cancel, partial failure, rate limit reached, success.
```

**Evaluation:** user stays in control; failure and limits are explained in plain language.

---

## A-06 Mobile-first web application

```
CONTEXT
Web app for {{USER}} who mostly use {{DEVICE_CONTEXT}} (for example mid-range Android, unstable mobile data). Main task: {{TASK}}.

SCREEN
390px: home with main task as the first action, bottom navigation with at most {{N}} items, task flow of {{N}} steps.

CONSTRAINTS
Thumb-reachable primary actions. Lightweight imagery. Forms use correct input types ({{INPUT_TYPES}}).
{{SHARED_APP_CONSTRAINTS}}

EXPECTED OUTPUT
Offline notice, slow loading skeleton, form error, and success states. Show the 1280px adaptation of the home screen.
```

**Evaluation:** task completes one-handed; no horizontal scrolling at 360px.
