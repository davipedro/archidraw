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

## Getting Started (Integrating into your Agent)

Because ArchiDraw uses the standard `agentskills.io` architecture, integrating it into any modern AI Agent (like Cline, Cursor, or Aider) is straightforward:

1. **Install Dependencies**:
   Ensure you have Python 3 installed, then install the required unofficial NotebookLM client:
   ```bash
   pip install notebooklm-py
   ```

2. **Authenticate NotebookLM**:
   Run the interactive login command so your agent can access your private notebooks:
   ```bash
   notebooklm login
   ```
   *(This will save the session cookies locally. This only needs to be done once per machine/expiration).*

3. **Mount the Skills**:
   Simply copy the `src/skills/` folder into your agent's workspace. Your AI Agent should be instructed to read the `SKILL.md` file inside each folder (`rag_references`, `research_context`, etc.) to understand **when** and **how** to execute the Python scripts.

4. **Feeding the Private Context (RAG)**:
   This feature allows the agent to search and interact with a highly specific RAG containing only the information you want it to follow.
   - A major advantage is that the context is already **pre-interpreted by NotebookLM's AI**. This drastically reduces the processing cost (tokens and reasoning time) for your primary agent.
   - You can combine various references (architectural docs, internal patterns, code snippets) into a single notebook to provide the agent with a unified, aligned vision of what needs to be built.
   - To add your sources, simply go to [notebooklm.google.com](https://notebooklm.google.com), open the notebook named `Diagram Agent Context` (or your configured name), and upload your files. The `rag_references` skill will instantly leverage this pre-processed knowledge.

5. **Verify Connection**:
   You can manually test if the environment is ready using the provided test scripts:
   ```bash
   python tools/setup/test_notebooklm.py
   ```
