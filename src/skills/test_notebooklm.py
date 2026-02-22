import asyncio
import sys
import os

# Adicionando o CWD ao path para garantir que pacotes locais sejam achados (se houver)
sys.path.append(os.getcwd())

from notebooklm import NotebookLMClient

async def main():
    print("🚀 Iniciando Teste de Conexão com NotebookLM (Contexto Privado)...")
    
    try:
        # 1. Conecta usando a sessão salva em ~/.notebooklm/storage_state.json
        async with await NotebookLMClient.from_storage() as client:
            print("✅ Autenticação bem-sucedida com sua conta dedicada!")
            
            # 2. Lista os Cadernos existentes
            notebooks = await client.notebooks.list()
            print(f"📚 Encontrados {len(notebooks)} cadernos na sua conta.")
            
            # 3. Vamos criar um caderno de teste para o Agente se ele não existir
            agent_notebook = None
            for nb in notebooks:
                # Modificado para acessar atributos se for objeto
                title = getattr(nb, 'title', None) or (nb.get('title') if isinstance(nb, dict) else str(nb))
                if 'Diagram Agent Context' in title:
                    agent_notebook = nb
                    break
                    
            if not agent_notebook:
                print("📝 Criando um novo caderno 'Diagram Agent Context'...")
                agent_notebook = await client.notebooks.create("Diagram Agent Context")
                print("✅ Caderno criado com sucesso!")
            else:
                nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else "desconhecido")
                print(f"📖 Usando caderno existente: Diagram Agent Context (ID: {nb_id})")

            # Pegando o ID de forma segura
            nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else agent_notebook)
            
            # 4. Exemplo Rápido de RAG: Perguntar algo sem contexto (O modelo base responde)
            print("\n🤖 Enviando pergunta de teste para o RAG engine...")
            resposta = await client.chat.ask(nb_id, "O que é o padrão arquitetural Facade?")
            
            print("\n--- 📝 Resposta do NotebookLM ---")
            # Acessando o texto da resposta baseado na estrutura típica da library
            texto_resposta = getattr(resposta, 'text', str(resposta))
            print(texto_resposta)
            print("----------------------------------\n")
            
            print("🎯 Teste finalizado! A conexão (Facade Provider) está operante.")
            
    except Exception as e:
        print(f"❌ Erro durante o teste: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
