# Contributing to Awesome Ads

We welcome contributions from the community! Follow these guidelines to help us improve the Awesome Ads repository.

## Repository structure

```
├── docs/
│   ├── channels/     # One guide per advertising channel
│   ├── resources/    # Cross-cutting topics (analytics, legal, FAQ, …)
│   ├── ad-templates/ # Template and design resources
│   ├── meta/         # Repo documentation and community policy
│   ├── assets/       # Social preview card
│   └── stylesheets/  # Site theme (extra.css)
├── .github/          # CI, issue/PR templates
├── scripts/          # Build and validation scripts
└── overrides/        # Theme template overrides (social tags, page actions)
```

Add new channel guides under `docs/channels/`. Add cross-cutting topics under `docs/resources/`. The site nav is generated at build time from those folders. Start each page with an H1. Optional `<!-- nav_order: 20 -->` on the next line controls sidebar order.

After reviewing a guide and its sources, add or update `<!-- reviewed: YYYY-MM-DD -->` on a separate line after the H1, beside any `nav_order` comment. The site shows that date as “Last reviewed.” Missing, invalid, future and more-than-12-month-old review dates produce build preparation warnings.

## Prerequisites

To run the checks in step 5 you need:

- Python 3.12 (the version CI uses)
- Node.js, for `npx markdownlint-cli2`
- The site build tools: `pip install -r requirements-docs.txt -c constraints-docs.txt`
- Git, because the link checker reads the list of tracked files

## How to contribute

1. **Fork the repository** — [TMHSDigital/Awesome-Ads](https://github.com/TMHSDigital/Awesome-Ads)
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/Awesome-Ads.git
   cd Awesome-Ads
   ```
3. **Create a branch**
   ```bash
   git checkout -b your-branch-name
   ```
4. **Make your changes** — follow existing markdown style; keep links relative.
5. **Verify locally.** These are the same checks CI runs on your pull request. See [Prerequisites](#prerequisites) if a command is missing.
   ```bash
   npx markdownlint-cli2 "**/*.md"
   python -m unittest scripts.test_catalog scripts.test_check_internal_links
   python scripts/check-public-repo-hygiene.py
   python scripts/check-internal-links.py
   python scripts/prepare-mkdocs.py
   zensical build --strict -f mkdocs.gen.yml
   ```
6. **Commit and push**
   ```bash
   git commit -m "Description of your changes"
   git push origin your-branch-name
   ```
7. **Open a pull request** against `main`.

## Preview the site locally

The site is built with [Zensical](https://zensical.org/). Install it and serve the docs site:

```bash
pip install -r requirements-docs.txt -c constraints-docs.txt
python scripts/prepare-mkdocs.py
zensical serve -f mkdocs.gen.yml
```

Open the local URL printed by `zensical serve` (typically port 8000). Run `prepare-mkdocs.py` again after you add or rename a guide.

## Standards

- Write clear, accurate prose aimed at small-business readers.
- Publish a statistic, price, or benchmark only with a primary source (the platform, a regulator or the law, a company filing, or a dated report with a stated method), linked next to the figure with its date. If no primary source exists, give the guidance in words without a number. Put cost benchmarks in the table in `docs/resources/BUDGETING.md` and link to it.
- Use relative links so pages work on GitHub and GitHub Pages.
- End markdown files with a single trailing newline.
- The published site catalog is generated from the docs folders. Do not maintain another page list. The one exception is the guide tables in the root README, which a unit test keeps in sync: add a row there when you add a guide.

## Issues and bug reports

Use [Issues](https://github.com/TMHSDigital/Awesome-Ads/issues) for bugs and content gaps. Reference issue numbers in commits when fixing them:

```bash
git commit -m "Fixes #123: Description of the fix"
```

## Community guidelines

Follow our [Community Guidelines](docs/meta/COMMUNITY_GUIDELINES.md).

## Resources

- [GitHub Guides](https://guides.github.com/)
- [Open Source Guides](https://opensource.guide/)
- [Markdown Guide](https://www.markdownguide.org/)
