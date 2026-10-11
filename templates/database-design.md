# Database Design: {{PROJECT_NAME}}

**How to use:** Fill before writing migrations. Guide: [database-guide.md](../engineering/database/database-guide.md).

**Engine:** {{ENGINE_AND_VERSION}} | **Hosting:** {{HOSTING}} | **Backups:** {{FREQUENCY_AND_RETENTION}}

## Entities
### {{TABLE_NAME}}
| Column | Type | Null | Default | Constraint | Notes |
|---|---|---|---|---|---|
| id | | no | | PK | |
| created_at | timestamptz | no | now() | | UTC |
| updated_at | timestamptz | no | now() | | UTC |

Indexes:
Relationships:

## Personal data inventory
| Table.column | Data type | Purpose | Retention | Access |
|---|---|---|---|---|

## Migration plan
## Recovery targets
Recovery point objective: {{RPO}} | Recovery time objective: {{RTO}} | Agreed with client on {{DATE}}
