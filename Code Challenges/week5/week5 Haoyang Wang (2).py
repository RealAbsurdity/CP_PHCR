# use the touchio with CPE to read capacitive touch input and print data

# import modules
import board
import time
import touchio
import neopixel

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1 - A6)
touchPin = touchio.TouchIn(board.A1)
a2_in = touchio.TouchIn(board.A2)
a3_in = touchio.TouchIn(board.A3)
a4_in = touchio.TouchIn(board.A4)
a5_in = touchio.TouchIn(board.A5)
a6_in = touchio.TouchIn(board.A6)


on_off_val = 0
color_1_val = 0
color_2_val = 0
color_3_val = 0

# use the neopixels to show if the touch pin is touched
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
COLOR = (0, 25, 255)
CLEAR = (0, 0, 0)

change_step = 50
# repeat forever
while True:
    # gather input
    touchVal = touchPin.value
    if touchVal:
        on_off_val += 1

    if a2_in.value and color_1_val < 255:
        color_1_val = min(change_step + color_1_val, 255)

    a3_val = a3_in.value
    if a3_val and color_1_val > 0:
        color_1_val = max(color_1_val-change_step, 0)

    if a3_val and color_2_val < 255:
        color_2_val = min(change_step + color_2_val, 255)

    if a4_in.value and color_2_val > 0:
        color_2_val = max(color_2_val-change_step, 0)

    if a5_in.value and color_3_val < 255:
        color_3_val = min(change_step + color_3_val, 255)

    if a6_in.value and color_3_val > 0:
        color_3_val = max(color_3_val-change_step, 0)

    if on_off_val % 2 == 1:
        pixels.fill((color_1_val, color_2_val, color_3_val))
    else:
        pixels.fill(CLEAR)

    time.sleep(0.1)