# Handover and Maintenance

**Purpose:** Transfer ownership cleanly and recommend realistic maintenance.
**Use with:** [templates/project-handover.md](../../templates/project-handover.md) (fill per project).

## Handover steps

1. **Access transfer.** Confirm the client owns domain, hosting, analytics, CMS admin, repository, and third-party accounts. Remove studio personal accounts or downgrade them to agreed roles. Transfer credentials only through the client's password manager or provider invitations.
2. **Documentation.** Deliver the handover document: architecture, how to edit content, how to deploy, environment variable names (no values), backups, contacts.
3. **Training.** Record a session on content editing and common tasks. Share the recording link.
4. **Warranty period.** State it from the contract ({{N}} days): which defects are covered, how to report.
5. **Sign-off.** Client signs the handover checklist.
6. **Retrospective.** Run the internal retro within one week using [templates/retrospective.md](../../templates/retrospective.md).

## Maintenance recommendations

Recommend based on the stack. Do not promise uptime numbers the hosting plan cannot support.

| Area | Recommended frequency | Owner options |
|---|---|---|
| CMS, plugin, and dependency updates | Monthly; immediately for security releases | Client team or studio retainer |
| Backup restore test | Quarterly | Hosting provider + owner |
| Domain and SSL renewal check | 60 days before expiry | Client |
| Accessibility and performance spot check | Quarterly or after major content changes | Studio retainer |
| Content review | Quarterly | Client |

## Maintenance offer: one paragraph (EN)
> After the warranty period, we offer a monthly maintenance plan covering updates, monitoring, backups, and {{N}} hours of small changes. Unused hours do not roll over. Response time: {{TIME}} on working days ({{TIMEZONE}}).

## Penawaran pemeliharaan (ID)
> Setelah masa garansi, kami menawarkan paket pemeliharaan bulanan yang mencakup pembaruan, pemantauan, backup, dan {{N}} jam perubahan kecil. Jam yang tidak terpakai tidak diakumulasi. Waktu respons: {{WAKTU}} pada hari kerja (WIB).
