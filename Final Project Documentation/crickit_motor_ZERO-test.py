# Adafruit crickit motor position zero and shaft sensor alignment code

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

# declare a crickit input for ZERO hall sensor
s_zero = crickit.SIGNAL2
# set the shaft counter as an input
ss.pin_mode(s_zero, ss.INPUT_PULLUP)

while True:
    # read and print the shaft zero hall sensor
    sz_read = ss.digital_read(s_zero)
    # read and print the shaft counter hall sensor
    sc_read = ss.digital_read(sc)
    print(sz_read, sc_read)
    time.sleep(0.01)