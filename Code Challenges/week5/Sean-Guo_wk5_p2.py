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

i = 0

# look up table RED GREEN BLUE YELLOW MAGENTA CYAN WHITE
colors = [(255, 0, 0), (0, 255, 0),
        (0, 0, 255), (255, 255, 0),
        (255, 0, 255), (0, 255, 255),
        (255, 255, 255)]

color = colors[i]

while True:

    if button_a.value != buttona_pre:
        buttona_pre = button_a.value
        if button_a.value:
            i += 1
            if i == 7:
                i = 0
            color = colors[i]

    if button_b.value != buttonb_pre:
        buttonb_pre = button_b.value
        if button_b.value:
            i -= 1
            if i == -1:
                i = 6
            color = colors[(i)]

    print(i)

    if switch.value != switch_off:
        pixels.fill(color)
    else:

        pixels.fill(0)
    time.sleep(0.1)