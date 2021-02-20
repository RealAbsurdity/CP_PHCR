# read an analog input and smooth the value with a weight

# import modules and libraries
import board
import analogio
import time

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


# repeat this code forever
while True:
    # gather input
    reading = analog_in.value

    # do calculation: weightedSmooth() with the reading and a weight
    smooth_val = weightedSmooth(reading, 0.25)
    # raise and lower the weight and see the effect in the serial monitor!
    # the weight must fall between 0.0 and 1.0

    # print both values to the serial monitor in a touple for PLOTTER
    print((reading, smooth_val))

    # sleep to prevent buffer overrun
    time.sleep(0.1)