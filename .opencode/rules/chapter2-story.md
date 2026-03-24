# Chapter 2 Story Rules

Applies to: `docs/2-Imaginary-Use-Case/**`

## Title Format
- Use an italicized challenge question as H1:
  - `# *"Challenge question"*`

## Content Style
- Narrative and conversational.
- Frame each section as a problem the protagonist faces.
- Explain why the challenge matters before naming the technology.

## Required Elements
- Story context (2-3 paragraphs)
- High-level solution overview (not detailed steps)
- Guide cross-link:

```markdown
!!! tip "Guide reference"
    For step-by-step instructions, see [Chapter 3.X — Topic](../3-Guide/3.X-Topic.md).
```

- WIP marker and TODO when incomplete.

## Images
- Images in Ch2 are **narrative and conceptual**: photos of sites, network topology overviews, scenario illustrations.
- Place images in the section's `images/` subfolder (see general rules for full convention).
- Use descriptive alt text that fits the story context.
- Captions (`<figure>`) are encouraged for photos that set the scene.
- Always use the placeholder workflow: copy `docs/assets/placeholder.webp` with the final filename, add a `<!-- TODO: Replace placeholder image — ... -->` comment.

## Do Not
- Do not write detailed implementation steps here.
- Do not create a Ch2 topic without a matching Ch3 guide.
