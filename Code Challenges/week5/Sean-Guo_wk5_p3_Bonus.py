# breathing
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

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

w = 15
a = 1
dimWhite = [0, 0, 0]
dimInterval = 0.01
dimTime = time.monotonic() + dimInterval

while True:

    if button_a.value != buttona_pre:
        buttona_pre = button_a.value
        if button_a.value:
            i += 1
            if i == 7:
                i = 0
            color = colors[i]
            pixels.show()

    if button_b.value != buttonb_pre:
        buttonb_pre = button_b.value
        if button_b.value:
            i -= 1
            if i == -1:
                i = 6
            color = colors[(i)]
            pixels.show()
    # print(i)

    if switch.value != switch_off:
        pixels.fill(color)
        pixels.show()

    # check if it is time to dim
    else:
        if time.monotonic() >= dimTime:

            # increament
            dimTime += dimInterval
            w += a
            if w > 20 or w < 1 :
                a = -a        # dim
            dimWhite = [w, w, w]
            pixels.fill(dimWhite)
            pixels.show()
        print(dimWhite, w)

    time.sleep(0.1)
