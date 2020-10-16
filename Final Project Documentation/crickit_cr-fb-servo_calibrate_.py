# parallax feedback 360 continuous servo move calibration
# written for adafruit CPX and adafruit crickit
# feedback is an pulsein signal on a digital pin from the servo feedback wire

import board
import neopixel
from adafruit_crickit import crickit
import pulseio
import time
import countio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=True, brightness=0.1)
pixels.fill((0, 0, 255))

# declare a crickit seesaw object
ss = crickit.seesaw

# declare a pulseio object for the servo feedback
servo_fb = pulseio.PulseIn(board.D5)
# immedately stop the pulse stream and clear it
servo_fb.pause()
servo_fb.clear()
MIN_P = 32
MAX_P = 1046
PULSE_RANGE = MAX_P - MIN_P

# declare a servo objet
servo = crickit.continuous_servo_1
servo.set_pulse_width_range(min_pulse=1200, max_pulse=1720)

scount = countio.Counter(board.D6)

# define a function to scale and translate pulsewidth into angle
def servo_angle(feedback_obj):
    # start with a clean pulsein reading
    feedback_obj.clear()
    feedback_obj.resume()
    # wait for a pulse on the pulsein pin
    while len(feedback_obj) == 0:
        pass
    feedback_obj.pause()
    pulse_width = feedback_obj[0]

    # calculate a scale factor (percent) from the inVal in pulse range
    inProportion = (pulse_width - MIN_P) / PULSE_RANGE
    # return the new value scaled and translated to the outRange
    _angle = inProportion * 360
    if _angle < 0:
        _angle = 0
    elif angle > 360:
        _angle = 360

    # angle is now monotonic
    angle = (scount.count * 360) + _angle
    return int(angle)

# CALIBRATE SERVO
# calibrate the min_pulse and max_pulse
pixels.fill((0, 255, 0))
time.sleep(0.5)
th = 2
fb_th = 0.0
fwd_th = 0.0
for x in range(100):
    angle1 = servo_angle(servo_fb)
    servo.throttle = fb_th
    time.sleep(0.1)
    servo.throttle = 0.0
    angle2 = servo_angle(servo_fb)
    print(abs(angle1 - angle2))
    if abs(angle1 - angle2) >= th and fb_th > 0:
        fwd_th = fb_th
        servo.throttle = 0.0
        print("forward movement starts at", fwd_th)
        break
    else:
        fb_th += 0.01

pixels.fill((255, 0, 0))
time.sleep(0.5)
fb_th = 0.0
rev_th = 0.0
for x in range(100):
    angle1 = servo_angle(servo_fb)
    servo.throttle = fb_th
    time.sleep(0.1)
    servo.throttle = 0.0
    angle2 = servo_angle(servo_fb)
    print(abs(angle1 - angle2))
    if abs(angle1 - angle2) >= th and fb_th < 0:
        rev_th = fb_th
        servo.throttle = 0.0
        print("reverse movement starts at", rev_th)
        break
    else:
        fb_th -= 0.01

# if the absolute value of rev_th and fwd_th are not equal
# adjust max_pulse or min_pulse up or down
# in manual tests the reverse movement started at a higher absolute value
# to compensate the pulse_min had to be smaller

pixels.fill((0, 0, 255))


while True:
    pass