---
name: anti-slop-audit
description: Audit a design, Stitch output, page, or creative direction for generic AI-style patterns, unjustified decoration, and fabricated content using the studio's anti-slop checklist. Use when reviewing design deliverables, screenshots, HTML/CSS, or creative briefs before a client sees them.
---

# Anti-slop audit

1. Read `studio/creative-direction/anti-slop-audit.md` for the checklist (sections A-F).
2. Read the project's approved creative brief (`projects/<slug>/04-creative-brief.md`) if it exists. Without a brief, report that items A1 and C1-C3 cannot be judged.
3. Inspect the deliverable (files, screenshots, or code the user points to).
4. For every item, mark Pass, Justified (quote the brief sentence that justifies it), or Fail (name the exact element, section, or line).
5. Output the result block in the format at the end of the checklist file, followed by a list of the smallest fixes for each Fail.

Rules:
- Judge against the brief, not personal taste.
- Do not mark Pass on anything you could not see. Mark it "Not reviewed" and say why.
- Do not edit files during the audit.
