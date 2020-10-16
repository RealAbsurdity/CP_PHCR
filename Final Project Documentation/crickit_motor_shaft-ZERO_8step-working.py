# Adafruit crickit motor test with hall effect shaft encoder

import board
import neopixel
from adafruit_crickit import crickit
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False, brightness=0.1)
pixels.fill((0, 0 , 255))
pixels.show()
time.sleep(5)

# declare a crickit seesaw object
ss = crickit.seesaw

# declare a crickit input for hall sensor shaft counter
sc = crickit.SIGNAL1
# set the shaft counter as an input
ss.pin_mode(sc, ss.INPUT_PULLUP)

# declare a crickit input for ZERO hall sensor
s_zero = crickit.SIGNAL2
# set the shaft counter as an input
ss.pin_mode(s_zero, ss.INPUT_PULLUP)

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
motor_run = True


#  BEGIN CALIBRATION ROUTINE
for x in range(3):
    pixels.fill((255, 0 , 0))
    pixels.show()
    time.sleep(0.25)
    pixels.fill(0)
    pixels.show()
    time.sleep(0.25)

pixels.fill((255, 255 , 0))
time.sleep(1)

# calibrate the start position of the shaft
print(ss.digital_read(s_zero))
motor.throttle = 0.3
time.sleep(1)
motor.throttle = 0.25

while ss.digital_read(s_zero):
    pass
else:
    motor.throttle = 0
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

pixels.fill((0, 0, 255))
pixels.show()
shaft_count = 0
sc_read = ss.digital_read(sc)
time.sleep(1)
# END CALIBRATION ROUTINE

# start the motor
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
            throttle = -0.6
            print("Motor REV")
        elif shaft_count == 0:
            motor.throttle = 0
            time.sleep(0.5)
            throttle = 0.6
            print("Motor FWD")

    if motor_run:
        motor.throttle = throttle