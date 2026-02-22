# ArchiDraw

**ArchiDraw**: AI-powered solution architecture assistant grounded in reference concepts and project-specific standards.

O ArchiDraw interpreta diagramas e desenhos técnicos para auxiliar arquitetos e desenvolvedores na iteração contínua de soluções eficazes. Seguindo padrões modernos de mercado, sua arquitetura é baseada em **Skills** desacopladas, permitindo que a inteligência do assistente seja agnóstica a provedores específicos de RAG ou busca de referências.

## Features
- **Drawing Interpretation**: Understands and iterates on technical diagrams (Excalidraw/Mermaid).
- **Reference Grounding**: Bases solutions on established software design patterns.
- **RAG Integration**: Connects to private project context via Google NotebookLM.
- **Skill-based Architecture**: Modular and decoupled implementation focused on goal-oriented capabilities.

## Technical Skills
- `research_context`: (MCP + RAG) - Advanced reference and context searching.
- `design_architecture`: (Obsidian + MCP + RAG) - Solution structuring and visualization.
- `rag_references`: (RAG Only) - Direct querying of private project memory.
