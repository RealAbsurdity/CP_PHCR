# blink an led without using delay

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction
import time

# declare variables and objects
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

blinkInterval = 0.5

# time.monotonic() always INCREASES! from program start
blinkTime = time.monotonic() + blinkInterval

# repeat this code forever
while True:

    # is it time to toggle the led?
    if time.monotonic() >= blinkTime:
        # YES! print debug output to the serial monitor
        print("The time is now: " + str(time.monotonic()))
        print("Time to change the led!")

        # toggle the led value
        led.value = not led.value

        # print the led value
        print("Led is " + str(led.value))

        # increment the by blinkDelay
        blinkTime += blinkInterval

        # print next time to blink
        print("The next blink will occur at " + str(blinkTime))