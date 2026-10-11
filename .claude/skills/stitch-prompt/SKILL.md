---
name: stitch-prompt
description: Write a Google Stitch prompt or iteration prompt for a client screen from the approved creative brief and UI requirement table. Use when the user asks for a Stitch prompt, a UI generation prompt, or an iteration on a Stitch output.
---

# Stitch prompt

1. Read `design/google-stitch/README.md` (prompt anatomy) and `design/google-stitch/capabilities.md` (what is verified).
2. Read the project's `04-creative-brief.md`. If no direction is approved, stop and ask for one. Do not invent a visual direction.
3. Read the UI requirement table in the project's design file if it exists.
4. Choose the closest start prompt from `design/google-stitch/prompt-library/` or iteration prompt from `design/google-stitch/iteration-prompts/iteration-prompts.md`.
5. Fill every placeholder from the brief. Use only its tokens (fonts, hex values, layout rule). Include the avoid list.
6. Keep blocks 1-4 under 250 words. Put the evaluation block separately for the reviewer.
7. Mark all sample content as sample or fictional if it is not real client content.

Do not claim Stitch features beyond those listed in `capabilities.md`.
