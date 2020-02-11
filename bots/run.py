from gpiozero import Robot
from time import sleep

left_pins = (24, 25)
right_pins = (18, 23)

robot = Robot(left_pins, right_pins)

while True:
	x = input("left 1, right 2, forward 3, back 4")
	if x == 1:
		print("left")
		robot.value=(1,0)
	elif x == 2:
		print("right")
		robot.value=(0,1)
	elif x == 3:
		print("forward")
		robot.value=(1,1)
	elif x == 4:
		print("back")
		robot.value=(-1,-1)
