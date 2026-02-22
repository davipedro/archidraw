[🇺🇸 English](README.md) | [🇧🇷 Português](README.pt-BR.md)

---

# ArchiDraw

> **⚠️ Note: Version 1 (Early Stage)**
> This is the initial version of the project. The core architecture is defined, and the base skills (including the NotebookLM RAG integration) are functional, but the main agent orchestration loop is still under active development.

**ArchiDraw**: AI-powered solution architecture assistant grounded in reference concepts and project-specific standards.

ArchiDraw interprets diagrams and technical drawings to assist architects and developers in the continuous iteration of effective solutions. Following modern market standards, its architecture is based on decoupled **Skills** (using the `agentskills.io` standard), allowing the assistant's core intelligence to be agnostic to specific RAG or reference search providers.

## Features
- **Drawing Interpretation**: Understands and iterates on technical diagrams (Excalidraw/Mermaid).
- **Reference Grounding**: Bases solutions on established software design patterns.
- **RAG Integration**: Connects to private project context via Google NotebookLM.
- **Skill-based Architecture**: Modular and decoupled implementation focused on goal-oriented capabilities.

## Technical Skills
- `research_context`: (MCP + RAG) - Advanced reference and context searching.
- `design_architecture`: (Obsidian + MCP + RAG) - Solution structuring and visualization.
- `rag_references`: (RAG Only) - Direct querying of private project memory.

## Core Technologies
This project was built using the following core technologies and libraries:
- **[notebooklm-py](https://github.com/mhamzaqayyum/notebooklm-py)**: An unofficial Python client for Google NotebookLM used to power the `rag_references` and private context capabilities.
- **Context7 (MCP)**: Model Context Protocol server used to fetch up-to-date market standards and architectural documentation.
- **Obsidian / Excalidraw**: Used as the primary canvas for diagram creation and modification.
- **Python 3**: The backend language powering the standalone skills.
