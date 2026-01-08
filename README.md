# Community-Network-Handbook
A field guide to build community networks from scratch

This directory contains the source documentation for the project. The documentation is built using [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Prerequisites

- Python 3
- The virtual environment located at `docs/.venv` (created automatically if you followed the setup).

## Setup

If you haven't set up the environment yet, you can create the virtual environment and install dependencies:

```bash
# From the project root
python3 -m venv docs/.venv
docs/.venv/bin/pip install -r docs/requirements.txt
```

## Serving Locally

To preview the documentation as you write, serve it locally. The site will automatically refresh when you save changes.

```bash
# From the project root
docs/.venv/bin/mkdocs serve
```

Open your browser to `http://127.0.0.1:8000/`.

## Building

To build the static site (output to `public/`):

```bash
# From the project root
docs/.venv/bin/mkdocs build
```
