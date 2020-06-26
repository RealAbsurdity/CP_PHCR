# read an analog input and smooth the value with a weight

# import modules and libraries
import board
import analogio
import time

# declare variables and objects
knob = analogio.AnalogIn(board.A1)

# initialize average with first read of the knob.value
average = knob.value

def weightedSmooth(inVal, weight):
    # declare average as global
    global average
    # apply weight to the incoming value and apply remaining weight to average
    average = weight * inVal + ((1 - weight) * average)
    # return the new average
    return average


# repeat this code forever
while True:
    # gather and smooth input
    newRead = knob.value
    smoothedValue = weightedSmooth(newRead, 0.25)

    # print both values to the serial monitor in a touple for PLOTTER
    print((newRead, ))
    time.sleep(0.01)