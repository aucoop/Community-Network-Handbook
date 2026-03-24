---
description: Create or update a handbook topic in both Chapter 2 and Chapter 3
agent: writer
subtask: true
---
Create or update a handbook topic from: $ARGUMENTS

Requirements:
- Phase 1 (mandatory): return a concise plan and clarifying questions first
- Command default: execute immediately after plan in the same invocation
- If `$ARGUMENTS` contains `PLAN-ONLY`, stop after the plan and do not edit files
- If blocking data is missing, stop after the plan with explicit blocking questions
- Add matching sections to both Ch2 and Ch3 if creating a new topic
- Add cross-links both ways
- Update `mkdocs.yml` nav if needed
- Update chapter index pages if needed
- Follow rules from `AGENTS.md` and `.opencode/rules/*.md`
- If user provided already-executed implementation steps, reuse them as source material for Ch3

Plan output format:
- Files to create/update
- Proposed section titles
- Proposed Ch2<->Ch3 mapping
- Open questions and assumptions