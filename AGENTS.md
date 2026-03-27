# Community Network Handbook — OpenCode Rules

This repository uses **OpenCode** conventions.

## Project Overview

This is a Community Network Handbook built with **Zensical**.
- Source content: `docs/`
- Site config: `mkdocs.yml`
- Build output: `public/`

Top-level handbook structure:
- `docs/1-Introduction/`
- `docs/2-Imaginary-Use-Case/`
- `docs/3-Guide/`
- `docs/4-Real-Use-Cases/`

Chapter 2 (story) and Chapter 3 (guide) must maintain a 1:1 mapping.

## Build Commands

Use Zensical commands only:
- `zensical build`
- `zensical serve`

Do not use `mkdocs serve` or `mkdocs build` directly for this project.

## Core Conventions

- Tone is practical, direct, and second-person.
- Use admonitions: `!!! tip`, `!!! warning`, `!!! info "Work in Progress"`.
- Use Mermaid code fences for diagrams.
- Images use co-located `images/` subfolders inside each section folder with `.webp` format and placeholder workflow (see `.opencode/rules/general.md`).
- Always update `mkdocs.yml` nav when adding/moving/removing docs files.

## OpenCode Agent Workflow

Use these project subagents:
- `@writer` for creating and expanding handbook content
- `@reviewer` for read-only quality reviews
- `@diagrams` for Mermaid diagrams
- `@structure` for structural refactors and nav sync
- `@consistency` for read-only audits

Use these custom commands:
- `/new-section`
- `/review-chapter`
- `/add-diagram`
- `/audit`
- `/guide-from-steps`

## External Rule Files (Load on demand)

When editing these targets, load and follow the corresponding rule file:
- Chapter 2 files: `@.opencode/rules/chapter2-story.md`
- Chapter 3 files: `@.opencode/rules/chapter3-guide.md`
- `mkdocs.yml`: `@.opencode/rules/mkdocs-nav.md`

General handbook rules: `@.opencode/rules/general.md`
