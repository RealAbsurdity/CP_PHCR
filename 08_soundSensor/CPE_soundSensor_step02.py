import board
import time
import audiobusio

import array
import math

# declare an audiobusio object for the microphone
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# declare a buffer array to store 16-bit integer values
samples = array.array('H', [0] * 160)

# use the .record method to store samples in the array
mic.record(samples, len(samples))

# define a function to average the values in the sample buffer
def mean(values):
    return sum(values) / len(values)

# define a function to calculate the RMS of the data sample
def normalized_rms(values):
    # average the samples to establish a baseline for normalization
    baseline = int(mean(values))

    # sum the square of the difference from the baseline of each sample
    sqDiffSum = sum(float(sample - baseline)**2 for sample in values)
    # ^this looks a little weird becuase it uses list comprehension
    # see the list comprehension example in the Miro slides.

    # average the squared samples
    avgSqDiff = sqDiffSum / len(values)

    # return the square root of the average of the squared samples
    return math.sqrt(avgSqDiff)


while True:
    mic.record(samples, len(samples))
    RMS = normalized_rms(samples)
    print((RMS,))
    time.sleep(0.01)