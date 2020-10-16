# Adafruit crickit stepper motor test with hall effect shaft encoder

import board
import neopixel
from adafruit_crickit import crickit
from adafruit_motor import stepper
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False, brightness=0.1)
pixels.fill((0, 0 , 255))
pixels.show()
time.sleep(2)

# declare a crickit seesaw object
ss = crickit.seesaw
# declare a crickit input for hall sensor shaft counter
s_zero = crickit.SIGNAL1
# set the shaft counter as an input
ss.pin_mode(s_zero, ss.INPUT_PULLUP)

# declare a motor object
stepmotor = crickit.stepper_motor


#  BEGIN CALIBRATION ROUTINE
for x in range(3):
    pixels.fill((255, 0 , 0))
    pixels.show()
    time.sleep(0.25)
    pixels.fill(0)
    pixels.show()
    time.sleep(0.25)

time.sleep(1)

# calibrate the start position of the shaft
print(ss.digital_read(s_zero))

pixels.fill((255, 0 , 0))
pixels.show()

while ss.digital_read(s_zero):
    stepmotor.onestep(direction=stepper.FORWARD)
    time.sleep(0.02)
else:
    pixels.fill((0, 255, 0))
    pixels.show()
    time.sleep(1)

pixels.fill((0, 0, 255))
pixels.show()

# variables to record motor shaft turns from known zero
shaft_steps = 0

time.sleep(1)
# END CALIBRATION ROUTINE


while True:

    while shaft_steps < 200:
       stepmotor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
       shaft_steps += 1

    time.sleep(0.5)

    while 0 < shaft_steps:
       stepmotor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
       shaft_steps -= 1

    time.sleep(0.5)