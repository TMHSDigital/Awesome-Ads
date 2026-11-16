# Repository Outline: Awesome Ads

<!-- nav_order: 10 -->

Overview of how documentation is laid out and how the published site is generated.

## Layout

```
docs/
├── channels/     # Per-channel advertising guides
├── resources/    # Cross-cutting topics (analytics, legal, FAQ, glossary)
├── ad-templates/ # Ad template and design resources
├── meta/         # Repo documentation
├── assets/       # Social preview card
└── stylesheets/  # Site theme (extra.css)
overrides/        # Theme template overrides
scripts/          # Site generation and validation scripts
```

Each user-facing guide is a markdown file in one of the first four folders. `AGENTS.md` files are agent instructions and are excluded from the site.

## How the site catalog is built

The site is built with [Zensical](https://zensical.org/), and there is no handwritten page list. Before each build, `scripts/prepare-mkdocs.py` scans the folders above and writes:

1. The home and section index pages.
2. `docs/CONTRIBUTING.md`, a copy of the root `CONTRIBUTING.md` with its links adjusted for the site.
3. `mkdocs.gen.yml`, which is `mkdocs.yml` plus the sidebar built from the same scan. The build reads this file.

Title comes from the first H1. Optional `<!-- nav_order: 20 -->` on the line after the H1 controls order. Files without `nav_order` sort last, then by title.

Adding a guide means adding the markdown file. Do not add a nav to `mkdocs.yml`, edit `mkdocs.gen.yml`, or regenerate indexes by hand.

## Contributing

See [Contributing Guidelines](https://github.com/TMHSDigital/Awesome-Ads/blob/main/CONTRIBUTING.md).

## Community guidelines

See [Community Guidelines](COMMUNITY_GUIDELINES.md).

## License

Apache License 2.0. See [LICENSE](https://github.com/TMHSDigital/Awesome-Ads/blob/main/LICENSE).
