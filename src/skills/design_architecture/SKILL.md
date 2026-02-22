---
name: design_architecture
description: Generate or modify software architecture diagrams in Obsidian (Excalidraw/Mermaid) based on researched context, reference patterns, and private RAG memory.
---

# `design_architecture` Skill

This is the core execution skill for the ArchiDraw agent. It uses the information gathered from other skills (such as `research_context` or `rag_references`) to actively create or update visual architectural artifacts in the Obsidian Vault.

## When to use this skill
- When the user specifically asks you to draw, update, or create an architecture diagram (e.g., in Mermaid or Excalidraw format).
- After you have gathered enough context to confidently propose a solution architecture.

## How to use this skill

Run the provided Python script `scripts/design.py` passing the target file path and the context you want to apply.

### Example Usage:

```bash
python src/skills/design_architecture/scripts/design.py "dev-docs/vault/diagram-agent/diagrams/new-diagram.md" "Complete context of the Delivery App using Microservices"
```

## Internal Scripts

- `scripts/design.py "<target_path>" "<context>"`: Orchestrates the creation or modification of the Excalidraw JSON or Mermaid Markdown files inside Obsidian.
