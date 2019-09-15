import asyncio
import websockets
import time
import json

async def say_hello(websocket, path):
    while True:
        await websocket.send("hello world")
        time.sleep(10)

start_server = websockets.serve(say_hello,'localhost',4040)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


