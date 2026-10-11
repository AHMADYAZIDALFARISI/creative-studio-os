# States and Forms

**Purpose:** Make sure every interface handles real conditions, not only the happy path.

## Required states

| State | Must contain |
|---|---|
| Loading | Skeleton or spinner within 300ms; layout does not jump when content arrives |
| Empty | Why it is empty and the next action ("No orders yet. Create your first order.") |
| Error | What happened in plain language, what the user can do, and a retry when possible. No raw error codes alone. |
| Success | Confirmation of what changed, and what comes next |
| Disabled | Visibly disabled and, where possible, a reason ("Add an address to continue") |
| Partial | Some data failed to load; show what loaded and flag what did not |
| Permission denied | What the user lacks and who can grant it |

## Form rules

1. Persistent visible labels. Placeholder is never the label.
2. Mark optional fields, not required ones, when most fields are required. Be consistent in a project.
3. Correct input types and `autocomplete` values (email, tel, postal-code).
4. Validate on blur for format, on submit for completeness. Do not show errors before the user types.
5. Error text appears next to the field, linked with `aria-describedby`, and summarized at the top on submit for long forms.
6. Keep entered data after an error.
7. Phone fields accept local and international formats (for example `0812...` and `+62 812...`).
8. Submit button shows loading and prevents double submission.

## Common mistakes

- "Something went wrong" with no next step.
- Clearing the form after a server error.
- Disabled submit button with no explanation of what is missing.
