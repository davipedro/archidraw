import asyncio
from notebooklm import NotebookLMClient

async def inspect():
    try:
        async with await NotebookLMClient.from_storage() as client:
            print("Sources methods:", [m for m in dir(client.sources) if not m.startswith('_')])
    except Exception as e:
        print(e)

asyncio.run(inspect())
