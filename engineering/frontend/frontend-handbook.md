# Frontend Handbook

**Purpose:** Production standards for frontend work across stacks.

## Foundations

- **Semantic HTML first.** Correct elements give accessibility, SEO, and behavior for free.
- **Modern CSS.** Custom properties for tokens, Grid and Flexbox for layout, `clamp()` for fluid type, container queries where components live in variable widths, logical properties for spacing.
- **TypeScript** for any app with state or data. Plain JS is acceptable for small static enhancements.
- **React/Next.js** when the project needs component-driven interactivity, client state, or a full-stack framework. Not by default for static content.

## Components

- Compose small components. Avoid abstractions until a pattern repeats three times.
- Props describe intent (`variant="primary"`), not style (`color="red"`).
- Keep data fetching out of presentational components.

## State

- Start with local state. Lift it only when siblings need it.
- Server data belongs in a server-state tool or framework loader, not a global store.
- Keep URL state for filters, tabs, and pagination so links are shareable.

## Forms and validation

- Validate on client for experience and on server for truth. Share schemas where the stack allows.
- Follow [states-and-forms.md](../../design/ui-ux/states-and-forms.md).

## Data fetching and routing

- Handle loading, error, and empty for every request.
- Set timeouts. Show retry for recoverable errors.
- Use the framework router. Every view has a URL when users might share or return to it.

## Assets

- Images: modern formats (AVIF/WebP) with fallback, `srcset` and `sizes`, explicit `width` and `height`, `loading="lazy"` below the fold, priority loading only for the main hero image.
- Fonts: self-host or use a fast provider, subset, `font-display: swap`, preload only the critical weight.

## Animation

Follow [interaction-motion.md](../../design/interaction-design/interaction-motion.md). Add an animation library only if CSS cannot meet the spec.

## Error boundaries

In React apps, wrap route-level sections in error boundaries with a recovery action and logging.

## SEO

Unique `<title>` and meta description, canonical URLs, Open Graph tags, `sitemap.xml`, `robots.txt`, structured data only when it truthfully matches page content.

## Internationalization

- Set `lang` per page. Use `hreflang` for language variants.
- Externalize strings when more than one language is in scope.
- Format numbers, currency, and dates with `Intl` APIs (`id-ID`, `en-US`, and so on).
- Allow for text expansion: English to Indonesian copy often grows.

## Environment variables

- Never commit `.env`. Commit `.env.example` with names and descriptions only.
- Anything exposed to the browser (for example `NEXT_PUBLIC_*`) is public. Never put secrets there.

## Production build verification

Before every release: clean install, type check, lint, tests, production build, start the build locally, click through priority journeys.
