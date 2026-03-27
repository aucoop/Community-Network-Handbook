# Community-Network-Handbook
A field guide to build community networks from scratch

This directory contains the source documentation for the project. The documentation is built using [Zensical](https://zensical.org/), a modern static site generator by the creators of Material for MkDocs.

## Prerequisites

- Python 3
- A virtual environment located at `.venv`

## Setup

If you haven't set up the environment yet, you can create the virtual environment and install dependencies:

```bash
# From the project root
python3 -m venv .venv
.venv/bin/pip install -r docs/requirements.txt
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\pip install -r docs\requirements.txt
```

Recommended for anyone contributing changes:

```bash
.venv/bin/pip install pre-commit
.venv/bin/pre-commit install
```

This installs the local commit hook that blocks non-WebP images inside `docs/`.

## Serving Locally

To preview the documentation as you write, serve it locally. The site will automatically refresh when you save changes.

```bash
# From the project root
.venv/bin/zensical serve
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\zensical.exe serve
```

Open your browser to `http://127.0.0.1:8000/`.

## Building

To build the static site (output to `public/`):

```bash
# From the project root
.venv/bin/zensical build
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\zensical.exe build
```

## Image Policy

Images committed under `docs/` must use the `.webp` format.

This rule is enforced in two places:

- Locally, through `pre-commit`, so contributors get feedback before creating a commit
- In GitHub Actions, so pull requests and pushes fail if non-WebP docs images slip through

If you add screenshots or illustrations to the handbook, convert them to `.webp` before committing them.
