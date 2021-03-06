# read an analog input and print the value to serial
# use simpleio map_range function to map the 16bit value to 8bit range
# set neopixels color with the 8bit value

# import modules and libraries
import board
import neopixel
import analogio
import time
from simpleio import map_range

# declare neopixel object with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare analog input object on pin A1
analog_in = analogio.AnalogIn(board.A1)

# create a color variable and fill the pixels with the color
color = (0, 0, 0)
pixels.fill(color)

# repeat this code forever
while True:
    # gather input
    reading = analog_in.value

    # do calculation: scale 16-bit reading to 8-bit value
    scaled_val = map_range(reading, 0, 65535, 0, 255)
    # cast float scaled_val to int()
    scaled_val = int(scaled_val)
    print(scaled_val)

    # set new color value
    color = (0, scaled_val, scaled_val)

    # do output
    pixels.fill(color)

    # sleep to prevent buffer overrun
    time.sleep(0.1)