# Adafruit crickit motor test with hall effect shaft encoder
#

import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
pixels.fill(0)
pixels.show()

# declare a crickit seesaw object
ss = crickit.seesaw

# declare a crickit input for hall sensor shaft counter
sc = crickit.SIGNAL1
# set the shaft counter as an input
ss.pin_mode(sc, ss.INPUT_PULLUP)

# variables to record motor shaft turns (48 / shaft rev)
sc_pre = ss.digital_read(sc)
shaft_count = 0

# declare a motor object
motor = crickit.dc_motor_1
# variable for motor throttle range -1 to 1 (rev to fwd)
throttle = 0

motor.throttle = throttle

throttle = 1

while True:
    # read the shaft counter hall sensor
    sc_read = ss.digital_read(sc)

    # if the shaft counter is changed
    if sc_read != sc_pre:
        sc_pre = sc_read
        print(sc_read)
        # if the shaft counter is True it has moved
        if sc_read == True:
            if throttle > 0:
                shaft_count += 1
                print(shaft_count)
            elif throttle < 0:
                shaft_count -= 1
                print(shaft_count)

    if shaft_count == 48:
        throttle = -1
    elif shaft_count == 0:
        throttle = 1

    motor.throttle = throttle