# import modules
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# declaring le objects
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declaring buttons and switches and their values
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
i = 0

# repeat loooooop
while True:
    # is the switch on or off?
    if switch.value:
        # changing the color modes with a list
        if buttonA.value != buttonA_pre:
            buttonA_pre = buttonA.value
            if buttonA.value:
                i -= 1

        if buttonB.value != buttonB_pre:
            buttonB_pre = buttonB.value
            if buttonB.value:
                i += 1
        i %= 7
        pixels.fill(color[i])
    # if switch value is 0 then the neopixels are off
    else:
        pixels.fill(0)
    time.sleep(0.01)