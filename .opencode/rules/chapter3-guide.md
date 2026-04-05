# Chapter 3 Guide Rules

Applies to: `docs/3-Guide/**`

Chapter 3 contains step-by-step technical implementation guides. Each guide enables the reader to implement the solution described in the corresponding Chapter 2 story.

---

## Required Structure

Every guide must follow this order:

```
# Title (descriptive, instructional — never a question)
Scope statement (one sentence)
Chapter 2 cross-link
## What You'll Learn
## Prerequisites (optional)
## Used Versions (optional)
## Step-by-Step Implementation
## References
## Revision History
```

---

## Title

- Descriptive and instructional.
- Not phrased as a question.
- Example: `# Flash OpenWrt on a Cudy WR3000E`

## Scope Statement

One concise sentence immediately after the title explaining what the guide covers.

## Chapter 2 Cross-Link

Reference the corresponding Ch2 story near the beginning:
```markdown
This guide implements the concept introduced in
[Chapter 2 — The First Router](../../2-Imaginary-Use-Case/2.1-The-First-Router/index.md).
```

## What You'll Learn

- 3-5 bullet points.
- Focus on practical skills or outcomes.
- Do not repeat concepts already covered in Chapter 2.

## Prerequisites (Optional)

Include when prior setup or knowledge is required.

## Used Versions (Optional)

Include when specific software versions are critical for the guide.

## Step-by-Step Implementation

- Steps must be **numbered** with short imperative headings: `### 1. Install the firmware`
- **The main body text IS the actionable path.** A reader must be able to follow just the non-admonition text and know exactly what to do.
- Inside each step, write actions as **numbered sub-steps**, not prose paragraphs. Each line is one thing the reader does:
  ```markdown
  ### 3. Configure the firewall

  1. Open a shell on the server.
  2. Install `ufw`:

      ```bash
      sudo apt install ufw
      ```

  3. Allow the required ports:

      ```bash
      sudo ufw allow 80/tcp
      sudo ufw allow 443
      ```
  ```
- Use **bullet points** for field values or options within a sub-step (e.g., form fields to fill in).
- Use `→` only for **UI navigation paths** (e.g., **Datacenter → Node → System → Network**), never as action markers.
- **Context and explanations go in `!!! info` admonitions**, keeping them visually separate from actions. The reader can skip them and still complete the guide:
  ```markdown
  !!! info "Why wildcard records?"
      Netmaker runs several services that each need a hostname. A wildcard record covers all of them with a single DNS entry.
  ```
- Warnings (`!!! warning`) and tips (`!!! tip`) stay as admonitions too.
- Examples must be realistically runnable.

---

## User-Provided Steps

When the user provides steps they already executed (field notes, terminal history):

- Treat them as primary input. Preserve real execution order if it makes sense.
- Normalize wording into instructional steps without changing technical meaning.
- Keep original commands, paths, and values as much as possible. Only adjust if you consider them wrong or outdated.
- Infer missing details from context or web research first. Leave TODO only for truly unknowable values.

---

## Internet Research

Before writing a guide, search for up-to-date technical information:

- Prefer official documentation, GitHub repos, and technical RFCs.
- Ensure commands and examples match current tool versions.
- Use research to complete missing values — not just for references.

---

## Images

- Ch3 images are **technical**: screenshots, terminal output, UI dialogs, configuration panels.
- Add `{ width="600" }` for screenshots.
- Captions are optional — use when the image needs extra context.
- Follow the placeholder workflow and naming convention in `general.md`.

---

## References (Required)

```markdown
## References

- OpenWrt Documentation — https://openwrt.org/docs/start
- Zabbix Manual — https://www.zabbix.com/documentation
```

- Bullet points with resource name and link.
- Prefer official documentation.

---

## Revision History (Required)

```markdown
## Revision History

| Date       | Version | Changes                | Author           | Contributors                |
|------------|---------|------------------------|------------------|-----------------------------|
| 2026-03-23 | 1.0     | Initial guide creation | John Doe         | Alice Muller, Bob Paski     |
```

---

## Writing Style

- Direct, instructional, concise.
- Short paragraphs. Explain why each step exists.
- No narrative storytelling or concept explanations already in Ch2.
