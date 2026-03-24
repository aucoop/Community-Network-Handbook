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

## Image Conventions

All sections use a **folder with `index.md`** structure. Images live in a co-located `images/` subfolder inside each section folder.

### Directory layout

```
docs/
  assets/
    placeholder.webp              # generic placeholder (swapped by the author)
  2-Imaginary-Use-Case/
    2.1-The-First-Router/
      images/
        2.1-router-front-panel.webp
        2.1.1-hardware-comparison.webp
      index.md
      2.1.1-Choosing-Hardware.md
  3-Guide/
    3.1-Flash-OpenWrt/
      images/
        3.1-sysupgrade-screen.webp
      index.md
```

### Naming convention

`{section}-{descriptive-kebab-case}.webp`

- Section number prefix ties the image to its content.
- All lowercase kebab-case.
- Always `.webp` format.

Examples: `2.1-router-front-panel.webp`, `3.6-zabbix-add-host-dialog.webp`, `2.1.2-openwrt-sysupgrade-page.webp`

### Reference patterns

From any file inside the section folder, images are always at `images/{name}.webp`.

**Standard image:**
```markdown
![Zabbix dashboard showing host status](images/2.5-zabbix-dashboard.webp)
```

**Image with caption** (use when contextually useful):
```markdown
<figure markdown="span">
  ![Router front panel](images/2.1-router-front-panel.webp)
  <figcaption>Front panel of the Huawei HG556a with ports labeled</figcaption>
</figure>
```

**Image with width constraint** (recommended for screenshots):
```markdown
![OpenWrt LuCI login](images/3.1-luci-login.webp){ width="600" }
```

### Placeholder workflow

When inserting an image:

1. Choose the final filename: `{section}-{descriptive-kebab-case}.webp`
2. Create the `images/` directory if it does not exist.
3. Copy `docs/assets/placeholder.webp` into the section's `images/` folder with the final filename.
4. Insert the markdown reference with descriptive alt text.
5. Add a TODO comment **above** the image:

```markdown
<!-- TODO: Replace placeholder image — screenshot of Zabbix host configuration dialog -->
![Zabbix host config](images/3.6-zabbix-add-host-dialog.webp)
```

6. Optionally wrap in `<figure>` with a caption when contextually useful.

## Navigation Sync
- Always update `mkdocs.yml` nav to match files on disk.
