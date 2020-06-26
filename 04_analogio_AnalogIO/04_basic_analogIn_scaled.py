# read an analog input and print the value to serial
# also change the brightness the neopixels on board

# import modules and libraries
import board
import neopixel
import analogio
import time

# declare variables and objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0)

knob = analogio.AnalogIn(board.A1)

# define a function to scale and translate input value to output range
def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    # calculate incoming range
    inRange = inEnd - inStart
    # calculate a scale factor (percent) from the inVal in the inRange
    inProportion = inVal / inRange
    # calculate the output range
    outRange = outEnd - outStart
    # calculate a new value scaled to the outRange
    scaledOut = inProportion * outRange
    # add the scaledOut to outMin and return the value
    return scaledOut + outStart


pixels.fill((255, 255, 255))


# repeat this code forever
while True:
    # gather and scale input
    scaledValue = scaleAndTranslate(knob.value, 0, 65535, 0, 1)

    print(scaledValue)

    # do output based on mode
    pixels.brightness = scaledValue
    time.sleep(0.01)