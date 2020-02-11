from gpiozero import Robot
from time import sleep

left_pins = (24,25)
right_pins = (18, 23)

robot = Robot(left_pins, right_pins)

while True:
	print("right")
	robot.value = (0, 1)
	sleep(2)
	print("left")
	robot.value = (1, 0)
	sleep(2)
	print("both")
	robot.value = (1, 1)
	sleep(2)
