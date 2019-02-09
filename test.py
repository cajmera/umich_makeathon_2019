import Controller
import RPi.GPIO as GPIO

control = Controller.ArduinoController()

Direction = None

print("w: Go Forward\n s: Go Backward\n a: Go Left\n d: Go Right")

while Direction != 'q':
    Direction = input("Current Direction: ")

    #North
    if Direction == 'w':
        control.North()

    #South
    if Direction == 's':
        control.South()

    #East
    if Direction == 'a':
        control.East()

    #West
    if Direction == 'd':
        control.West()

    #Stop Moving North/South
    if Direction == 'b':
        control.StopNorthSouth()

    #Stop Moving East/West
    if Direction == 't':
        control.StopEastWest()

    if Direction == 'q':
        control.StopNorthSouth()
        control.StopEastWest()
        GPIO.cleanup()
        print("Quitting")
        exit()