# see how a break keyword can affect the flow of code in a for loop
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

# create analogio object for KNOB
knob = analogio.AnalogIn(board.A1)

while True:
    # calculate the top pixel index value from the knob value
    level = int(knob.value / 66000 * 10)  # ranges 0 - 9
    print("Level is", level)

    # iterate over the pixel index
    for x in pixel_index:
        print("Pixel is ", x)
        # if the index value is less than or eqaul to level, make pixel BLUE
        if x <= level:
            pixels[x] = BLUE
        # otherwise, turn it off and exit the loop
        else:
            pixels[x] = 0
            print("loop ends early")
            # why iterate through the whole list if you don't have to?
            break
    pixels.show()
    time.sleep(0.01)