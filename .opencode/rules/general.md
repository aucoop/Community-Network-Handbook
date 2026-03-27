# General Handbook Rules

## Tone and Scope
- Write practical content for real deployments in low-resource settings.
- Prefer direct language and second-person voice.
- Keep advice actionable over academic.

## File and Structure Rules
- Sections with children use a folder with `index.md`.
- Single-page sections use a flat `.md` file.
- Naming style: `{number}-{Kebab-Case-Name}`.

## Chapter Mapping
- Chapter 2 (Imaginary Use Case) and Chapter 3 (Guide) must remain 1:1.
- If one side adds/removes a section, mirror the change on the other side.

## WIP Conventions
- Unfinished sections must include:
  - `!!! info "Work in Progress"`
  - `<!-- TODO: ... -->`

## Diagrams
- Use Mermaid fenced blocks:

```mermaid
flowchart TD
  A --> B
```

## Navigation Sync
- Always update `mkdocs.yml` nav to match files on disk.
