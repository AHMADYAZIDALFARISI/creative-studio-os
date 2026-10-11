# Accessibility Checklist

**Target:** WCAG 2.2 Level AA unless the contract says otherwise.
**Use when:** Design review, before QA sign-off, and after major changes.

This checklist supports reviews. It does not certify conformance. A formal audit needs a qualified reviewer and assistive technology testing.

## Design stage

- [ ] Text contrast 4.5:1, large text (24px or 18.66px bold) 3:1, UI boundaries and icons 3:1.
- [ ] Color is never the only way to convey meaning.
- [ ] Focus indicator designed and visible on all interactive elements.
- [ ] Touch targets at least 24x24px CSS (WCAG 2.2 minimum); 44x44px recommended for primary mobile actions.
- [ ] Form fields have visible labels and error designs.
- [ ] Text can resize to 200% without loss of content.
- [ ] Motion has a reduced-motion alternative.

## Build stage

- [ ] Correct `lang` attribute on `<html>` (`id` or `en`), and on inline passages in another language.
- [ ] One `<h1>` per page, logical heading order.
- [ ] Landmarks: `header`, `nav`, `main`, `footer`.
- [ ] All images have appropriate `alt` (empty `alt=""` for decorative).
- [ ] Buttons are `<button>`, links are `<a href>`.
- [ ] Every function works with keyboard only. No keyboard traps.
- [ ] Skip link to main content.
- [ ] Dialogs trap focus while open and return focus on close.
- [ ] Error messages linked to fields with `aria-describedby`; dynamic status uses `aria-live` where appropriate.
- [ ] Page titles are unique and descriptive.

## Test stage

- [ ] Automated scan (for example axe DevTools or Lighthouse) with zero critical issues. Automated tools catch only part of the problems.
- [ ] Keyboard pass through every priority journey.
- [ ] Screen reader pass on at least one journey (NVDA + Firefox or Chrome on Windows, VoiceOver + Safari on macOS or iOS, TalkBack on Android).
- [ ] 200% zoom and 320px width check.

Record results in the project QA report with tool names and dates.
