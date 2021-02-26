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

# import modules and libraries
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# declare neopixel with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare digital input object on pin D7, slideswitch
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonA_pre = buttonA.value

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonB_pre = buttonB.value

# create a color variable and fill the pixels with the color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

colors = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE]

for x in range(len(pixels)):
    pixels[x] = colors[x]

colorMode = 0

"""
How could we make it so the two
buttons cycle forward and backward through a series of color options?
-> like a ping pong...???
"""

while True:
    if switch.value != switch_off:
        pixels.fill(colors[colorMode])

        if buttonA.value != buttonA_pre:
            buttonA_pre = buttonA.value
            if buttonA.value:
                colorMode += 1
                

        if buttonB.value != buttonB_pre:
            buttonB_pre = buttonB.value
            if buttonB.value:
                colorMode += 2

    else:
        pixels.fill(0)
