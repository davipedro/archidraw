---
name: rag_references
description: Consult the private context (references) of a project directly using NotebookLM RAG to obtain accurate architectural or technical answers grounded in the project's documentation.
---

# `rag_references` Skill

This skill allows you to query the private memory and documentation references of any project stored in the Google NotebookLM platform. It uses the `notebooklm-py` client under the hood.

## When to use this skill
- When the user asks a question about the reference architecture, design decisions, or context of a specific project.
- When you need to retrieve facts from project documentation that is not available in the local codebase but was uploaded to NotebookLM.
- When you want to isolate a query specifically to the reference material.

## How to use this skill

1. **Identify the Target**: Ensure you know the name of the notebook referencing the current project (e.g., "Diagram Agent Context", "Delivery App"). If unsure, you may first need to list the notebooks or ask the user.
2. **Formulate the Query**: Create a clear and concise question to ask the RAG engine.
3. **Execute the Script**: Run the provided Python script `scripts/query_rag.py` passing the notebook name and the query as arguments.

### Example Usage:

```bash
python src/skills/rag_references/scripts/query_rag.py "Diagram Agent Context" "Which design patterns were applied in the orchestrator?"
```

## Internal Scripts

- `scripts/query_rag.py "<notebook_name>" "<query>"`: Finds the notebook by name (fuzzy match) and asks the query. Returns the RAG answer.
