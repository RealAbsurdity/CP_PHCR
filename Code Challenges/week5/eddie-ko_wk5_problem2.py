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

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

color = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, WHITE]
i = 0

while True:
    if switch.value:
        if button_a.value != buttona_pre:
            buttona_pre = button_a.value
            if button_a.value:
                i -= 1

        if button_b.value != buttonb_pre:
            buttonb_pre = button_b.value
            if button_b.value:
                i += 1
        i %= 7
        pixels.fill(color[i])
    else:
        pixels.fill(0)
    time.sleep(0.01)
