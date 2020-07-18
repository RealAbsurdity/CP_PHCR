# Example of for loops using range() function
# assigns color values from range() to animate 'breathing' pixels
# potentiometer value alters the step to change speed
# written and tested on Adafruit Circuit Playground Express
# wire potentiometer wiper pin to A1

import board
import neopixel
import analogio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

knob = analogio.AnalogIn(board.A1)

pixels.fill(0)

while True:
    # get a step value from the analog knob input
    step = int(knob.value / 63000 * 10) + 1
    print("Step value is", step)

    # fill with blue value using range(), control speed with step
    for x in range(0, 255, step):
        pixels.fill((0, 0, x))
        pixels.show()

    # same in reverse
    for x in range(255, 0, -step):
        pixels.fill((0, 0, x))
        pixels.show()

    time.sleep(0.01)