# Deployment and Rollback

## Environments

- **Local:** developer machines.
- **Preview or staging:** every pull request or release candidate. Client review happens here.
- **Production:** deploy from the main branch only, after checks pass.

## Release steps

1. Complete [templates/deployment-checklist.md](../../templates/deployment-checklist.md).
2. Confirm backup or snapshot of production data (if any) and its timestamp.
3. Deploy at an agreed time. Avoid Friday evening and client peak hours. State the timezone (for example `WIB, UTC+7`).
4. Run smoke tests on production: home, priority journeys, forms, payments in test mode if possible.
5. Monitor errors and uptime for at least one hour.
6. Notify the client with what changed.

## Rollback

- Every release has a written rollback method before deploy: redeploy previous build, revert commit, or restore database snapshot.
- Database migrations that cannot be reversed need a separate plan and client approval.
- Decide rollback triggers in advance: for example, priority journey failure or error rate spike.

## DNS and domains

- Lower DNS TTL a day before a domain switch.
- Confirm who owns the domain registrar account. It should be the client.
- Set up HTTPS and redirects from old URLs (301) to preserve search traffic.

Never report a deployment as complete unless it ran and smoke tests passed.
