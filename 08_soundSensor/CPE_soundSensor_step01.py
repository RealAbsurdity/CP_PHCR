import board
import time
import audiobusio

import array

# declare an audiobusio object for the microphone
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# declare a buffer array to store 16-bit integer values
samples = array.array('H', [0] * 10)
# 'H' tells the array to only store 16-bit integers
# [0] is the value to store in the array
# * is not multiplication here! it is "packing" 10 0-values into the array!
# we will increase this number later

# use the .record method to store samples in the array
mic.record(samples, len(samples))

# define a function to average the values in the sample buffer
def mean(values):
    return sum(values) / len(values)


while True:
    mic.record(samples, len(samples))
    average = mean(samples)
    print((average,))
    time.sleep(0.01)