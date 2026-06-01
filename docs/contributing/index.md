# Contributing

This handbook is open source and built to grow. Whether you're fixing a typo, adding a new Guide section, or documenting a real-world deployment — your contribution is welcome.

The source lives at [github.com/aucoop/Community-Network-Handbook](https://github.com/aucoop/Community-Network-Handbook). All content is plain Markdown under `docs/`. Direct edits to `main` are blocked; everything goes through pull requests.

## Three ways to contribute

### Tiny fix (30 seconds)

Typos, broken links, outdated text.

1. Open the page in the published handbook.
2. Click the **Edit this page** button at the top right.
3. GitHub opens the source in its web editor.
4. Make the change and follow GitHub's prompts to open a pull request.

No local setup needed. This is the easiest path if you don't already work with Git locally.

### New content (recommended path)

A new Guide topic, an expansion of the Story, fixing a stub.

**The recommended path is the AI-agent workflow** — the project's agents know the handbook's tone, structure, and conventions, and produce drafts that pass review faster. See **[Authoring with AI agents](authoring-with-agents.md)** for a worked example.

If you'd rather write by hand, the conventions are listed below and the same fork → branch → PR flow applies.

### Real-world case study

A community network you've actually deployed.

See **[Case study template](case-study.md)** for the structure and a checklist.

## Conventions

These apply to any new or rewritten content, whether you use the agents or write by hand.

- **Story ↔ Guide stay in sync.** Chapter 2 (the Story) and Chapter 3 (the Guide) maintain a 1:1 mapping. When you add a Story section that introduces a technology, add or extend the corresponding Guide topic.
- **Images.** Co-located `images/` subfolder inside each section folder, `.webp` format.
- **Admonitions.** `!!! tip` for advice, `!!! warning` for things that can break, `!!! info` for context and works-in-progress.
- **Used Versions table.** Each Guide topic carries a *Used Versions* table at the top. Keep it updated when you test against a new version.
- **Nav.** Update `mkdocs.yml` when you add, move, or remove a page.
- **Tone.** Practical, direct, second-person. Show how, not just why. Be honest about what didn't work, not just what did.

The project's full conventions live in [`.opencode/rules/general.md`](https://github.com/aucoop/Community-Network-Handbook/blob/main/.opencode/rules/general.md) and the per-chapter rule files alongside it.

## Local development

To preview the site locally with live reload:

```bash
# Clone
git clone https://github.com/aucoop/Community-Network-Handbook.git
cd Community-Network-Handbook

# Create a Python virtual environment
python -m venv .venv

# Activate it
# Linux / macOS:
source .venv/bin/activate
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r docs/requirements.txt

# Serve with live reload
zensical serve
```

Open `http://127.0.0.1:8000/` in your browser. Edits to any `docs/` file refresh the page automatically.

## Pull request review

All pull requests are reviewed by a maintainer before merging. Expect a back-and-forth — most PRs go through one or two rounds of feedback before they land. We try to be timely; nudge us in the PR if a week goes by without a response.

## Questions?

[Open an issue on GitHub](https://github.com/aucoop/Community-Network-Handbook/issues/new) — we're happy to help.
