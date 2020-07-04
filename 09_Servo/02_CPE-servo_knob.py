import board
import time
import pulseio
from adafruit_motor import servo
import analogio

# delcare a PWMOut object
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# declare a servo object
thisServo = servo.Servo(pwm)

# declare an analog input
knob = analogio.AnalogIn(board.A5)

# define a function to scale and translate input value to output range
def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart

while True:
    angle = scaleAndTranslate(knob.value, 0, 65535, 0, 180)
    thisServo.angle = angle
    time.sleep(0.01)