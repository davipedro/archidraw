import asyncio
import sys
import os

sys.path.append(os.getcwd())
from notebooklm import NotebookLMClient

async def main():
    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            print("--- YOUR NOTEBOOKS (ON THE AGENT'S ACCOUNT) ---")
            for nb in notebooks:
                # In the current version, nb is an object with attributes.
                print(f"📖 {nb.title} (ID: {nb.id})")
            print("-----------------------------------------------")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
