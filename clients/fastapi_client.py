import asyncio
import websockets


async def websocket_client():
    message = input("Client :")
    uri = "ws://127.0.0.1:8000/ws"
    async with websockets.connect(uri) as websocket:
        while True and message != "exit_chat":
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Server: {response}")
            message = input("Client :")


def main():
    asyncio.run(websocket_client())
