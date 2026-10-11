# Database Guide

## Choosing

- Relational (PostgreSQL, MySQL) by default for business data with relationships.
- Document stores when data is truly document-shaped and relationships are few.
- Do not add a second database without a measured need.

## Schema design

1. List entities and relationships from the requirements.
2. Normalize first. Denormalize only for measured performance needs.
3. Every table: primary key, `created_at`, `updated_at` (UTC).
4. Use foreign keys and constraints. The database is the last line of validation.
5. Index columns used in filters, joins, and sort. Check with the query planner.
6. Soft delete only when there is a business need for recovery or audit.
7. Separate personal data where practical so access can be restricted and data deleted on request.

## Personal data

Indonesia's Personal Data Protection Law (UU No. 27 Tahun 2022) and, for EU users, the GDPR may apply. This guide is not legal advice. Flag personal data processing in the spec and ask the client to confirm their legal obligations with counsel.

## Migrations and backups

See [backend handbook](../backend/backend-handbook.md). Document the schema with [templates/database-design.md](../../templates/database-design.md).
