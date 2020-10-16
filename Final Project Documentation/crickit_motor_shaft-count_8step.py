# Adafruit crickit motor test with hall effect shaft encoder
#

import board
import neopixel
from adafruit_crickit import crickit
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False, brightness=0.1)
pixels.fill((0, 0 , 255))
pixels.show()

# declare a crickit seesaw object
ss = crickit.seesaw

# declare a crickit input for hall sensor shaft counter
sc = crickit.SIGNAL1
# set the shaft counter as an input
ss.pin_mode(sc, ss.INPUT_PULLUP)

# variables to record motor shaft turns
# (8 poles / motor rev) only counting half
# (48 : 1 gear ratio)
# 4 x 48 is 192
sc_pre = ss.digital_read(sc)
shaft_count = 0

# declare a motor object
motor = crickit.dc_motor_1
# variable for motor throttle range -1 to 1 (rev to fwd)
throttle = 0.3

motor.throttle = throttle

motor_run = True

# calibrate the start position of the shaft
motor.throttle = 0.3
while shaft_count < 8:
    # read the shaft counter hall sensor
    sc_read = ss.digital_read(sc)
    if sc_read != sc_pre:
        sc_pre = sc_read
        print(sc_read)
        shaft_count += 1
shaft_count = 0

motor.throttle = 0.3

while True:
    # read the shaft counter hall sensor
    sc_read = ss.digital_read(sc)

    # if the shaft counter is changed
    if sc_read != sc_pre:
        sc_pre = sc_read
        print(sc_read)
        # if the shaft counter is changed it has moved at least 1/8 turn
        if throttle > 0:
            shaft_count += 1
            print(shaft_count)
        elif throttle < 0:
            shaft_count -= 1
            print(shaft_count)

        # after counting the shaft check to see if it has made a full turn
        if shaft_count == 8:
            motor.throttle = 0
            time.sleep(0.5)
            throttle = -0.3
            print("Motor REV")
        elif shaft_count == 0:
            motor.throttle = 0
            time.sleep(0.5)
            throttle = 0.3
            print("Motor FWD")

    if motor_run:
        motor.throttle = throttle