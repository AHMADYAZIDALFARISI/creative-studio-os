---
name: new-client-project
description: Create a new client project workspace from the studio template. Use when the user wants to start, set up, or bootstrap a new client project folder.
disable-model-invocation: true
---

# New client project

1. Ask for the client slug and display name if not given. The slug uses lowercase letters, numbers, and hyphens.
2. Run a dry run first and show the output:
   `python3 scripts/new_project.py <slug> --client "<Name>" --dry-run`
3. After the user confirms, run it without `--dry-run`.
4. Remind the user that real client folders belong in a private repository.
5. Point to the first stage document: `projects/<slug>/01-project-brief.md`.

If the script reports that the folder exists, stop. Never delete or overwrite an existing project.
