# read an analog input and smooth the value with a weight
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

# initialize average with first read of the knob.value
smooth_val = analog_in.value

def weightedSmooth(in_val, weight):
    # weight is a float value between 0.0 and 1.0
    # reference smooth_val as global variable
    global smooth_val
    # apply weight to the incoming value and apply remaining weight to average
    smooth_val = weight * in_val + ((1 - weight) * smooth_val)
    # return the new average
    return smooth_val

# create a color variable and fill the pixels with the color
color = (0, 0, 0)
pixels.fill(color)

# repeat this code forever
while True:
    # gather input
    reading = analog_in.value

    # do calculation: weightedSmooth() with the reading and a weight
    smooth_val = weightedSmooth(reading, 0.1)

    # do calculation: scale 16-bit reading to 8-bit value
    scaled_val = map_range(smooth_val, 0, 65535, 0, 255)
    # cast float scaled_val to int()
    scaled_val = int(scaled_val)

    print((reading, smooth_val, scaled_val))

    # set new color value
    color = (0, scaled_val, scaled_val)

    # do output
    pixels.fill(color)

    # sleep to prevent buffer overrun
    time.sleep(0.05)