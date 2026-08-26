# Repository Outline: Awesome Ads

<!-- nav_order: 10 -->

Overview of how documentation is laid out and how the published site is generated.

## Layout

```
docs/
├── channels/     # Per-channel advertising guides
├── resources/    # Cross-cutting topics (analytics, legal, FAQ)
├── ad-templates/    # Ad template and design resources
└── meta/         # Repo documentation
```

Each user-facing guide is a markdown file in one of those folders. `AGENTS.md` files are agent instructions and are excluded from the site.

## How the site catalog is built

MkDocs does not keep a handwritten page list. At build time:

1. `scripts/prepare-mkdocs.py` scans the folders above and writes home and section indexes.
2. `scripts/mkdocs_hooks.py` builds the sidebar from the same scan.

Title comes from the first H1. Optional `<!-- nav_order: 20 -->` on the line after the H1 controls order. Files without `nav_order` sort last, then by title.

Adding a guide means adding the markdown file. Do not edit `mkdocs.yml` nav or regenerate indexes by hand.

## Contributing

See [Contributing Guidelines](https://github.com/TMHSDigital/Awesome-Ads/blob/main/CONTRIBUTING.md).

## Community guidelines

See [Community Guidelines](COMMUNITY_GUIDELINES.md).

## License

Apache License 2.0. See [LICENSE](https://github.com/TMHSDigital/Awesome-Ads/blob/main/LICENSE).
