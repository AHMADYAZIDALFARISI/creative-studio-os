# Security Baseline

**Purpose:** Minimum controls for client projects. Use it as a review checklist.
**Reference:** OWASP Top 10 and OWASP ASVS for deeper requirements.

## Authentication

- [ ] Use a proven auth library or provider. Do not write password hashing or session crypto yourself.
- [ ] Passwords hashed with a modern algorithm (Argon2id or bcrypt) through the library.
- [ ] Rate limit and lockout or delay on login and password reset.
- [ ] Session cookies: `HttpOnly`, `Secure`, `SameSite=Lax` or stricter.
- [ ] Multi-factor authentication offered for admin accounts.

## Authorization

- [ ] Check permissions on the server for every request, not only in the UI.
- [ ] Check object ownership (user A cannot read `/orders/{id}` of user B).
- [ ] Admin functions on separate routes with separate checks.

## Input and output

- [ ] Parameterized queries or ORM. No string-built SQL.
- [ ] Output encoding by the framework; review every raw HTML insertion.
- [ ] CSRF protection for cookie-based sessions.
- [ ] Security headers: Content-Security-Policy, Strict-Transport-Security, X-Content-Type-Options, Referrer-Policy, frame protection.

## Secrets and dependencies

- [ ] No secrets in code, docs, logs, or client-side bundles.
- [ ] Secret scanning enabled on the repository where the platform supports it.
- [ ] Dependency audit run before launch (`npm audit`, `pip-audit`, or platform equivalent). High and critical issues resolved or documented.

## Payments

- [ ] Use the payment provider's hosted fields or checkout. Card data never touches our servers.
- [ ] Verify webhooks with the provider's signature.
- [ ] Reconcile order status from the provider, not from the browser redirect.

## Data

- [ ] HTTPS everywhere.
- [ ] Backups encrypted and access-restricted.
- [ ] Personal data minimized and retention defined.

## Reporting

Record reviewer, date, scope, and result in the QA report. If something was not reviewed, say so.
