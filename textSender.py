import asyncio
import websockets

nums = 0
reply = ""


# create handler for each connection
async def handler(websocket, path):
    global nums, reply
    while True:
        t2 = asyncio.create_task(websocket.recv())
        data = None
        try:
            data = await asyncio.wait_for(t2, timeout=2)
        except:
            await asyncio.sleep(1)
        if data and data == "T":
            print("Clearing")
            nums = 0
        if nums > 10:
            reply = "AAAA"
        else:
            reply = f"Hello {nums}"
        nums += 1
        print("sending " + reply)

        await websocket.send(reply)


message = False


async def text(websocket, path):
    global message
    while True:
        task = asyncio.create_task(websocket.recv())
        try:
            message = await asyncio.wait_for(task, timeout=2)
            print(message)
        except:
            pass
        await websocket.send(message)


start_server = websockets.serve(text, "localhost", 8000)


asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()
