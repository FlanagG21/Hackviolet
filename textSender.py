import asyncio
import websockets
message = False


async def text(websocket, path):
    global message
    message = asyncio.wait_for(asyncio.create_task(websocket.recv()), timeout=2)
    await websocket.send(message)


start_server = websockets.serve(text, "localhost", 8000)

