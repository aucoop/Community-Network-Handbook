# Community Network Handbook

**A practical, opinionated field guide to building community networks from scratch — even with limited resources.**

🌍 **Read it online:** <https://aucoop.github.io/Community-Network-Handbook/>
📄 **Download the PDF:** [latest release](https://github.com/aucoop/Community-Network-Handbook/releases/latest/download/Community-Network-Handbook.pdf)

## What this is

This repository holds the source of the **Community Network Handbook**, a living guide for anyone who wants to build and run a small community network — a school, a clinic, a community centre — where commercial internet doesn't reach.

It is based on almost two decades of deployments by [AUCOOP](https://aucoop.upc.edu), a student cooperation group at the UPC, with the [Hahatay Network](https://hahatay.network) in Senegal as its main source of accumulated experience, and was validated in the field at a primary school in Gochas, Namibia. The handbook is the deliverable of a UPC Master's thesis (software side) and its companion thesis (hardware side).

The guide is **opinionated** (one clear, mostly open-source stack), **practical** (how-to over why), and **living** (plain Markdown under Git — contributions are just pull requests).

## Structure

The content lives in `docs/` and is organized in four parts:

| Part | Folder | What it is |
|---|---|---|
| 1. Introduction | `docs/1-Introduction/` | Why the handbook exists and who it's for |
| 2. The Story of a Community Network | `docs/2-Imaginary-Use-Case/` | A story that builds a network step by step |
| 3. Guide | `docs/3-Guide/` | Self-contained technical recipes |
| 4. Real Use Cases | `docs/4-Real-Use-Cases/` | Field deployments (e.g. Namibia) |

Chapters 2 (story) and 3 (guide) mirror each other and are cross-linked throughout.

The documentation is built with [Zensical](https://zensical.org/), a modern static site generator by the creators of Material for MkDocs. Site config is `mkdocs.yml`; the build output goes to `public/`.

## Prerequisites

- Python 3
- A virtual environment located at `.venv`

## Setup

If you haven't set up the environment yet, create the virtual environment and install dependencies:

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

## Serving locally

To preview the documentation as you write, serve it locally. The site refreshes automatically when you save changes.

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

## Contributing

Contributions are welcome — corrections, clearer explanations, new guide sections, or your own deployment story. See the [Contributing guide](docs/contributing.md). Even without Git, you can edit any page directly from the **Edit this page** button on the published site.
