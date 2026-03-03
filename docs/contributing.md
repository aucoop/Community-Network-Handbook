# Contributing

This handbook is open source and built to grow. Whether you're fixing a typo, adding a new guide section, or documenting a real-world deployment — your contribution is welcome.

## How to contribute

1. **Fork the repository** on GitHub
2. **Create a branch** for your changes
3. **Edit or add files** in the `docs/` folder (all content is Markdown)
4. **Submit a Pull Request** with a clear description of what you changed and why

## What you can contribute

- **Corrections** — fix typos, broken links, outdated information
- **Improvements** — clarify explanations, add diagrams, expand incomplete sections
- **New guide sections** — add step-by-step instructions for a technology (Chapter 3)
- **Real use cases** — document a community network deployment (Chapter 4)
- **Translations** — help make this handbook accessible in other languages

## Writing style

- **Be practical** — show how, not just why
- **Be direct** — use simple language, short sentences
- **Be honest** — share what didn't work, not just what did
- **Use admonitions** for tips (`!!! tip`), warnings (`!!! warning`), and notes (`!!! info`)
- **Link to the Guide** from the Imaginary Use Case, and vice versa

## Local development

```bash
# Clone the repo
git clone https://github.com/YOUR_ORG/Community-Network-Handbook.git
cd Community-Network-Handbook

# Create a virtual environment and install dependencies
python -m venv .venv
.venv/Scripts/activate  # Windows
# source .venv/bin/activate  # Linux/macOS
pip install -r docs/requirements.txt

# Serve locally
mkdocs serve
```

Then open `http://127.0.0.1:8000` in your browser.

## Questions?

Open an issue on GitHub — we're happy to help.
