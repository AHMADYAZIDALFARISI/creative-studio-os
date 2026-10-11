# Backend Handbook

**Purpose:** Practical standards for APIs, data, and server-side features.

## Architecture options

| Option | Fits | Trade-offs |
|---|---|---|
| Serverless functions | Low or spiky traffic, small APIs, form handlers, webhooks | Cold starts, execution limits, vendor lock-in, harder local debugging |
| Managed backend (BaaS: hosted database + auth + storage) | MVPs, small teams, standard CRUD with auth | Fast start; pricing grows with usage; limits on custom logic; data portability needs planning |
| Custom backend application | Complex business logic, integrations, long-running jobs, strict control | Highest flexibility; you own uptime, security patches, scaling |

Pick the simplest option that meets the requirements for the next 12-18 months. Document the migration path if growth is expected.

## Standards

- **Validation:** validate every input at the boundary with a schema. Reject unknown fields.
- **Errors:** consistent error format (see [REST guidelines](../api-design/rest-guidelines.md)). Never leak stack traces to clients.
- **Logging:** structured logs (JSON) with request ID, no secrets or full personal data. Define retention.
- **Monitoring:** uptime check on key endpoints, error tracking, alert to a named person.
- **Rate limiting:** on auth, forms, and any expensive endpoint.
- **Secrets:** environment variables or a secret manager. Rotate on staff changes and incidents.
- **File uploads:** check type by content, limit size, store outside the web root or in object storage, generate new filenames, scan if the risk warrants it.
- **Email:** use a transactional provider, configure SPF, DKIM, and DMARC on the sending domain, handle bounces.
- **Background jobs:** only when work exceeds request time or must retry. Jobs must be idempotent.
- **Migrations:** versioned, reviewed, reversible where possible, run in CI before production.
- **Backups:** automated, tested by restoring at least once before launch. Record recovery point and recovery time targets with the client.
- **API documentation:** OpenAPI for REST APIs, kept next to the code.
- **Integration tests:** for each external integration, test success, failure, and timeout paths.

## Honesty rule

Do not tell a client their authentication, payments, or data protection is secure unless someone reviewed the actual implementation against the [security baseline](../authentication-security/security-baseline.md) and recorded the result.
