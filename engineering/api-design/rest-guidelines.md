# REST API Guidelines

## Resources and methods

- Plural nouns: `/orders`, `/orders/{id}`, `/orders/{id}/items`.
- `GET` reads, `POST` creates, `PATCH` partially updates, `PUT` replaces, `DELETE` removes.
- No verbs in paths, except for clear actions that are not CRUD: `POST /orders/{id}/cancel`.

## Requests and responses

- JSON with `camelCase` fields, or `snake_case`, chosen once per project.
- Dates in ISO 8601 with offset: `2026-10-12T09:30:00+07:00`. Store in UTC.
- Money as integers plus an ISO 4217 currency code: `{ "amount": 125000, "currency": "IDR" }`. ISO 4217 assigns IDR two decimal places, but retail prices are normally whole rupiah. Choose "whole units" or "minor units" once per project, write it in the API contract, and never mix them.
- Pagination: cursor-based for large or changing lists, `?limit=20&cursor=...`.

## Error format

```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Email is not valid.",
    "details": [{ "field": "email", "issue": "format" }],
    "requestId": "req_7f3a"
  }
}
```

## Status codes

200 OK, 201 Created, 204 No Content, 400 Bad Request (malformed JSON or wrong types), 401 Unauthenticated, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Content (well-formed request that fails validation rules, code `VALIDATION_FAILED`), 429 Too Many Requests, 500 Server Error.

## Versioning

Version in the path (`/v1/`) for public APIs. Add fields without breaking; never repurpose a field.

## Contract

Write the contract in [templates/api-contract.md](../../templates/api-contract.md) before building. Frontend and backend agree on it.
