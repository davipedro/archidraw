import asyncio
import sys
import os

# Add project root to path for global imports if needed
sys.path.append(os.getcwd())
from notebooklm import NotebookLMClient

async def query_notebook(notebook_name: str, query: str):
    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            
            # Simple fuzzy match by name
            target_nb = None
            for nb in notebooks:
                title = getattr(nb, 'title', None) or nb.get('title', '')
                if notebook_name.lower() in title.lower():
                    target_nb = nb
                    break
                    
            if not target_nb:
                print(f"❌ Error: Notebook '{notebook_name}' not found.")
                print("Available notebooks:")
                for nb in notebooks:
                    title = getattr(nb, 'title', None) or nb.get('title', '')
                    print(f" - {title}")
                return

            nb_id = getattr(target_nb, 'id', None) or target_nb.get('id')
            
            # Ask the question
            response = await client.chat.ask(nb_id, query)
            response_text = getattr(response, 'text', str(response))
            
            print(response_text)
            
    except Exception as e:
        print(f"❌ Error executing RAG query: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python query_rag.py \"<Notebook Name>\" \"<Your Question>\"")
        sys.exit(1)
        
    nb_name = sys.argv[1]
    question = sys.argv[2]
    
    # Silence unnecessary warnings/logs so the output is clean
    asyncio.run(query_notebook(nb_name, question))
