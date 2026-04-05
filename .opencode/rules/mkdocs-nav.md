# mkdocs.yml Navigation Rules

Applies to: `mkdocs.yml`

## Nav Management
- `nav:` must reflect real files in `docs/`.
- Use short sidebar labels (2-4 words).
- Keep Chapter 2 sections grouped under YAML act comments (e.g. `# Act 1 — Getting Connected`). Place new sections under the appropriate act.

## 1:1 Mapping
- Every Ch2 topic must have a matching Ch3 topic in nav.
- Keep numbering and order coherent between chapters.

## Verification Checklist
After any nav edit, confirm:
- Every nav target path exists on disk.
- No docs files are orphaned outside nav.
- Ch2 and Ch3 mapping remains complete.
