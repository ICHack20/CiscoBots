import matplotlib.pyplot as plt

import asyncio
import websockets

async def send_action(action, uri="ws://172.20.10.8:8765"):
    async with websockets.connect(uri) as websocket:
        await websocket.send(action)
        resp = await websocket.recv()

def key_press(event):
    if event.key == "up":
        print("send up")
        asyncio.get_event_loop().run_until_complete(send_action("forward"))
    elif event.key == "down":
        print("send down")
        asyncio.get_event_loop().run_until_complete(send_action("backward"))
    elif event.key == "right":
        print("send right")
        asyncio.get_event_loop().run_until_complete(send_action("right"))
    elif event.key == "left":
        print("send left")
        asyncio.get_event_loop().run_until_complete(send_action("left"))
    elif event.key == "q":
        print("ending")
        asyncio.get_event_loop().run_until_complete(send_action("q"))

def main():
    fig = plt.figure()
    fig.canvas.mpl_connect("key_press_event", key_press)
    plt.show()

if __name__=="__main__":
    main()
