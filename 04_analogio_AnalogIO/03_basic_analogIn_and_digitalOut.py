# read an analog input and use a threshold to light led

# import modules and libraries
import board
import time
import digitalio
import analogio

# declare variables and objects
analogIn = analogio.AnalogIn(board.A1)

# declare led1 - led5
led1 = digitalio.DigitalInOut(board.A2)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.A3)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.A4)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.A5)
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.A6)
led5.direction = digitalio.Direction.OUTPUT

# declare threshold constants
TH1 = 5000
TH2 = 17000
TH3 = 29000
TH4 = 41000
TH5 = 53000

# repeat this code forever
while True:
    # gather input
    reading = analogIn.value

    # do output
    # print the threshold and reading for PLOTTER
    print((TH1, TH2, TH3, TH4, TH5, reading))

    # if reading is > threshold turn on the led
    if reading > TH5:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        led5.value = True
    elif reading > TH4:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        led5.value = False
    elif reading > TH3:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = False
        led5.value = False
    elif reading > TH2:
        led1.value = True
        led2.value = True
        led3.value = False
        led4.value = False
        led5.value = False
    elif reading > TH1:
        led1.value = True
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
    else:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False

    # sleep to prevent serial buffer overflow
    time.sleep(0.05)