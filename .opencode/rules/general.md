# General Handbook Rules

## Tone and Scope
- Practical content for real deployments in low-resource settings.
- Direct language, second-person voice.
- Actionable over academic.

## File and Structure Rules
- 4 chapters: 1-Intro, 2-Imaginary-Use-Case, 3-Guide, 4-Resources.
  - You will primarily work in Chapter 2 (stories) and Chapter 3 (guides).
- Each chapter has sections that is a folder.
  - Each section folder has an `index.md` and optionally other markdown files for guides, plus an `images/` subfolder for images.
- Naming:
  - For chapter 2 section folders: `{number}-{Descriptive-Title}`
  - For chapter 3 section folders: `{Kebab-Case-Name}`.

## Chapter Mapping
- Chapter 2 (story) and Chapter 3 (guide) must remain **1:1**.
- Adding or removing a section on one side requires mirroring on the other.
- Cross-links must exist in both directions (Ch2 → Ch3 and Ch3 → Ch2).

## WIP Conventions
Unfinished sections must include both:
- `!!! info "Work in Progress"`
- `<!-- TODO: ... -->`

## Diagrams
If a diagram is needed, use Mermaid fenced blocks:

```mermaid
flowchart TD
  A --> B
```

## Image Conventions

Images live in a co-located `images/` subfolder inside each section folder.

### Directory layout

```
docs/
  assets/
    placeholder.webp              # generic placeholder
  2-Imaginary-Use-Case/
    2.1-The-First-Router/
      images/
        2.1-router-front-panel.webp
        2.1.2-install-openwrt.webp
      2.1.2-Installing-OpenWrt.md
      index.md
  3-Guide/
    Flash-OpenWrt/
      images/
        sysupgrade-screen.webp
        Cudy-WR3000E-openwrt-login.webp
      Cudy-WR3000E.md
      index.md
```

### Naming convention

`{section}-{descriptive-kebab-case}.webp`

- Section prefix ties the image to its content.
  - For Chapter 2 guides, use the section number (e.g. `3.1`, `2.5.1`) as prefix.
  - For Chapter 3 guides, use the section/guide title (e.g. `Cudy-WR3000E`) as prefix.
- Examples: `2.1-router-front-panel.webp`, `Cudy-WR3000E-openwrt-login.webp`

### Reference patterns

**Standard:**
```markdown
![Zabbix dashboard showing host status](images/2.5-zabbix-dashboard.webp)
```

**With caption** (when contextually useful):
```markdown
<figure markdown="span">
  ![Router front panel](images/2.1-router-front-panel.webp)
  <figcaption>Front panel of the Huawei HG556a with ports labeled</figcaption>
</figure>
```
**With width constraint** (for screenshots, especially in Ch3):
```markdown
![OpenWrt LuCI login](images/3.1-luci-login.webp){ width="600" }
```

### Image Workflows

**Placeholder workflow** (when no image is available yet):
1. Choose the final filename: `{section}-{descriptive-kebab-case}.webp`
2. Create the `images/` directory if needed: `mkdir -p docs/<chapter>/<section>/images`
3. Copy placeholder: `cp docs/assets/placeholder.webp docs/<chapter>/<section>/images/<final-name>.webp`
4. Insert the markdown reference with descriptive alt text.
5. Add a TODO comment **above** the image:
```markdown
<!-- TODO: Replace placeholder image — screenshot of Zabbix host configuration dialog -->
![Zabbix host config](images/3.6-zabbix-add-host-dialog.webp)
```
6. Optionally wrap in `<figure>` with a caption.

**Provided image workflow** (when the user supplies an image):
1. Convert to WebP if not already (quality 85 is a good default):
   ```bash
   cwebp -q 85 <input> -o <final-name>.webp
   # or with ffmpeg if cwebp is not available:
   ffmpeg -i <input> -quality 85 <final-name>.webp
   ```
   If conversion fails or no image is available, fall back to the **placeholder workflow**.
2. Copy the image to the section's `images/` folder with the correct filename:
   ```bash
   cp <final-name>.webp docs/<chapter>/<section>/images/<final-name>.webp
   ```

## Navigation Sync
- Always update `mkdocs.yml` nav when adding, moving, or removing files.
- See `.opencode/rules/mkdocs-nav.md` for detailed nav rules.
