# blink an led without using delay

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# declare variables and objects
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
ledMode = 0

# make a digitalInOut object to read the onboard switches
button = DigitalInOut(board.D4)  # (D4, D5, or D7)
button.direction = Direction.INPUT
button.pull = Pull.DOWN  # D7 slide switch uses Pull.UP
buttonPre = False
buttonPressTime = 0

blinkInterval = 0.5

# time.monotonic() always INCREASES! from program start
blinkTime = time.monotonic() + blinkInterval

# repeat this code forever
while True:
    # gather inputs
    # see if the button has CHANGED
    if button.value != buttonPre:
        # reset the previous value
        buttonPre = button.value
        if button.value:
            # mark the time when the button is pushed
            buttonPressTime = time.monotonic()
        else:
            if time.monotonic() >= buttonPressTime + 1:
                ledMode = 0
            else:
                ledMode += 1
                if ledMode > 2:
                    ledMode = 0

    # do output based on mode
    if ledMode == 1:
        blinkInterval = 0.5
        # is it time to toggle the led?
        if time.monotonic() >= blinkTime:
            # blink
            print("blink")
            # toggle the led value
            led.value = not led.value
            # increment the by blinkDelay
            blinkTime += blinkInterval
    elif ledMode == 2:
        blinkInterval = 0.25
        # is it time to toggle the led?
        if time.monotonic() >= blinkTime:
            # blink
            print("blink")
            # toggle the led value
            led.value = not led.value
            # increment the by blinkDelay
            blinkTime += blinkInterval
    else:
        led.value = False
        blinkTime = time.monotonic()