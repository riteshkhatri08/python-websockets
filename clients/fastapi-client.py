import asyncio
import websockets

async def websocket_client():
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from client!")
        response = await websocket.recv()
        print(response)

asyncio.run(websocket_client())