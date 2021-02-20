# toggle a blinking led with button push

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# declare variables and objects
led = DigitalInOut(board.A7)
led.direction = Direction.OUTPUT
ledMode = 0

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPre = False

blinkInterval = 0.5

# time.monotonic() always INCREASES! from program start
blinkTime = time.monotonic() + blinkInterval

# repeat this code forever
while True:
    # gather input
    # is the button CHANGED?
    if button.value != buttonPre:
        # save the button value for the next loop
        buttonPre = button.value
        # is the button pushed?
        if button.value:
            # increment the ledMode
            ledMode += 1
            # constrain the ledMode, lo op to 0
            if ledMode > 1:
                ledMode = 0

    # do output according to mode
    # is the ledMode 1?
    if ledMode == 1:
        if time.monotonic() >= blinkTime:
            print("blink")
            # toggle the led value
            led.value = not led.value
            # increment the time by blinkDelay
            blinkTime += blinkInterval
    else:
        # turn led off
        led.value = False
        # reset the blink time
        blinkTime = time.monotonic()

    # sleep for serial debug
    time.sleep(0.01)