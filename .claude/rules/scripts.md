---
paths:
  - "scripts/**/*.py"
---

# Script rules

- Python 3.9+ standard library only. No third-party imports.
- Default behavior must be non-destructive. Writing operations need an explicit argument and refuse to overwrite existing files.
- Exit code 0 on success, 1 on validation failure, 2 on usage error.
- Every non-trivial function has a unit test in the matching `test_*.py` file.
- Print actionable messages: file path, problem, and how to fix it.
