# Agents: Documentation

You are working inside the `docs/` tree. All user-facing guides live here.

## Subdirectories

| Directory | Contents | Agent instructions |
|-----------|----------|-------------------|
| [channels/](channels/) | Channel-specific advertising guides | [channels/AGENTS.md](channels/AGENTS.md) |
| [resources/](resources/) | Cross-cutting planning and compliance topics | [resources/AGENTS.md](resources/AGENTS.md) |
| [ad-templates/](ad-templates/) | Ad templates and design resources | [ad-templates/AGENTS.md](ad-templates/AGENTS.md) |
| [meta/](meta/) | Repository outline and community policy | [meta/AGENTS.md](meta/AGENTS.md) |

## Index

[README.md](README.md) points at the published site. Home and section indexes are generated at build time from the markdown files in each subdirectory. Do not hand-edit `index.md` files under `docs/`.

## Link conventions

Links between docs should be **relative to the current file**:

- From `docs/README.md` to a channel: `channels/SEA.md`
- From `docs/channels/SEA.md` to a resource: `../resources/ANALYTICS.md`
- From `docs/ad-templates/TEMPLATES.md` to a channel: `../channels/SOCIAL.md`

Links from the root [README.md](../README.md) use the `docs/` prefix (e.g. `docs/channels/SEA.md`).

## Adding a new page

1. Place the file in the correct subdirectory (`channels/`, `resources/`, or `ad-templates/`).
2. Start the file with an H1. Optional `<!-- nav_order: 20 -->` on the next line controls sidebar order.
3. Run validation from the repo root (see [CONTRIBUTING.md](../CONTRIBUTING.md)).

## Content standards

- One primary `#` heading per file matching the topic title.
- Use `##` and `###` for sections; keep hierarchy logical.
- End every file with a single trailing newline.
- External tool links (Google Ads, Meta, etc.) are welcome in "Tools and Resources" sections.
- Do not duplicate large blocks across files; cross-link instead.

## Parent context

Repo-wide agent instructions: [../AGENTS.md](../AGENTS.md)
