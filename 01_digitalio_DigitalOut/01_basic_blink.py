# import modules and libraries
import board
from digitalio import DigitalInOut, Direction
import time

# declare variables and objects
led = DigitalInOut(board.A1)
led.direction = Direction.OUTPUT

# repeat this code forever
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)