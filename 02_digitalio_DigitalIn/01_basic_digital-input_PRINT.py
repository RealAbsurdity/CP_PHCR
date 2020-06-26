# print the values of digigal inputs

# import modules and libraries
import board
from digitalio import DigitalInOut, Direction
import time

# declare switch digitalio object, set direction and pull
switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT

# repeat this code forever
while True:

    print(switch.value)
    time.sleep(0.1)