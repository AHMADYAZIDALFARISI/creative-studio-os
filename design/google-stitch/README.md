# Google Stitch Toolkit

**Purpose:** Use Google Stitch for fast, directed UI exploration without letting it replace product thinking or engineering.
**Use when:** After a creative brief is approved. Never before.

## What Stitch is for here

- Generating first screens from a specific brief.
- Exploring two or three visual directions quickly.
- Extending an approved direction across more screens.
- Producing a starting point for handoff to Figma or code.

## What Stitch is not for here

- Deciding the business goal, information architecture, or content.
- Final accessibility or usability validation.
- Production code without engineering review.

## Files

| File | Use it to |
|---|---|
| [capabilities.md](capabilities.md) | Check what is verified vs unverified before relying on a feature |
| [workflows/stitch-workflow.md](workflows/stitch-workflow.md) | Follow the 12-step process from brief to validated implementation |
| [prompt-library/websites.md](prompt-library/websites.md) | Start prompts: corporate, portfolio, agency, campaign landing, e-commerce, experimental |
| [prompt-library/applications.md](prompt-library/applications.md) | Start prompts: SaaS, admin dashboard, fintech, education, AI app, mobile-first web app |
| [iteration-prompts/iteration-prompts.md](iteration-prompts/iteration-prompts.md) | Improve an existing Stitch output without rebuilding it |
| [handoff/handoff-kit.md](handoff/handoff-kit.md) | Prepare screens, components, tokens, states, and notes for developers |
| [qa/stitch-output-review.md](qa/stitch-output-review.md) | Review generated output and compare the implementation against the design |

## Prompt anatomy used across this toolkit

Every prompt has five blocks:

1. **Context:** client, audience, goal, direction summary.
2. **Screen request:** one screen or flow, with its content in priority order.
3. **Constraints:** typography, color, density, components to avoid, accessibility.
4. **Expected output:** what the screen must contain, including states.
5. **Evaluation:** how we will judge it. Stitch may not use this block, but the reviewer does.

Fill `{{PLACEHOLDERS}}` from the creative brief. Delete any constraint that does not apply instead of leaving it vague.
