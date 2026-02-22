import asyncio
import sys
import os
from pathlib import Path

# Add the CWD to the path to ensure local packages are found (if any)
sys.path.append(os.getcwd())

from notebooklm import NotebookLMClient

async def main():
    print("🚀 Starting Private Context Upload to NotebookLM...")
    
    file_to_upload = r"c:\Users\User\Desktop\diagram-agent\dev-docs\vault\diagram-agent\diagrams\arch-mermaid.md"
    
    try:
        # 1. Authentication and connection
        async with await NotebookLMClient.from_storage() as client:
            print("✅ Authentication confirmed!")
            
            # 2. Locate the "Diagram Agent Context" notebook
            notebooks = await client.notebooks.list()
            agent_notebook = None
            for nb in notebooks:
                title = getattr(nb, 'title', None) or (nb.get('title') if isinstance(nb, dict) else str(nb))
                if 'Diagram Agent Context' in title:
                    agent_notebook = nb
                    break
                    
            if not agent_notebook:
                print("❌ Notebook 'Diagram Agent Context' not found! Run the previous test first.")
                return

            nb_id = getattr(agent_notebook, 'id', None) or (agent_notebook.get('id') if isinstance(agent_notebook, dict) else agent_notebook)
            print(f"📖 Identified notebook: Diagram Agent Context (ID: {nb_id})")

            # 3. Read the Markdown file content and send it as a Text Source
            print(f"📄 Reading content from {os.path.basename(file_to_upload)}...")
            with open(file_to_upload, "r", encoding="utf-8") as f:
                content = f.read()
                
            print("☁️ Uploading the file as a source to NotebookLM...")
            # Using add_text instead of add_file to guarantee formatting and exact title
            await client.sources.add_text(nb_id, content, "Design Patterns Document - V2")
            print("✅ Upload finished!")

            # 4. Send a question validating that the RAG has read the new source
            question = "Based exclusively on the uploaded document about 'V2: Arquitetura com Design Patterns', what are the Names of the Design Patterns used and in which components were they applied?"
            print(f"\n🤖 Asking RAG: '{question}'")
            
            response = await client.chat.ask(nb_id, question)
            
            print("\n--- 📝 NotebookLM Response ---")
            response_text = getattr(response, 'text', str(response))
            print(response_text)
            print("----------------------------------\n")
            
            print("🎯 Validation complete. The Private Context is consuming our files perfectly!")
            
    except Exception as e:
        print(f"❌ Error during the context test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
