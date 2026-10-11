# Google Stitch: Capability Notes

**Purpose:** Separate what we have verified from what we have only read about.
**Last reviewed:** 2026-10-12. Recheck before each new project. Stitch changes often.

Stitch is a Google Labs product. Entry point used by the studio: https://stitch.withgoogle.com (confirm the address in Google Labs before sharing it with clients).

## Status labels

- **Reported:** described in third-party reviews or announcements. Confirm in the Stitch interface before relying on it.
- **Verified by studio:** a team member confirmed it in the interface and recorded the date.
- **Unknown:** no reliable information. Do not plan around it.

## Capability table

| Capability | Status | Notes |
|---|---|---|
| Generate UI screens from a text prompt | Reported [S1, S2, S4] | Core function in all sources reviewed. |
| Use images or sketches as input | Reported [S2, S4] | Useful for wireframe-to-UI. Upload only assets the client has cleared. |
| Generate multiple design variants | Reported [S3] | Use for direction exploration. |
| Edit a design through follow-up chat prompts | Reported [S3, S5] | Basis of our iteration prompt library. |
| Export to Figma (paste as editable layers) | Reported [S1, S2, S4] | Treat Figma as the refinement and handoff source of truth. |
| Export HTML/CSS (and reportedly Tailwind and other frameworks) | Reported [S1, S4, S5] | Treat as a prototype. Engineering rewrites to project conventions. |
| DESIGN.md design-rule file | Reported, 2026 update [S5] | Check format in the current UI before generating one. |
| MCP server or SDK for coding agents | Reported, 2026 update [S4, S5] | Do not script against it until a team member verifies setup from official docs. |
| Export to Google AI Studio or Jules | Reported [S3, S4] | Not part of our default workflow. |
| Other export options (.zip, copy code, project brief, instant prototype) | Reported [S4] | Labels may differ in the current UI. |
| Public REST API with documented endpoints | Unknown | Do not invent endpoints or automation. |
| Language support beyond English prompts | Unknown | Write prompts in English. Put Indonesian UI copy in quotes as content. |

## Sources (accessed 2026-10-12)

All are third-party. None is official Google documentation. That is why every capability stays **Reported**.

- [S1] index.dev, Google Stitch AI review for UI designers: https://index.dev/blog/google-stitch-ai-review-for-ui-designers
- [S2] Digital Citizen, What is Google Stitch: https://www.digitalcitizen.life/what-is-google-stitch-and-how-it-turns-text-into-app-designs/
- [S3] MindStudio, What is Google Stitch: https://www.mindstudio.ai/blog/what-is-google-stitch-ai-design-tool
- [S4] Moda, Google Stitch review: https://moda.app/blog/google-stitch-review
- [S5] Redwerk, Google Stitch vibe design tool: https://redwerk.com/blog/google-stitch-ai-vibe-design-tool/

Replace these with official Google documentation links when the team finds them.

## Default workflow decision

We use a **manual, prompt-driven workflow** with copy-ready prompts and documented handoff. If the team later verifies the MCP integration, add a section here with the verified setup steps, version, and date. Do not automate before that.

## How to verify a capability

1. Test it in the Stitch interface on a throwaway project.
2. Record: date, account type, what worked, what failed.
3. Update this table to **Verified by studio (YYYY-MM-DD, initials)**.
