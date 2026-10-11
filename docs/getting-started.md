# Getting Started

**Purpose:** Get a new team member productive in one sitting.
**Use when:** You join the studio or open this repo for the first time.

## 0. Make it yours (once per studio)

Create a **private** copy of this repository for your studio before adding any client folder. Keep the MIT license notice. Update `SECURITY.md` and the client templates with your studio's contacts.

## 1. Read these four files in order

1. [workflow-overview.md](workflow-overview.md): the eight stages from inquiry to retrospective.
2. [quality-standards.md](quality-standards.md): what "done" means here.
3. [../studio/creative-direction/anti-slop-audit.md](../studio/creative-direction/anti-slop-audit.md): how we reject generic output.
4. [../projects/examples/kopi-laras/README.md](../projects/examples/kopi-laras/README.md): one fictional project from brief to handover.

## 2. Know where things live

| Need | Location |
|---|---|
| A blank document to fill | `templates/` |
| How to do a task well | the matching domain folder (`studio/`, `design/`, `engineering/`, `ai/`) |
| Something you send to a client | `client-operations/` (EN and ID versions) |
| A live client workspace | `projects/<client-slug>/` in a private copy of this repo |

## 3. Start a project

```bash
python3 scripts/new_project.py acme-coffee --client "Acme Coffee"
```

The script copies `projects/_template/` and refuses to overwrite an existing folder. Details: [../projects/README.md](../projects/README.md).

## 4. Validate before you share

```bash
python3 scripts/validation/validate_repo.py
```

## Common mistakes

- Opening Google Stitch before the creative brief exists. Stitch amplifies a vague brief into a generic design.
- Copying the example project's visual direction. Copy its process only.
- Editing templates in place. Copy them into the project folder first.

**Next:** [workflow-overview.md](workflow-overview.md)
