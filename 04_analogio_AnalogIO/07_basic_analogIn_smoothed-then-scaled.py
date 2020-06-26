# read an analog input and print the value to serial
# also change the brightness the neopixels on board

# import modules and libraries
import board
import neopixel
import analogio
import time

# declare variables and objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)

knob = analogio.AnalogIn(board.A1)

# initialize average with first read of the knob.value
average = knob.value

def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    # calculate incoming range
    inRange = inEnd - inStart
    # calculate a scale factor (percent) from the inVal in the inRange
    inProportion = inVal / inRange
    # calculate the output range
    outRange = outStart - outEnd
    # calculate a new value scaled to the outRange
    scaledOut = inProportion * outRange
    # add the scaledOut to outMin and return the value
    return scaledOut + outStart

def expSmooth(inVal, weight):
    # declare average as global
    global average
    # apply weight to the incoming value and apply remaining weight to average
    average = weight * inVal + ((1 - weight) * average)
    # print touple of inval and average to both in MU's serial plotter
    print((inVal, average))
    # return the new average
    return average


pixels.fill((255, 255, 255))


# repeat this code forever
while True:
    # gather and smooth input
    smoothedValue = expSmooth(knob.value, 0.25)

    # scale the smoothed value to calculate a brightness for the pixels
    scaledValue = scaleAndTranslate(smoothedValue, 0, 65535, 0, 1)
    print(scaledValue)

    # do output based on mode
    pixels.fill = scaledValue
    time.sleep(0.1)