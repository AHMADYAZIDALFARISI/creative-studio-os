# Design Critique Prompts

**Use:** Attach screenshots or exported frames plus the creative brief. AI critique supports, but does not replace, a human design review.

**C-01 Brief alignment**
```
Inputs: creative brief (attached), screens (attached).
Task: for each of the 10 creative direction parts in the brief, state whether the screens follow it, with a specific visual reference (section, element). Mark Follows / Partly / Does not follow.
Rule: judge against the brief, not your taste.
```

**C-02 Anti-slop audit**
```
Inputs: screens, creative brief.
Task: run the checklist in studio/creative-direction/anti-slop-audit.md. Mark each item Pass, Justified (quote the brief reason), or Fail with the exact element.
```

**C-03 Hierarchy and scanning**
```
Task: for each screen, list in order the first five elements a typical user would notice, and compare with the intended priority from the UI requirement table. Recommend the smallest changes to align them.
```

**C-04 Usability heuristics**
```
Task: review the flow {{FLOW}} against Nielsen's 10 usability heuristics. Report only concrete issues: screen, element, heuristic, severity (1-4), fix.
```

**C-05 Compare two directions**
```
Inputs: direction A and B on the same screens, brief, audience cards.
Task: compare on fit with positioning, audience task support, differentiation from competitors (attached findings), and build cost. Recommend one with reasons. Do not merge them.
```
