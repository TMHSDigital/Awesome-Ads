# Agents: Documentation

You are working inside the `docs/` tree. All user-facing guides live here.

## Subdirectories

| Directory | Contents | Agent instructions |
|-----------|----------|-------------------|
| [channels/](channels/) | Channel-specific advertising guides | [channels/AGENTS.md](channels/AGENTS.md) |
| [resources/](resources/) | Cross-cutting planning and compliance topics | [resources/AGENTS.md](resources/AGENTS.md) |
| [templates/](templates/) | Ad templates and design resources | [templates/AGENTS.md](templates/AGENTS.md) |
| [meta/](meta/) | Repository outline and community policy | [meta/AGENTS.md](meta/AGENTS.md) |

## Index

[README.md](README.md) is the canonical table of contents for this folder. Keep it in sync when adding or removing pages.

## Link conventions

Links between docs should be **relative to the current file**:

- From `docs/README.md` to a channel: `channels/SEA.md`
- From `docs/channels/SEA.md` to a resource: `../resources/ANALYTICS.md`
- From `docs/templates/SOCIAL_MEDIA.md` to the hub: `TEMPLATES.md`

Links from the root [README.md](../README.md) use the `docs/` prefix (e.g. `docs/channels/SEA.md`).

## Adding a new page

1. Place the file in the correct subdirectory (`channels/`, `resources/`, or `templates/`).
2. Add an entry to [README.md](README.md).
3. Update the root [README.md](../README.md) if the page should appear on the landing page.
4. Update [meta/REPO_OUTLINE.md](meta/REPO_OUTLINE.md) for structural changes.
5. Run `python scripts/check-internal-links.py` from the repo root.

## Content standards

- One primary `#` heading per file matching the topic title.
- Use `##` and `###` for sections; keep hierarchy logical.
- End every file with a single trailing newline.
- External tool links (Google Ads, Meta, etc.) are welcome in "Tools and Resources" sections.
- Do not duplicate large blocks across files; cross-link instead.

## Parent context

Repo-wide agent instructions: [../AGENTS.md](../AGENTS.md)
