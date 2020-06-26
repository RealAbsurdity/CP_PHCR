# use the slide switch to turn blink on or off

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction, Pull
import time

# declare variables and objects

# declare led digitalio object and set its direction
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# declare switch digitalio object, set direction and pull
switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


# repeat this code forever
while True:

    print(switch.value)
    led.value = switch.value

    time.sleep(0.1)