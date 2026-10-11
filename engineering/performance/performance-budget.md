# Performance Budget

**Purpose:** Set measurable performance targets per project.

## Default targets (adjust in the tech spec)

Measured at the 75th percentile on mobile, using field data when available and lab data before launch:

| Metric | Target |
|---|---|
| Largest Contentful Paint (LCP) | 2.5s or less |
| Interaction to Next Paint (INP) | 200ms or less |
| Cumulative Layout Shift (CLS) | 0.1 or less |
| JavaScript shipped on marketing pages | Under 150KB compressed, unless justified |
| Hero image | Under 200KB at mobile size |

These follow Google's published Core Web Vitals "good" thresholds. Confirm current thresholds on web.dev before contract commitments.

## How to test

1. Lighthouse in Chrome DevTools with mobile throttling, three runs, median.
2. WebPageTest or PageSpeed Insights on a real URL before launch.
3. Test on a mid-range Android phone on a mobile connection.

## Common causes and fixes

| Problem | Fix |
|---|---|
| Slow LCP | Optimize hero image, preload it, reduce render-blocking CSS and fonts |
| High CLS | Set image dimensions, reserve space for embeds and banners, use matched font fallbacks |
| Poor INP | Reduce JavaScript, split long tasks, avoid heavy third-party scripts |

Report actual measured values. Do not claim a score that was not measured.
