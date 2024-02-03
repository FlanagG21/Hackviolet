import asyncio
import websockets
from twilio.rest import Client
textSent = False

async def text(websocket, path):
    message = await websocket.recv()
    if message and not textSent:
        await websocket.send("A fire alarm may be going off in your vicinity, check your suroundings")
        textSent = True
    elif not message:
        textSent = False 


start_server = websockets.serve(text, "localhost", 8000)

