# see how break and else interact in a for loop
# written and tested on Adafruit Circuit Playground Express
# wire potentiometer with wiper pin to A1

import board
import neopixel
import analogio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# save a series of index values in a tuple
pixel_index = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

BLUE = (0, 0, 255)
RED = (255, 0, 0)

# create analogio object for KNOB
knob = analogio.AnalogIn(board.A1)

while True:
    # calculate the top pixel index value from the knob value
    level = int(knob.value / 63000 * 10)  # ranges 0 - 10
    print("Level is", level)

    # clear the pixel values before the for loop
    pixels.fill(0)
    # iterate over the pixel index
    for x in pixel_index:
        # make the index value pixel BLUE
        pixels[x] = (BLUE)
        # if the index value equals the level break
        if x == level:
            break
    else:  # no break
        # level value not found, fill RED
        print("Level not found, fill RED")
        pixels.fill(RED)

    pixels.show()
    time.sleep(0.01)

    # this demo is intended to demonstrate the use of else with for
    # there are faster ways to achieve the result of this code