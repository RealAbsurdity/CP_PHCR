# Visual Thermometer for Adafruit Circuit Playground Express

import adafruit_thermistor     # import libraries required
import board
import time
import neopixel

thermistor = \
 adafruit_thermistor.Thermistor(board.TEMPERATURE, 10000, 10000, 22, 3950)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.01)
pixels.fill((0, 0, 0))
pixels.show()

n_pixels = 10            # Number of pixels you are using
mintemp = 0              # For adjustment of graph low
maxtemp = 40             # For adjustment of graph high

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition b - g - r - back to b.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(255 - pos*3), 0, int(pos*3))  # blue
    elif (pos < 170):
        pos -= 85
        return (0, int(pos*3), int(255 - pos*3))  # green
    else:
        pos -= 170
        return (int(pos * 3), int(255 - (pos*3)), 0)  # red


def remapRange(value, leftMin, leftMax, rightMin, rightMax):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (int)
    valueScaled = int(value - leftMin) / int(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))

while True:
    print("Temperature is: %f C" % (thermistor.temperature))
    # Store thermistor reading as a variable
    temp = thermistor.temperature
    # Calculate bar height based on adjustable min/max temperature:
    height = n_pixels * (temp - mintemp) / (maxtemp - mintemp)

    # Color pixels based on rainbow gradient
    for i in range(0, len(pixels)):
        if (i >= height):
            pixels[i] = [0, 0, 0]
        elif (temp >= maxtemp):
            pixels[i] = [255, 0, 0]
        else:
            pixels[i] = wheel(remapRange(i, 0, (n_pixels), 85, 255))

    time.sleep(0.5)      # reduces flickering