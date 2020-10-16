# parallax feedback 360 continuous servo move calibration
# written for adafruit CPX and adafruit crickit
# feedback is an pulsein signal on a digital pin from the servo feedback wire

import board
import neopixel
from adafruit_crickit import crickit
import pulseio
import time
import countio
import random

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=True, brightness=0.1)
pixels.fill((0, 0, 255))

# declare a crickit seesaw object
ss = crickit.seesaw

# pulsein for servo feedback idle_state True counts up with positive throttle
servo_fb = pulseio.PulseIn(board.D5, idle_state=True)
# immedately stop the pulse stream and clear it
servo_fb.pause()
servo_fb.clear()
MIN_P = 32
MAX_P = 1046
PULSE_RANGE = MAX_P - MIN_P

# declare a servo objet
servo = crickit.continuous_servo_1
servo.set_pulse_width_range(min_pulse=1200, max_pulse=1720)
servo.throttle = 0.0

fw_min = 0.18  # from calibration data
bw_min = -0.18  # from calibration data
fw_max = 0.8
bw_max = -0.8
fw_range = fw_max - fw_min
bw_range = bw_max - bw_min
slope = 0.5 / 360

# countio object for spindle zero sensor
scount = countio.Counter(board.D6)

# declare four digital inputs for the motion sensors
PIR = [crickit.SIGNAL1, crickit.SIGNAL2, crickit.SIGNAL3, crickit.SIGNAL4]
for pir in PIR:
    ss.pin_mode(pir, ss.OUTPUT)
    ss.pin_mode(pir, ss.INPUT_PULLUP)

pir_read = [False, False, False, False]
pir_readpre = [False, False, False, False]
pir_change = [False, False, False, False]
pir_angles = [0, 0, 0, 0]
pir_opangles = [0, 0, 0, 0]

direction = 0
servo_speed = 0

move_timer = time.monotonic()


# define a function to scale and translate pulsewidth into angle
def servo_angle(feedback_obj):
    # start with a clean pulsein reading
    feedback_obj.pause()
    feedback_obj.clear()
    feedback_obj.resume()
    # wait for a pulse on the pulsein pin
    while len(feedback_obj) == 0:
        pass
    pulse_width = feedback_obj[0]
    # calculate a scale factor (percent) from the inVal in pulse range
    inProportion = (pulse_width - MIN_P) / PULSE_RANGE
    # return the new value scaled and translated to the outRange
    _angle = inProportion * 360
    if _angle < 0:
        _angle = 0
    elif _angle > 360:
        _angle = 360
    return int(_angle)


def servo_zero(servo_obj, feedback_obj):
    global pir_angles
    global pir_opangles
    global move_timer

    scount.reset()
    while scount.count == 0:
        servo.throttle = 0.3
    servo.throttle = 0.0
    scount.reset()

    cur_angle = 2
    print(servo_angle(servo_fb))
    pir_angles[0] = cur_angle + 45
    pir_angles[1] = cur_angle + 135
    pir_angles[2] = cur_angle + 225
    pir_angles[3] = cur_angle + 315
    pir_opangles[0] = pir_angles[2]
    pir_opangles[1] = pir_angles[3]
    pir_opangles[2] = pir_angles[0]
    pir_opangles[3] = pir_angles[1]

    move_timer = time.monotonic()

def servo_move(servo_obj, feedback_obj, t_angle):
    global move_timer
    # pick a random direction
    new_dir = random.choice((1, -1))
    # pick a random speed
    new_speed = random.uniform(fw_min, fw_max)
    # calculate the new random throttle
    new_th = new_dir * new_speed
    print("new throttle is", new_th)
    print("target angle is", t_angle)

    if t_angle in range(t_angle - 20, t_angle + 20):
        servo.throttle = new_th
        time.sleep(0.1)

    while servo_angle(servo_fb) not in range(t_angle - 20, t_angle + 20):
        servo.throttle = new_th

    servo.throttle = 0

    move_timer = time.monotonic()


time.sleep(2)
servo_zero(servo, servo_fb)
time.sleep(2)

while True:
    cur_angle = servo_angle(servo_fb)
    print(cur_angle)

    # read each sensor in order and look for a change from low to high
    for index, pir in enumerate(PIR):
        pir_read[index] = ss.digital_read(pir)
        if pir_read[index] != pir_readpre[index]:
            pir_readpre[index] = pir_read[index]
            if pir_read[index] == True:
                pir_change[index] = True
        else:
            pir_change[index] = False

    try:
        change_index = pir_change.index(True)
        pir_change[change_index] = False
    except ValueError:
        change_index = -1

    if change_index > -1:
        move_angle = pir_opangles[change_index]
        servo_move(servo, servo_fb, move_angle)

    time.sleep(0.1)