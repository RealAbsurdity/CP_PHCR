# use the touchio with CPE to read capacitive touch input and print data

# import modules
import board
import time
import touchio
import neopixel

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1 - A6)
touchPin = touchio.TouchIn(board.A1)

# use the neopixels to show if the touch pin is touched
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
COLOR = (0, 25, 255)
CLEAR = (0, 0, 0)

# repeat forever
while True:
    # gather input
    touchVal = touchPin.value
    print(touchVal)

    # do output
    if not touchVal:
        pixels.fill(COLOR)
    else:
        pixel.fill(CLEAR)

    time.sleep(0.1)