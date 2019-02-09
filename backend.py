import Controller
import RPi.GPIO as GPIO

control = Controller.ArduinoController()

print("message")

control.North()
control.South()

control.StopNorthSouth()
control.StopEastWest()
GPIO.cleanup()

exit()