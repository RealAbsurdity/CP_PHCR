# parallax feedback 360 continuous servo response to 4 digital inputs
# written for adafruit CPX and adafruit crickit

import board
import neopixel
from adafruit_crickit import crickit
import time
from pulseio import PulseIn

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)
pixels.fill((0, 0, 255))

# declare a crickit seesaw object
ss = crickit.seesaw

# declare a servo objet
servo = crickit.continuous_servo_1
servo.set_pulse_width_range(min_pulse=1220, max_pulse=1720)

# declare a pulseio object for the servo feedback
servo_fb = PulseIn(board.D5)

# declare four digital inputs
PIR = [crickit.SIGNAL1, crickit.SIGNAL2, crickit.SIGNAL3, crickit.SIGNAL4]
for pir in PIR:
    ss.pin_mode(pir, ss.OUTPUT)
    ss.pin_mode(pir, ss.INPUT_PULLUP)

pir_read = [False, False, False, False]
pir_readpre = [False, False, False, False]
pir_change = [False, False, False, False]
change_index = []
last_change = 0
max_change = 4

direction = 0
servo_speed = 0

while True:
    # read the pulseIn object for the servo_fb
    servo_fb.pause()
    print(servo_fb)
    servo_fb.clear()
    pulses.resume()

    """
    # read each sensor in order and look for a change from low to high
    for index, pir in enumerate(PIR):
        pir_read[index] = ss.digital_read(pir)
        if pir_read[index] != pir_readpre[index]:
            pir_readpre[index] = pir_read[index]
            if pir_read[index] == True:
                pir_change[index] = True
                change_index.append(index + 1)
        else:
            pir_change[index] = False
    else:
        if len(change_index) > max_change:
            change_index.pop(0)
        # print("raw read", pir_read)
        print("change?", pir_change)
        print("change index", change_index)

    if len(change_index) >= 2:
        motion = change_index[1]
        pre_motion = change_index[0]
        if motion == 1:
            if pre_motion == 4:
                direction = 1
            else:
                try:
                    direction = int(motion - pre_motion / abs(motion - pre_motion))
                except:
                    pass
        elif motion == 4:
            if pre_motion == 1:
                direction = -1
            else:
                try:
                    direction = int(motion - pre_motion / abs(motion - pre_motion))
                except:
                    pass
        else:
            direction = int(motion - pre_motion / abs(motion - pre_motion))
        change_index.clear()
    print(direction)
    """

    time.sleep(0.1)