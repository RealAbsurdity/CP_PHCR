# import modules
import time
import board
import pulseio

# make a led object with pulseio.PWMOut on pin board.A1
led = pulseio.PWMOut(board.A1, duty_cycle=0)

fadeInc = 1000

newDutyCycle = 0

"""
pulseio.PWMOut creates a PWMOut object with the name led

you can set the duty_cycle with the property led.duty_cycle

led.duty_cycle accepts a 16-bit integer value from 0 - 65535
"""

# loop forever
while True:
    newDutyCycle += fadeInc

    if newDutyCycle > 65535:
        newDutyCycle = 65535
        fadeInc = -1000
    elif newDutyCycle < 0:
        newDutyCycle = 0
        fadeInc = 1000

    led.duty_cycle = newDutyCycle
    print(led.duty_cycle)
    time.sleep(0.01)