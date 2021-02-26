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

RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
CLEAR = (0, 0, 0)
color = BLUE
cycle = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE]
i = 0

while True:

    if switch.value != switch_off:

        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                color = cycle[i]
                i += 1
                if i == 7:
                    i = 0

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                color = cycle[i]
                i -= 1
                if i == -1:
                    i = 6

        print(i)
        pixels.fill(color)

    else:
        pixels.fill(0)

    time.sleep(0.01)
