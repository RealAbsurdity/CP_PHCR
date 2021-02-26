# import modules

import board
import time
import analogio
import neopixel
from simpleio import map_range

# declare neopixel object with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analog input object on pin A1
analog_in1 = analogio.AnalogIn(board.A1)
analog_in2 = analogio.AnalogIn(board.A2)

# create a color variable and fill the pixels with color
color = (0, 0, 0)
pixels.fill(color)

# repeat this code
while True:
    # gather input
    reading1 = analog_in1.value
    reading2 = analog_in2.value

    # do calculation: sscale 16-bit reading to 8-bit value
    scaled_val1 = map_range(reading1, 0, 65535, 0, 255)
    scaled_val2 = map_range(reading2, 0, 65535, 0, 255)
    # cast float scaled_val to int
    scaled_val1 = int(scaled_val1)
    scaled_val2 = int(scaled_val2)
    print(scaled_val1)
    print(scaled_val2)

    # set new color value
    color = (scaled_val2, 0, scaled_val2)

    # do output
    pixels.fill(color)
    brighness = (scaled_val1)

    # sleep to prevent buffer overrun
    time.sleep(0.2)