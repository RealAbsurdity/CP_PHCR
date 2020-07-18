# see how a continue keyword affects the flow of code in a for loop
# written and tested on Adafruit Circuit Playground Express
# wire potentiometer with wiper pin to A1

import board
import neopixel
import analogio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write = False)

# save a series of index values in a tuple
pixel_index = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

BLUE = (0, 0, 255)
RED = (255, 0, 0)

# create analogio object for KNOB
knob = analogio.AnalogIn(board.A1)

while True:
    # calculate a pixel index value from the knob value
    level = int(knob.value / 66000 * 10)  # ranges 0 - 9
    print("Level is", level)

    # iterate through the pixel_index
    for x in pixel_index:
        print("Pixel is ", x)
        # if index equals level make it red and skip the reest
        if x == level:
            print("Pixel", x, "is RED")
            pixels[x] = RED
            continue
        # make index value blue
        pixels[x] = BLUE
    pixels.show()

    time.sleep(0.01)