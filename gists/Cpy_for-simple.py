# count through pixels with a for loop
# written and tested on Adafruit Circuit Playground Express

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# save a series of index values in a tuple
pixel_index = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

BLUE = (0, 0, 255)
RED = (255, 0, 0)

while True:

    for x in pixel_index:
        pixels.fill(0)
        pixels[x] = BLUE
        time.sleep(1)

    pixels.fill(RED)
    time.sleep(1)