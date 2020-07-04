import board
import time
import pulseio
from adafruit_motor import servo

# delcare a PWMOut object
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# declare a servo object
thisServo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 1):
        thisServo.angle = angle
        time.sleep(0.003)
    time.sleep(0.5)
    for angle in range(180, 0, -1):
        thisServo.angle = angle
        time.sleep(0.003)
    time.sleep(0.5)