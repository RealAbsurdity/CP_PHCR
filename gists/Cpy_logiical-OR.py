# Example of LOGICAL OR expressions on circuit playground express
# uses onboard buttons and neopixels to visualize logical OR
# uses adafuirt_circuitplayground library for shorter code
from adafruit_circuitplayground import cp

RED = (255, 0, 0)
GREEN = (0, 255, 0)

cp.pixels.brightness = 0.05
cp.pixels.fill(0)

while True:

    if cp.button_a or cp.button_b:
        cp.pixels.fill(GREEN)
    else:
        cp.pixels.fill(RED)

    # the pixles will remain red until ANY button is pressed