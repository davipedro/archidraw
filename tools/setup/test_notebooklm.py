import asyncio
import sys
import os

# Add the CWD to the path to ensure local packages are found (if any)
sys.path.append(os.getcwd())

from notebooklm import NotebookLMClient

async def main():
    print("🚀 Starting NotebookLM Connection Test (Private Context)...")
    
    try:
        # 1. Connects using the session saved in ~/.notebooklm/storage_state.json
        async with await NotebookLMClient.from_storage() as client:
            print("✅ Authentication successful with your dedicated account!")
            
            # 2. Lists existing Notebooks
            notebooks = await client.notebooks.list()
            print(f"📚 Found {len(notebooks)} notebooks in your account.")
            
            # 3. Let's create a test notebook for the Agent if it doesn't exist
            agent_notebook = None
            for nb in notebooks:
                # Modified to access attributes if it's an object
                title = getattr(nb, 'title', None) or (nb.get('title') if isinstance(nb, dict) else str(nb))
                if 'Diagram Agent Context' in title:
                    agent_notebook = nb
                    break
                    
            if not agent_notebook:
                print("📝 Creating a new notebook 'Diagram Agent Context'...")
                agent_notebook = await client.notebooks.create("Diagram Agent Context")
                print("✅ Notebook created successfully!")
            else:
                nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else "unknown")
                print(f"📖 Using existing notebook: Diagram Agent Context (ID: {nb_id})")

            # Safely fetching the ID
            nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else agent_notebook)
            
            # 4. Quick RAG Example: Ask something without context (The base model responds)
            print("\n🤖 Sending a test question to the RAG engine...")
            response = await client.chat.ask(nb_id, "What is the Facade architectural pattern?")
            
            print("\n--- 📝 NotebookLM Response ---")
            # Accessing the response text based on the typical library structure
            response_text = getattr(response, 'text', str(response))
            print(response_text)
            print("----------------------------------\n")
            
            print("🎯 Test finished! The connection (Facade Provider) is operational.")
            
    except Exception as e:
        print(f"❌ Error during the test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
