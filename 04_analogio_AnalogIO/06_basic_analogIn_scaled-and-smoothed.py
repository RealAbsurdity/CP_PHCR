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

def mapValuetoRange(inVal, inMin, inMax, outMin, outMax):
    # calculate incoming range
    inRange = inMax - inMin
    # calculate a scale factor (percent) from the inVal in the inRange
    inPercent = inVal / inRange
    # calculate the output range
    outRange = outMax - outMin
    # calculate a new value scaled to the outRange
    scaledOut = inPercent * outRange
    # add the scaledOut to outMin and return the value
    return outMin + scaledOut

# initialize average with first read of the knob.value
average = mapValuetoRange(knob.value, 0, 65535, 0, 1)

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
    # gather and scale input
    scaledValue = mapValuetoRange(knob.value, 0, 65535, 0, 1)

    # scale the smoothed value to calculate a brightness for the pixels
    smoothedValue = expSmooth(scaledValue, 0.1)

    print(smoothedValue)

    # do output based on mode
    pixels.brightness = smoothedValue
    time.sleep(0.01)