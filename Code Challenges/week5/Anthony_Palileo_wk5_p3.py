# written for circuit playground boards (CPX and CPB)
# toggle neopixel leds on and off with the slide switch
# scroll through colors using onboard buttons

"""
BONUS PROBLEM
Currently our system indicates off by merely turning off the leds but it
is never truly off. It is more or less "sleeping" when the leds are not lit.
What if we wanted to more honestly indicate "sleep" mode with a slowly
breathing set of pixels at a dimmer value than the lit pixels? Can you
make it so it always turns the pixels totally off before breathing?
And use breathe to indicate sleep?
"""

import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

button_a = DigitalInOut(board.BUTTON_A)
button_a.direction = Direction.INPUT
button_a.pull = Pull.DOWN
buttona_pre = button_a.value

button_b = DigitalInOut(board.BUTTON_B)
button_b.direction = Direction.INPUT
button_b.pull = Pull.DOWN
buttonb_pre = button_b.value

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
switch_off = switch.value

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)

colorVals = [WHITE, RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW]
colorMode = 0

offInterval = 2
offTime = time.monotonic() + offInterval

breatheColor = [0, 0, 0]
breatheIncrement = 0.5

while True:
    if switch.value != switch_off:
        pixels.fill(colorVals[colorMode])
        pixels.show()

        for i in range(3):
            breatheColor[i] = 0
        offTime = time.monotonic() + offInterval

        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                colorMode -= 1
                if colorMode < 0:
                    colorMode = 6

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                colorMode += 1
                if colorMode > 6:
                    colorMode = 0

    else:
        pixels.fill(0)
        if time.monotonic() >= offTime:
            pixels.fill(breatheColor)
            pixels.show()
            for i in range(3):
                breatheColor[i] += breatheIncrement
            if breatheColor[0] >= 7:
                breatheIncrement *= -1
            if breatheColor[0] <= 0:
                breatheIncrement *= -1
            # reset the color to white
            colorMode = 0

        time.sleep(0.05)