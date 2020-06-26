# use the touchio with CPE to read capacitive touch input and print data

# import modules
import board
import time
import touchio
import neopixel

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1 - A6)
touchPin1 = touchio.TouchIn(board.A1)
touchPin2 = touchio.TouchIn(board.A2)
touchPin3 = touchio.TouchIn(board.A3)
touchPin4 = touchio.TouchIn(board.A4)
touchPin5 = touchio.TouchIn(board.A5)
touchPin6 = touchio.TouchIn(board.A6)
touchPin7 = touchio.TouchIn(board.A7)

# put pins in a list
touchPins = [touchPin1, touchPin2, touchPin3,
            touchPin4, touchPin5, touchPin6, touchPin7]

touchVals = [False, False, False, False, False, False, False]

# neopixel stuff
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
COLOR = (0, 25, 255)
CLEAR = (0, 0, 0)

# repeat forever
while True:
    # capture touch input
    for x in range(7):
        touchVals[x] = touchPins[x].value

    print(touchVals)

    # do neopixel out with for loop
    for x in range(7):
        if touchVals[x] == True:
            pixels[x] = COLOR
        else:
            pixels[x] = CLEAR

    time.sleep(0.1)