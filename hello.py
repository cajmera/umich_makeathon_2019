import RPi.GPIO as gpio
import time

#Pin 14: W (Forward): Blue LED
#Pin 15: A (Left): Red LED
#Pin 18: S (Backward): Yellow LED
#Pin 23: D (Right): Green LED

FORWARD = 14
LEFT = 15
BACKWARD = 18
RIGHT = 23

Pins = [FORWARD, LEFT, BACKWARD, RIGHT]

gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)
gpio.output(14, False)
gpio.output(15, False)
gpio.output(18, False)
gpio.output(23, False)


name = "start"

def SwitchOn(PinNumber1, PinNumber2):
	for SomePin in Pins:
		if SomePin == PinNumber1:
			gpio.output(SomePin, True)
		elif SomePin == PinNumber2:
			gpio.output(SomePin, True)
		else:
			gpio.output(SomePin, False)

def AllOff():
	for SomePin in Pins:
		gpio.output(SomePin, False)

def Forward():
	SwitchOn(FORWARD, -1)

def Backward():
	SwitchOn(BACKWARD, -1)

def Right():
	SwitchOn(RIGHT, -1)

def Left():
	SwitchOn(LEFT, -1)

def ForwardRight():
	SwitchOn(FORWARD, RIGHT)

def ForwardLeft():
	SwitchOn(FORWARD, LEFT)

def BackwardLeft():
	SwitchOn(BACKWARD, LEFT)

def BackwardRight():
	SwitchOn(BACKWARD, RIGHT)

while name != exit:
	name = input("Enter command: ")
	
	if name == 'w':
		SwitchOn(FORWARD, -1)
	
	elif name == 'd':
		SwitchOn(RIGHT, -1)
	
	elif name == 's':
		SwitchOn(BACKWARD, -1)

	elif name == 'a':
		SwitchOn(LEFT, -1)

	elif name == "wa":
		SwitchOn(FORWARD, LEFT)

	elif name == "wd":
		SwitchOn(FORWARD, RIGHT)	

	elif name == "sa":
		SwitchOn(BACKWARD, LEFT)	

	elif name == "sd":
		SwitchOn(BACKWARD, RIGHT)	

	#b for break
	elif name == 'b':
		AllOff()

	elif name == 'q':
		print("Ending")
		gpio.cleanup()
		exit()

	elif name == "start":
		continue

	else:
		print("Directions are w, a, s, d (f, l, b, r)")



