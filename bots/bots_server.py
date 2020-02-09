## needs to be added to start up

import asyncio
import websockets

actions = {
    "forward": (1, 1),
    "backward": (-1, -1),
    "right": (0, 1),
    "left": (1, 0),
}

from gpiozero import Robot

left_pins = (24, 25)
right_pins = (18, 23)

robot = Robot(left_pins, right_pins)

run_robot = False

async def control(websocket, path):
    action = await websocket.recv()
    print(f"< {action}")
    
    valid_move = False
    

    if action == "forward":
        print("going forward")
        valid_move = True
    elif action == "backward":
        print("going backward")
        valid_move = True
    elif action == "right":
        print("going right")
        valid_move = True
    elif action == "left":
        print("going left")
        valid_move = True
    
    if valid_move and run_robot:
        robot.value = actions[action]

    resp = f"{action}"
    await websocket.send(resp)
    print(f"> {resp}")

start_server = websockets.serve(control, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
