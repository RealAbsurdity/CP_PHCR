import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

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

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

color = [RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, WHITE]
i = 0
bright = 0
add = 0.01

while True:
    if switch.value:
        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                i -= 1
                if i == -1:
                    i = 6

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                i += 1
                if i == 7:
                    i = 0

        pixels.fill(color[i])
    else:
        breathe = (int(color[i][0] * bright), int(color[i][1] * bright), int(color[i][2] * bright))
        bright += add
        if bright > 0.8:
            add = -add
            time.sleep(0.01)
        if bright < 0:
            add = -add
            time.sleep(0.01)

        pixels.fill(breathe)
    time.sleep(0.01)
