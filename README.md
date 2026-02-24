# Community-Network-Handbook
A field guide to build community networks from scratch

This directory contains the source documentation for the project. The documentation is built using [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

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

## Serving Locally

To preview the documentation as you write, serve it locally. The site will automatically refresh when you save changes.

```bash
# From the project root
.venv/bin/mkdocs serve
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\mkdocs.exe serve
```

Open your browser to `http://127.0.0.1:8000/`.

## Building

To build the static site (output to `public/`):

```bash
# From the project root
.venv/bin/mkdocs build
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\mkdocs.exe build
```
