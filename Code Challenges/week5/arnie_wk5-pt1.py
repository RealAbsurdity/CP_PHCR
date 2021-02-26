# written for circuit playground boards (CPX and CPB)
# toggle neopixel leds on and off with the slide switch
# set the color to blue with button B and orange with button A
"""
# problem 1:

the code currently allows the color to change even when the leds are off...

Try it! Set the slide switch to the ON position and press button A.
Next set the slide switch to the OFF position and press button B.
Now set the slide switch to the ON position again. What happened? Why?

How can we make it so the device only changes the color when the slide
switch is in the ON position? Do it without adding a single line of code...
"""

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

pixels = neopixel.NeoPixel(board.NEOPIXEL, 30)

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

ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
color = BLUE

while True:

    if button_a.value != buttona_pre:
        buttona_pre = button_a.value
        if button_a.value:
            color = ORANGE

    if button_b.value != buttonb_pre:
        buttonb_pre = button_b.value
        if button_b.value:
            color = BLUE

    if switch.value != switch_off:
        pixels.fill(color)
    else:
        pixels.fill(0)