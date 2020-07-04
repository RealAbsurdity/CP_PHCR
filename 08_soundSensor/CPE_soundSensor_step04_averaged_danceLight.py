import board
import time
import audiobusio
import neopixel

import array
import math

# declare a neopixels object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

pixels.fill(0)

# declare an audiobusio object for the microphone
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# declare a buffer array to store 16-bit integer values
samples = array.array('H', [0] * 80)

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

# define a function to scale and translate RMS value to rgb output range
def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart

# a list of colors and index value for the neopixels
colorList = [0, 0, 0]
listIndex = 0

# a timer and interval to control how often to listen to the mic
sampleTime = time.monotonic()
sampleInterval = 0.1

# a list to store soundlevels to calculate an average level
soundLevels = []
for x in range(10):
    mic.record(samples, len(samples))
    RMS = normalized_rms(samples)
    soundLevels.append(RMS)
    time.sleep(sampleInterval)

# a variable to store the last 1 second worth of sound values
averageRMS = mean(soundLevels)

# loop 4-ever
while True:
    if time.monotonic() >= sampleTime:
        # reset the next sampleTime
        sampleTime += sampleInterval

        #gather some mic data
        mic.record(samples, len(samples))
        RMS = normalized_rms(samples)
        print((RMS,))

        # save the new RMS value in the levels list
        soundLevels.pop(0)
        soundLevels.append(RMS)
        # get the average of the list
        averageRMS = mean(soundLevels)

        # use the new RMS value to set the intensity of the leds
        colorVal = int(scaleAndTranslate(RMS, min(soundLevels), max(soundLevels), 0, 255))

        # don't let the colorVal go out of range
        if colorVal > 255:
            colorVal = 255

        # lower threshold is more responsive
        threshold = averageRMS * 1.75  # factor betwee 1 - 2
        # if the rms value is high enough, change the colorList index
        if RMS > threshold:
            listIndex += 1
            if listIndex > 2:
                listIndex = 0

    # "fall-off" all values in the colorList
    for value in range(3):
        temp = colorList[value]
        # colors are more vivid with higher fall-offs
        temp -= 12  # range of 2 - 32
        if temp < 0:
            temp = 0
        colorList[value] = temp

    # store the newest value in the list
    colorList[listIndex] = colorVal

    pixels.fill(tuple(colorList))
