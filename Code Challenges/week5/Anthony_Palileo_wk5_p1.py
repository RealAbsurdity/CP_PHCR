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

ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
color = BLUE

while True:
    """
    moving the if statement that tests for the switch value up and
    nesting the button inputs into it requires the switch to be on
    for the button state changes to be evaluated
    """
    if switch.value != switch_off:
        pixels.fill(color)

        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                color = ORANGE

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                color = BLUE

    else:
        pixels.fill(0)