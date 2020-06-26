# Write your code here :-)
# import modules
import board
from digitalio import DigitalInOut, Direction
import time

# declare objects and variables
led = DigitalInOut(board.A1)
led.direction = Direction.OUTPUT

# variables to control sleep time for blinking
onTime = 0.25
offTime = 0.5
onTime2 = 1.25

def morseSean(pulse):
    # reset the count variable
    count = 0
    # loop three times to pulse the led three times
    while count < 3:
        led.value = True
        if pulse == onTime:
            print("dot")
        else:
            print("dash")
        time.sleep(pulse)
        # turn the led off
        led.value = False
        time.sleep(offTime)
        count += 1
        print(count)


# loop forever
while True:

    morseSean(onTime)
    morseSean(onTime2)

    print("break")

    time.sleep(0.1)