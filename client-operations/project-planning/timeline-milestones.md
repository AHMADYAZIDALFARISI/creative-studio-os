# Timeline and Milestones

**Purpose:** Plan dates that account for client dependencies and review time.
**Use when:** Writing the SOW and at kickoff. Update weekly.

## Planning rules

1. Plan backward from the launch date, then check forward from kickoff. If they do not meet, cut scope or move the date before signing.
2. Every client review gets its own row with a duration ({{N}} working days).
3. Mark dependencies on the client in a separate column.
4. Add buffer of 10-20% to build and QA. Do not hide it inside tasks.
5. Exclude public holidays for both sides. For Indonesian clients check the official national holiday and joint leave (cuti bersama) list for the year.
6. State the timezone in the header.

## Template

**Timezone:** {{TIMEZONE}} | **Kickoff:** {{YYYY-MM-DD}} | **Target launch:** {{YYYY-MM-DD}}

| # | Milestone | Owner | Start | End | Depends on | Client action needed | Status |
|---|---|---|---|---|---|---|---|
| M1 | Discovery complete | Studio | | | Interview held | Confirm summary | Not started |
| M2 | Direction approved | Client | | | M1 | Choose direction | Not started |
| M3 | Design approved | Client | | | M2, copy draft | Consolidated feedback | Not started |
| M4 | Content delivered | Client | | | | Final copy and images | Not started |
| M5 | Staging ready | Studio | | | M3, M4 | | Not started |
| M6 | UAT complete | Client | | | M5 | Test and report | Not started |
| M7 | Launch | Studio | | | M6, access | Go-live approval | Not started |
| M8 | Handover | Studio | | | M7 | Sign handover | Not started |

Status values: Not started, In progress, Waiting on client, Blocked, Done.

## Common mistakes

- Treating client review as zero days.
- Starting build before content exists, then redesigning around real copy.
