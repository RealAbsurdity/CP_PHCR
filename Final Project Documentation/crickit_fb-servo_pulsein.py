# parallax feedback 360 continuous servo pulse width example

import board
from adafruit_crickit import crickit
import time
import pulseio

# declare a pulseio object for the servo feedback
servo_fb = pulseio.PulseIn(board.D5)
# immedately stop the pulse stream and clear it
servo_fb.pause()
servo_fb.clear()
MIN_P = 32
MAX_P = 1046
PULSE_RANGE = MAX_P - MIN_P

""" Max pulse lenth is 97.1% of 910Hz or .971 * 1098.9us
    theoretical max_pulse is 1067us

    measured max_pulse is 1045

    Min pulse legth is 2.7% of 910Hz or .027 * 1098.9us
    theoretical min_pulse is 29us

    measured min_pulse is 32
"""

# define a function to scale and translate pulsewidth into angle
def servo_angle(feedback_obj):
    # start with a clean pulsein reading
    feedback_obj.pause()
    feedback_obj.clear()
    feedback_obj.resume()
    # wait for a pulse on the pulsein pin
    while len(feedback_obj) == 0:
        pass
    feedback_obj.pause()
    pulse_width = feedback_obj[0]
    feedback_obj.clear()

    # calculate a scale factor (percent) from the inVal in pulse range
    inProportion = (pulse_width - MIN_P) / PULSE_RANGE
    # return the new value scaled and translated to the outRange
    angle = inProportion * 360
    if angle < 0:
        angle = 0
    elif angle > 360:
        angle = 360
    return int(angle)

while True:
    # print servo angle
    print((servo_angle(servo_fb), ))

    time.sleep(0.01)