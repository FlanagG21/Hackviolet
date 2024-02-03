import asyncio
import websockets


async def text(websocket, path):
    message = await websocket.recv()
    await websocket.send(message)


start_server = websockets.serve(text, "localhost", 8000)

