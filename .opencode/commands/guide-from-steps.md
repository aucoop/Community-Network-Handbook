---
description: Build or update a Chapter 3 guide from user-provided executed steps
agent: writer
subtask: true
---
Create or update a Chapter 3 guide using user field steps from: $ARGUMENTS

Required behavior:
- Phase 1 (mandatory): produce a draft plan and questions before writing
- Command default: execute immediately after the plan in the same invocation
- If `$ARGUMENTS` contains `PLAN-ONLY`, return plan/questions only and do not edit files
- If critical data is missing and cannot be inferred, stop after plan with explicit blocking questions
- Treat user-provided executed steps as primary source material
- Normalize wording while preserving technical meaning and execution order
- Keep real commands/paths/values whenever possible
- Complete missing details proactively whenever they can be inferred or validated
- Use web research to validate versions, commands, flags, and current best practices
- Add warnings for risky/outdated steps and propose safer alternatives
- Add TODO markers only for details that are truly unknowable from user input, repository context, or reliable web sources
- Keep Chapter 2/Chapter 3 mapping and cross-links consistent
- Update `mkdocs.yml` nav and chapter indexes if files are created or moved

Plan output format:
- Target files and whether they are create/update
- Normalized step outline (from user field steps)
- Risks and proposed warnings
- Missing data required from user
