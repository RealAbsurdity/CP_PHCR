# written for circuit playground boards (CPX and CPB)
# toggle neopixel leds on and off with the slide switch
# set the color to blue with button B and orange with button A

"""
# problem 2

The code currently only allows for two colors to be set: button A sets
one color and button B sets another color. This is wasteful because we
can toggle between two things with a single button. How could we make
better use of the hardware we have? How could we make it so the two
buttons cycle forward and backward through a series of color options?

Make it cycle through all primary and secondary colors including white!

RED GREEN BLUE YELLOW MAGENTA CYAN WHITE
"""

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

while True:

    if switch.value != switch_off:
        pixels.fill(colorVals[colorMode])

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
        # reset the color
        colorMode = 0