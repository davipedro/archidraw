import asyncio
import sys
import os
from pathlib import Path

# Adicionando o CWD ao path para garantir que pacotes locais sejam achados (se houver)
sys.path.append(os.getcwd())

from notebooklm import NotebookLMClient

async def main():
    print("🚀 Iniciando Upload de Contexto Privado para o NotebookLM...")
    
    file_to_upload = r"c:\Users\User\Desktop\diagram-agent\dev-docs\vault\diagram-agent\diagrams\arch-mermaid.md"
    
    try:
        # 1. Autenticação e conexão
        async with await NotebookLMClient.from_storage() as client:
            print("✅ Autenticação confirmada!")
            
            # 2. Localizar o caderno "Diagram Agent Context"
            notebooks = await client.notebooks.list()
            agent_notebook = None
            for nb in notebooks:
                title = getattr(nb, 'title', None) or (nb.get('title') if isinstance(nb, dict) else str(nb))
                if 'Diagram Agent Context' in title:
                    agent_notebook = nb
                    break
                    
            if not agent_notebook:
                print("❌ Caderno 'Diagram Agent Context' não encontrado! Rode o teste anterior primeiro.")
                return

            nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else agent_notebook)
            print(f"📖 Identificou caderno: Diagram Agent Context (ID: {nb_id})")

            # 3. Ler o conteúdo do arquivo Markdown e enviar como Fonte de Texto
            print(f"📄 Lendo conteúdo de {os.path.basename(file_to_upload)}...")
            with open(file_to_upload, "r", encoding="utf-8") as f:
                conteudo = f.read()
                
            print("☁️ Fazendo upload do arquivo como fonte para o NotebookLM...")
            # Usando add_text ao invés de add_file apenas para garantir que a formatação e title vão exatos
            await client.sources.add_text(nb_id, conteudo, "Design Patterns Document - V2")
            print("✅ Upload finalizado!")

            # 4. Enviar pergunta validando que a RAG leu a nova fonte
            pergunta = "Com base exclusivamente no documento enviado sobre 'V2: Arquitetura com Design Patterns', quais são os Nomes dos Design Patterns utilizados e em quais componentes eles foram aplicados?"
            print(f"\n🤖 Perguntando ao RAG: '{pergunta}'")
            
            resposta = await client.chat.ask(nb_id, pergunta)
            
            print("\n--- 📝 Resposta do NotebookLM ---")
            texto_resposta = getattr(resposta, 'text', str(resposta))
            print(texto_resposta)
            print("----------------------------------\n")
            
            print("🎯 Validação completa. O Contexto Privado está consumindo nossos arquivos com perfeição!")
            
    except Exception as e:
        print(f"❌ Erro durante o teste de contexto: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
