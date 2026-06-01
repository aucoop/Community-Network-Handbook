# Authoring with AI agents

This handbook's content is regularly written and reviewed with the help of AI agents. The agents know the project's conventions (tone, structure, admonition vocabulary, the 1:1 Story↔Guide mapping, image rules, *Used Versions* banners) and produce drafts that already match the house style. Using them is **recommended** for new content — it saves you reading every rule file before you start writing.

Every pull request is reviewed and merged by a human maintainer. Nothing is auto-merged.

## The agents

| Agent | What it's good for |
|---|---|
| `@writer` | Drafting and expanding handbook content. |
| `@reviewer` | Read-only quality review of a page or chapter. |
| `@diagrams` | Producing Mermaid diagrams for an existing page. |
| `@structure` | Structural refactors and nav sync (`mkdocs.yml`). |
| `@consistency` | Read-only cross-page audit (terminology, link health, tone). |

## The slash commands

| Command | What it does |
|---|---|
| `/new-section` | Scaffolds a new Guide topic or Story section with the right file layout, admonitions, and nav entry. |
| `/guide-from-steps` | Turns your raw step-by-step notes into a Guide topic that follows the project's recipe template. |
| `/review-chapter` | Full pass over a chapter — flags inconsistencies, gaps, and tone drift. |
| `/add-diagram` | Produces a Mermaid diagram for an existing page. |
| `/audit` | Repo-wide consistency check. |

## Tooling

The agent configuration lives in two parallel places, kept in sync:

- `.opencode/` — the project's primary tooling, [OpenCode](https://opencode.ai).
- `.claude/` — [Claude Code](https://claude.com/claude-code) configuration.

Pick whichever you already use. If you have neither installed, OpenCode is the default the project's maintainers run.

## Worked example: adding a new Guide topic from raw notes

You have a scratch file with your installation steps. You want it turned into a proper Guide topic.

1. **Drop your raw notes** into a scratch file, anywhere outside `docs/`. Keep it readable — bullet points, snippets, and short prose are fine.
2. **Run `/guide-from-steps`** pointing at the file. The agent produces a draft under `docs/3-Guide/<your-topic>/` with the recipe template, the *Used Versions* banner, and image placeholders.
3. **Fill in the blanks the agent flagged** — actual version numbers, real screenshots, environment-specific commands.
4. **Run `/review-chapter`** over the new file to catch obvious gaps and tone drift.
5. **Open a pull request.** A maintainer will review and either merge or ask for changes.

## Honest disclaimer

Agents draft; humans decide. If you are uncomfortable using AI tooling, you can contribute without it — the conventions are documented in [Contributing](index.md) and the [rule files under `.opencode/rules/`](https://github.com/aucoop/Community-Network-Handbook/tree/main/.opencode/rules) tell you everything an agent would know.
