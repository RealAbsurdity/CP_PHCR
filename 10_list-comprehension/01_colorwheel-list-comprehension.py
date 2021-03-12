# Example of for loop using enumerate() function
# assigns tuple color values contained in colorList to pixels
# written and tested on Adafruit Circuit Playground Express

import board
import neopixel
import analogio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

"""
color_list = [(255, 0, 0), (227, 28, 0),
             (198, 57, 0), (170, 85, 0),
             (142, 113, 0), (113, 142, 0),
             (85, 170, 0), (57, 198, 0),
             (28, 227, 0), (0, 255, 0)]
"""

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)

color_list = [wheel(x) for x in range(0, 255, 26)]

print(color_list)

pixels.fill(0)

# create analogio object for KNOB
knob = analogio.AnalogIn(board.A1)

while True:
    # calculate the top pixel index value from the knob value
    level = int(knob.value / 66000 * 10)  # ranges 0 - 9
    print("Level is", level)

    pixels.fill(0)

    # write a color list to neopixels with for and enumerate()
    for index, color in enumerate(color_list, level):
        print(index, color)
        if index < 10:
            pixels[index] = color
        else:
            break

    pixels.show()
    color_list.append(color_list.pop(0))
    # change sleep time to speed or slow the animation effect
    time.sleep(0.01)