import asyncio
import sys
import os

sys.path.append(os.getcwd())
from notebooklm import NotebookLMClient

async def main():
    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            agent_notebook = next(nb for nb in notebooks if 'Diagram Agent Context' in (getattr(nb, 'title', None) or nb.get('title', '')))
            nb_id = getattr(agent_notebook, 'id', None) or agent_notebook.get('id')
            
            pergunta = "Com base exclusivamente no documento enviado sobre 'V2: Arquitetura com Design Patterns', quais são os Nomes dos Design Patterns utilizados e em quais componentes eles foram aplicados?"
            resposta = await client.chat.ask(nb_id, pergunta)
            texto_resposta = getattr(resposta, 'text', str(resposta))
            print(f"--- RESPOSTA DA IA ---\n{texto_resposta}\n----------------------")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(main())
