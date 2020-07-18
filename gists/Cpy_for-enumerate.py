# Example of for loop using enumerate() function
# assigns tuple color values contained in colorList to pixels
# written and tested on Adafruit Circuit Playground Express

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

color_list = [(255, 0, 0), (227, 28, 0),
             (198, 57, 0), (170, 85, 0),
             (142, 113, 0), (113, 142, 0),
             (85, 170, 0), (57, 198, 0),
             (28, 227, 0), (0, 255, 0)]

pixels.fill(0)

while True:
    # write a color list to neopixels with for and enumerate()
    for index, color in enumerate(color_list):
        print(index, color)
        pixels[index] = color

    pixels.show()
    color_list.append(color_list.pop(0))
    # change sleep time to speed or slow the animation effect
    time.sleep(0.01)