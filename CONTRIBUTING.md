# Contributing to Awesome Ads

We welcome contributions from the community! Follow these guidelines to help us improve the Awesome Ads repository.

## Repository structure

```
├── docs/
│   ├── channels/     # One guide per advertising channel
│   ├── resources/    # Cross-cutting topics (analytics, legal, FAQ, …)
│   ├── ad-templates/    # Template and design resources
│   └── meta/         # Repo documentation
├── .github/          # CI, Dependabot, issue/PR templates
└── scripts/          # Maintenance scripts (link checker)
```

Add new channel guides under `docs/channels/`. Add cross-cutting topics under `docs/resources/`. Update [docs/README.md](docs/README.md) and the root [README.md](README.md) when adding pages.

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
5. **Verify locally**
   ```bash
   npx markdownlint-cli2 "**/*.md"
   python scripts/check-internal-links.py
   python scripts/prepare-mkdocs.py
   mkdocs build --strict
   ```
6. **Commit and push**
   ```bash
   git commit -m "Description of your changes"
   git push origin your-branch-name
   ```
7. **Open a pull request** against `main`.

## Preview the site locally

Install MkDocs Material and serve the docs site:

```bash
pip install -r requirements-docs.txt
python scripts/prepare-mkdocs.py
mkdocs serve
```

Open [http://127.0.0.1:8000/Awesome-Ads/](http://127.0.0.1:8000/Awesome-Ads/) in your browser.

## Standards

- Write clear, accurate prose aimed at small-business readers.
- Use relative links so pages work on GitHub and GitHub Pages.
- End markdown files with a single trailing newline.
- Update the table of contents when adding or renaming pages.

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
