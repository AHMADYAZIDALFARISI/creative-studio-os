# Interaction and Motion

**Purpose:** Use interaction and motion to give feedback, orientation, and continuity, not decoration.

## Motion has one of three jobs

1. **Feedback:** confirm an action happened (button press, item added).
2. **Orientation:** show where something came from or went (panel opens from its trigger).
3. **Continuity:** keep context during a change (list reorders smoothly).

If an animation has none of these jobs, remove it.

## Timing defaults

- Micro feedback: 100-150ms.
- Small transitions (menus, tooltips): 150-250ms.
- Larger panels or page-level: 250-400ms.
- Ease-out for entering, ease-in for leaving.

## Performance

- Animate `transform` and `opacity`. Avoid animating layout properties (width, height, top, left).
- No scroll-jacking. Do not override native scroll speed.
- Test on a mid-range Android phone, not only a laptop.

## Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

Use this as a baseline, then design specific reduced alternatives for key moments.

## Common mistakes

- Fade-up on every section during scroll.
- Hover-only interactions with no touch or keyboard equivalent.
