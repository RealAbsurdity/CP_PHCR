# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare varialbes and objects
led = DigitalInOut(board.A1)
led.direction = Direction.OUTPUT

# loop forever
while True:
    # this is a new code block
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.5)

# this is outside of the while loop
