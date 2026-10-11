# Prompt Framework

**Purpose:** Write prompts that produce specific, verifiable output with low hallucination risk.
**Use when:** Any AI-assisted task on client or studio work.

## Full structure (for major tasks)

| Block | Question it answers |
|---|---|
| Role and expertise | Which expertise should the model apply? |
| Project context | What does the model need to know about the client and situation? |
| Objective | What single outcome do we want? |
| Input materials | Which documents or data are attached, and which is authoritative? |
| Constraints | What must it do or avoid? |
| Workflow | In what order should it work? |
| Deliverables | What exact output, in what format? |
| Quality criteria | How will we judge it? |
| Verification | What must it check, cite, or flag? |
| Failure handling | What should it do when information is missing? |

## Short structure (for simple tasks)

`Task + context in one line + output format + one constraint.`
Example: "Rewrite this error message for a checkout form. Audience: first-time mobile buyers in Indonesia. Output: Indonesian and English, max 15 words each. Say what to do next."

Do not force the full structure on simple tasks. Verbosity dilutes instructions.

## Rules

1. Give the source of truth. "Use only the attached discovery summary for facts about the client."
2. Ask for labels on uncertain claims: Client, Verified, Hypothesis, Recommendation.
3. State failure handling: "If a required fact is missing, list it under Open Questions instead of guessing."
4. Specify format and length.
5. Remove contradictions before sending. Read the prompt once as the model would.
6. Never paste secrets, credentials, or personal data that the task does not need.

## Where prompts live

- Lifecycle prompts: [lifecycle-prompts.md](lifecycle-prompts.md)
- Design critique: [../design-critique/critique-prompts.md](../design-critique/critique-prompts.md)
- Stitch: [../../design/google-stitch/prompt-library/websites.md](../../design/google-stitch/prompt-library/websites.md)
- Evaluate a prompt: [../evaluation/prompt-rubric.md](../evaluation/prompt-rubric.md)
