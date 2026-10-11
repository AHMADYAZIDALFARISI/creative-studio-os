# Component Decisions: Reuse, Compose, Customize, or Create

**Purpose:** Decide how to build each component without forcing every client into one library or aesthetic.

## Decision path

1. **Reuse** when an existing component meets the need with token changes only. Example: a button that only needs new colors and font.
2. **Compose** when two or more existing components combine to meet the need. Example: product card = media + text block + price + button.
3. **Customize** when an existing component needs a new variant or behavior that other projects may also use. Add the variant; do not fork.
4. **Create** when the component expresses something unique to this client or no existing component fits the interaction. Document why.

## Questions to ask

- Does the behavior already exist somewhere? Behavior is harder to rebuild than style.
- Is the difference visual (tokens) or structural (markup and logic)?
- Will a second client plausibly need this?
- Does a library component bring accessibility we would otherwise have to build (dialogs, menus, comboboxes)? Prefer proven accessible primitives for complex widgets.

## Record

| Component | Decision | Reason | Owner |
|---|---|---|---|
| Origin map card | Create | Expresses the client's sourcing story; no generic equivalent | {{NAME}} |

## Common mistakes

- Creating a custom dropdown when a native `<select>` works.
- Forcing a client's unique storytelling block into a generic card.
