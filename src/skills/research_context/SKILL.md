---
name: research_context
description: Search for documentation, architectural patterns, and private context using a combination of external MCP (Context7) and internal RAG (NotebookLM).
---

# `research_context` Skill

This is a composite skill designed to gather comprehensive research about a specific technical topic or architectural decision. It abstracts the complexity of deciding where to search by querying both external market standards and internal project documentation.

## When to use this skill
- When you need to understand how to implement a specific feature.
- When you need to cross-reference market standards (Context7 docs) with the project's internal decisions (NotebookLM).
- When asked to "research", "find", or "learn" about a topic relevant to the solution.

## How to use this skill

Run the provided Python script `scripts/research.py` passing the target query.

### Example Usage:

```bash
python src/skills/research_context/scripts/research.py "How to implement JWT authentication in Next.js considering the rules in the Delivery App notebook"
```

## Internal Scripts

- `scripts/research.py "<query>"`: Orchestrates the search using MCP Context7 for public docs and NotebookLM API for private docs.
