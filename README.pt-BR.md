[🇺🇸 English](README.md) | [🇧🇷 Português](README.pt-BR.md)

---

# ArchiDraw

> **⚠️ Nota: Versão 1 (Fase Inicial)**
> Esta é a versão inicial do projeto. A arquitetura central está definida e as skills base (incluindo a integração RAG com NotebookLM) são funcionais, mas o loop principal de orquestração do agente ainda está em desenvolvimento ativo.

**ArchiDraw**: Assistente inteligente para desenho de arquitetura de soluções, fundamentado em conceitos de referência e padrões específicos do projeto.

O ArchiDraw interpreta diagramas e desenhos técnicos para auxiliar arquitetos e desenvolvedores na iteração contínua de soluções super eficientes. Seguindo padrões modernos de mercado, sua arquitetura é baseada em **Skills** desacopladas (padrão `agentskills.io`), permitindo que a inteligência base do assistente seja agnóstica a provedores específicos de RAG ou busca de referências.

## Funcionalidades
- **Interpretação de Desenhos**: Entende e itera sobre diagramas técnicos (Excalidraw/Mermaid).
- **Fundamentação em Referências**: Baseia as soluções em Design Patterns e documentações de software maduras.
- **Integração RAG**: Conecta-se ao contexto privado do projeto consultando o Google NotebookLM.
- **Arquitetura Baseada em Skills**: Implementação modular e puramente desacoplada, focada em capacidades orientadas a objetivos.

## Skills Técnicas
- `research_context`: (MCP + RAG) - Pesquisa avançada de referências de mercado e contexto local.
- `design_architecture`: (Obsidian + MCP + RAG) - Estruturação de soluções e renderização visual.
- `rag_references`: (Apenas RAG) - Consulta direta à memória e documentação privada do projeto.

## Principais Tecnologias
Este projeto foi construído utilizando as seguintes tecnologias ferramentas centrais:
- **[notebooklm-py](https://github.com/mhamzaqayyum/notebooklm-py)**: Cliente não-oficial em Python para o Google NotebookLM, responsável por isolar a lógica de RAG e memória privada (`rag_references`).
- **Context7 (MCP)**: Servidor de Model Context Protocol utilizado para buscar padrões de mercado e documentações arquiteturais atualizadas.
- **Obsidian / Excalidraw**: Utilizado como tela (canvas) principal para criação e modificação fluida dos diagramas.
- **Python 3**: A linguagem backend responsável por fornecer as habilidades (skills) independentes.
