# importing le modulesssss
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# declaring neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declaring switch and buttons inputs
buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonA_pre = buttonA.value

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonB_pre = buttonB.value

switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# storing color variablessssss lets make a rainbowwwww
RED = (255, 0, 0)
ORANGE = (255, 145, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

# creating a list from the color variables
color = [RED, ORANGE, YELLOW, GREEN, BLUE, CYAN, WHITE]
bright = 0
mode = 0
step = 1

while True:
    if switch.value:
        # changing the neopixel color modes
        if buttonA.value != buttonA_pre:
            buttonA_pre = buttonA.value
            if buttonA.value:
                mode -= 1

        if buttonB.value != buttonB_pre:
            buttonB_pre = buttonB.value
            if buttonB.value:
                mode += 1
        mode %= 7
        pixels.fill(color[mode])
        bright = 0
    else:
        # when slide switch mode changes state, intiates "breate" mode.
        # breathe is by adjusting brightness
        breathe = (int(color[mode][0] * bright / 500),
                   int(color[mode][1] * bright / 500),
                   int(color[mode][2] * bright / 500))
        # using dot notation to fill neopixels with breathe mode
        pixels.fill(breathe)
        bright += step
        if (bright == 201) or (bright == -1):
            step = -step
    time.sleep(0.05)
