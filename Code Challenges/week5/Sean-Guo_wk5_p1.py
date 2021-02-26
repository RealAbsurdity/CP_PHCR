# device only changes the color when the slide switch is in the ON position

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

ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
color = BLUE

while True:



    if switch.value != switch_off:


        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                color = ORANGE

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                color = BLUE
        pixels.fill(color)
    else:
        pixels.fill(0)
