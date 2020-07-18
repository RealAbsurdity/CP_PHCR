# Example of LOGICAL NOT expressions on circuit playground express
# uses onboard buttons and neopixels to visualize logical NOT
# uses adafuirt_circuitplayground library for shorter code
from adafruit_circuitplayground import cp

RED = (255, 0, 0)
GREEN = (0, 255, 0)

cp.pixels.brightness = 0.05
cp.pixels.fill(0)

while True:

    if not cp.button_a:
        cp.pixels.fill(GREEN)
    else:
        cp.pixels.fill(RED)

    # the pixles will remain GREEN until button_A is pressed
    # not reverses the value of cp.button_a == True