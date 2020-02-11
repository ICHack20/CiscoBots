import matplotlib.pyplot as plt

import asyncio
import websockets

class Control:
    def __init__(self, ip):
        self.ip = ip

    async def send_action(self, action):
        uri = f"ws://{self.ip}:8765"
        async with websockets.connect(uri) as websocket:
            await websocket.send(action)
            resp = await websocket.recv()

    def key_press(self, event):
        if event.key == "up":
            print("send up")
            asyncio.get_event_loop().run_until_complete(self.send_action("forward"))
        elif event.key == "down":
            print("send down")
            asyncio.get_event_loop().run_until_complete(self.send_action("backward"))
        elif event.key == "right":
            print("send right")
            asyncio.get_event_loop().run_until_complete(self.send_action("right"))
        elif event.key == "left":
            print("send left")
            asyncio.get_event_loop().run_until_complete(self.send_action("left"))
        elif event.key == "q":
            print("ending")
            asyncio.get_event_loop().run_until_complete(self.send_action("q"))

    def main(self, ip):
        fig = plt.figure()
        fig.canvas.mpl_connect("key_press_event", self.key_press)
        plt.show()

if __name__=="__main__":
    robot_to_control = input("enter 0 or 1:")
    robot_to_control = int(robot_to_control)

    f = open("ip.txt", "r")
    ip = f.readlines()[robot_to_control]
    f.close()
    print(ip)
    ip = ip.strip()
    c = Control(ip)
    c.main(ip)
