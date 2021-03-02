# version 2 add blinking to yellow and red lights
import board
# import neopixels and assign colors
import neopixel
# import time for timemonotonic for flashing lights
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)
# declare neopixel with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# create a color variable and fill the pixels with the color

GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
color = GREEN
pixels.fill(0)

# delcare thresholds
TH1 = 110
TH2 = 60
TH3 = 20

# the intervals of the blinks
slowblinking = 1
fastblinking = 0.4

# time.monotonic() always Increases! from program start
blinkTime = time.monotonic() + slowblinking

this_distance = 120

# repeat this code forever
while True:
    try:
        this_distance = sonar.distance
    except RuntimeError:
        print("Retrying!")

    # print output
    print((this_distance, TH1, TH2, TH3))

    # check the thresholds
    if this_distance > TH1:
        color = 0
    elif this_distance > TH2:
        color = GREEN
    elif this_distance > TH3:
        if time.monotonic() >= blinkTime:
            blinkTime += slowblinking
            if color != 0:
                color = 0
            else:
                color = YELLOW
    if time.monotonic() >= blinkTime:
        blinkTime += fastblinking
        if color != 0:
            color = 0
        else:
            color = RED

    # use the output of the previous if statement and set output of pixels
    pixels.fill(color)

    time.sleep(0.05)
