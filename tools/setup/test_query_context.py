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
            
            question = "Based exclusively on the uploaded document about 'V2: Arquitetura com Design Patterns', what are the Names of the Design Patterns used and in which components were they applied?"
            response = await client.chat.ask(nb_id, question)
            response_text = getattr(response, 'text', str(response))
            print(f"--- AI RESPONSE ---\n{response_text}\n----------------------")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
