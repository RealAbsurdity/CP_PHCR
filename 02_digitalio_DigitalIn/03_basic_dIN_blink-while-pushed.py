# blink an led while a button is pushed

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# declare variables and objects
led = DigitalInOut(board.A7)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

blinkInterval = 0.5

# time.monotonic() always INCREASES! from program start
blinkTime = time.monotonic() + blinkInterval

# repeat this code forever
while True:

    # is the button pused?
    if button.value:
        # is it time to toggle the led?
        if time.monotonic() >= blinkTime:
            # YES! print debug output to the serial monitor
            print("blink")
            # toggle the led value
            led.value = not led.value
            # increment the time by blinkDelay
            blinkTime += blinkInterval
    else:
        led.value = False
        blinkTime = time.monotonic()

    # sleep for serial debug
    time.sleep(0.01)