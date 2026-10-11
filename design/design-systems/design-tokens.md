# Design Tokens

**Purpose:** Share one set of named values between design and code.

## Token layers

1. **Primitive:** raw values. `clay-600: #A4522E`.
2. **Semantic:** roles. `color-action: clay-600`.
3. **Component (only when needed):** `button-primary-bg: color-action`.

Code uses semantic tokens. Changing a client's brand should mean changing primitives and semantic mapping only.

## Minimum token set per project

- Color: ink, ink-muted, surface, surface-raised, border, action, action-hover, focus, success, warning, danger, info.
- Type: font-heading, font-body, font-mono (if used), size steps (6-8), line heights, weights.
- Space: 4px base scale: 4, 8, 12, 16, 24, 32, 48, 64, 96.
- Radius: 2-3 values maximum.
- Shadow or elevation: 2-3 values maximum, or none.
- Motion: duration-fast (120-150ms), duration-base (200-250ms), easing-standard.
- Breakpoints: 360 (design min), 768, 1024, 1280.

## CSS example

```css
:root {
  --color-ink: #1d1b19;
  --color-surface: #f6f1ea;
  --color-action: #a4522e;
  --color-focus: #1f5fbf;
  --font-heading: "Fraunces", Georgia, serif;
  --font-body: "Source Sans 3", system-ui, sans-serif;
  --space-4: 16px;
  --radius-1: 2px;
  --duration-base: 200ms;
}
```

Values above are illustrative. Each client gets its own.

## Common mistakes

- Naming tokens after colors in semantic layers (`--blue-button`).
- Adding a new token for every one-off value.
