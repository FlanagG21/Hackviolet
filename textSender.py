import asyncio
import websockets
from twilio.rest import Client

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

async def sender():
    client = Client(authSid, authKey)
    message = client.messages \
    .create(
         body='There may be a fire alarm going off in your vicinity, please check your suroundings',
         from_='+18446992585',
         to='+7039096770'
     )
    print(message.sid)


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

authSid = input("enter your user sid:")
authKey = input("enter your authorization token:")
start_server = websockets.serve(text, "localhost", 8000)


asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_forever()