# Technical Specification: Kopi Laras (Fictional)

## 1. Scope
Five pages in Indonesian (English added by CR-KL-001): Home, Origins (list + 3 detail), Wholesale, About the farms, Contact.

## 2. Stack decision
| Layer | Choice | Reason | Rejected |
|---|---|---|---|
| Site | Astro static site | Content site, fast on mobile, low hosting cost | Next.js: no app logic needed; WordPress: plugin maintenance burden for a team without a developer |
| Content editing | Git-based CMS editing Markdown files | Staff edit stock weekly through a web UI | Hand-editing code |
| Hosting | Static hosting with preview deploys | Free or low tier fits traffic | VPS: requires maintenance |
| Form | Hosted form service with email notification | No backend to maintain | Custom backend: unnecessary |

Product names of the CMS, hosting, and form service were chosen in the real spec. They are omitted here to keep the example vendor-neutral.

## 3. Data
Each origin is a Markdown file with frontmatter: `name`, `farm`, `notes`, `roastDate` (ISO date), `stockKg` (integer), `status` (`in`, `low`, `out`). Status is derived at build time: `out` if 0, `low` if under 20, else `in` (threshold set by client).

## 4. Non-functional
- Performance budget: LCP 2.5s or less on mobile; no client-side framework JavaScript except the form enhancement.
- Accessibility: WCAG 2.2 AA target.
- Locales: `id-ID` default, `en` under `/en/` with `hreflang`.

## 5. Environment variables
`FORM_ENDPOINT` (form service URL), `SITE_URL`. Values stored in the hosting dashboard only.

## 6. Risks
Stock goes stale if staff forget weekly edits. Mitigation: show the last-updated date (for example "Updated 2026-10-09") next to the table, so staleness is visible.
