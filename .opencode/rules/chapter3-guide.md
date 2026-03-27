# Chapter 3 Guide Rules

**Applies to:** `docs/3-Guide/**`

## Purpose

Chapter 3 contains **step-by-step technical implementation guides** that translate the concepts introduced in Chapter 2 into **practical instructions that can be executed in a real environment**.

Each guide should enable the reader to **implement the solution described in the corresponding Chapter 2 story**.

---

# Required Structure

Every Chapter 3 guide must follow this structure in the same order:

```
H1 Title
Scope statement
Chapter 2 cross-link
## What You'll Learn
## Prerequisites (optional)
## Step-by-Step Implementation
## References
## Revision History
```

---

# Title (H1)

Rules:

* Must be **descriptive and instructional**
* Must **not be phrased as a question**
* Must clearly describe the implementation task

Example:

```
# Implement Request Validation Middleware in Express
```

---

# Scope Statement

Immediately after the title include **one concise sentence** explaining what the guide covers.

Example:

```
This guide shows how to implement reusable request validation middleware in an Express API.
```

---

# Chapter 2 Cross-Link

Every Chapter 3 guide must reference the **corresponding Chapter 2 story**.

Example:

```
This guide implements the concept introduced in
[Chapter 2 – Why Request Validation Matters](../2-Story/request-validation.md).
```

Rules:

* The link must appear near the beginning of the document
* A Chapter 3 guide **must not exist without a matching Chapter 2 story**

---

# What You'll Learn

Required section.

```
## What You'll Learn
```

Rules:

* 3–5 bullet points
* Focus on **practical skills or outcomes**
* Avoid conceptual explanations already covered in Chapter 2

Example:

* How middleware integrates into the Express request lifecycle
* How to validate incoming request payloads
* How to return structured validation errors

---

# Prerequisites (Optional)

Include this section when prior setup or knowledge is required.

```
## Prerequisites
```

Examples:

* Node.js installed
* A running Express project
* Basic knowledge of JavaScript modules

---

# Step-by-Step Implementation

Required section.

```
## Step-by-Step Implementation
```

Rules:

* Steps must be **numbered**
* Each step must include:

  * A short heading
  * Explanation of **why the step exists**
  * Code examples when applicable

Example:

```
### 1. Install the Validation Library
```

Guidelines:

* Keep explanations concise
* Prefer **clear instructions and code examples**
* Ensure examples are **realistically runnable**

---

# Internet Research Requirement

Before generating a guide, the agent **must search for up-to-date technical information**.

Rules:

* Prefer **official documentation**
* Avoid outdated APIs or deprecated libraries
* Ensure examples match **current tool versions**
* Validate syntax and best practices against reliable sources

Preferred sources:

* Official documentation
* GitHub repositories
* Technical RFCs
* Well-known technical blogs

---

# References (Required)

Every guide must include a references section listing the sources used during research.

```
## References
```

Rules:

* Use bullet points
* Include the resource name and link
* Prefer official documentation

Example:

```
## References

- Express Documentation — https://expressjs.com
- Zod Documentation — https://zod.dev
- Node.js HTTP API — https://nodejs.org/api/http.html
```

Purpose:

* Allow readers to verify information
* Provide additional learning resources
* Ensure technical accuracy

---

# Revision History (Required)

Every guide must include a revision history section.

```
## Revision History
```

Rules:

* Use a table format
* Record meaningful documentation updates

Example:

```
| Date | Version | Changes |
|-----|-----|-----|
| 2026-03-11 | 1.0 | Initial guide creation |
| 2026-03-15 | 1.1 | Updated examples to match latest library version |
```

---

# Writing Style

Guidelines:

* Direct
* Instructional
* Practical
* Concise

Rules:

* Avoid storytelling
* Use short paragraphs
* Explain **why each step exists**
* Prefer **code + explanation**

---

# Prohibited Content

Do not include:

* Long narrative storytelling
* Concept explanations already covered in Chapter 2
* Philosophical discussions
* New topics without a corresponding Chapter 2 story

---

# Content Integrity Rule

A Chapter 3 guide **must not be created unless a matching Chapter 2 story exists**.

Relationship model:

```
Chapter 2 → Concept / Story
Chapter 3 → Practical Implementation
```

If the Chapter 2 story does not exist, the agent must **create the story first or stop generation**.

