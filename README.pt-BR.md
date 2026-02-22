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

## Como Usar (Integração no seu Agente)

Como o ArchiDraw utiliza a arquitetura padrão `agentskills.io`, integrá-lo a qualquer Agente de IA moderno (como Cline, Cursor ou Aider) é super direto:

1. **Instale as Dependências**:
   Garanta que você tem o Python 3 instalado, e então instale o client não-oficial do NotebookLM:
   ```bash
   pip install notebooklm-py
   ```

2. **Autentique no NotebookLM**:
   Rode o comando interativo de login para que o agente tenha acesso aos seus cadernos privados:
   ```bash
   notebooklm login
   ```
   *(Isso salvará os cookies de sessão localmente. Só precisa ser feito uma vez por máquina/expiração).*

3. **Incorpore as Skills**:
   Simplesmente copie a pasta `src/skills/` para o workspace do seu agente. O seu Agente de IA deve ser instruído a ler o arquivo `SKILL.md` dentro de cada pasta (`rag_references`, `research_context`, etc.) para entender **quando** e **como** executar os scripts Python.

4. **Alimentando o Contexto Privado (RAG)**:
   Para documentações arquiteturais, padrões locais ou dados privados da empresa que não existem publicamente via MCP (como Context7), você deve alimentar a sua instância do NotebookLM:
   - Acesse [notebooklm.google.com](https://notebooklm.google.com).
   - Crie ou abra o caderno chamado `Diagram Agent Context` (ou o nome que você configurar).
   - Faça upload dos seus PDFs, `.md` ou arquivos de texto com as regras locais. A skill `rag_references` imediatamente passará a ler e entender essas restrições ao desenhar soluções.

5. **Verifique a Conexão**:
   Você pode testar manualmente se o seu ambiente está pronto rodando os scripts de testes providenciados:
   ```bash
   python tools/setup/test_notebooklm.py
   ```
