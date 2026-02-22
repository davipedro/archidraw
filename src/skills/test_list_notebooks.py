import asyncio
import sys
import os

sys.path.append(os.getcwd())
from notebooklm import NotebookLMClient

async def main():
    try:
        async with await NotebookLMClient.from_storage() as client:
            notebooks = await client.notebooks.list()
            print("--- SEUS CADERNOS (NA CONTA DO AGENTE) ---")
            for nb in notebooks:
                # Na versão atual, nb é objeto com atributos.
                print(f"📖 {nb.title} (ID: {nb.id})")
            print("------------------------------------------")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    asyncio.run(main())
