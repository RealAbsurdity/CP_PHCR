# use the touchio with CPE to read capacitive touch input and print data

# import modules
import board
import time
import touchio

# declare objects and variables
# declare touchIn object on CPE cap-touch pin (A1 - A6)
touchPin = touchio.TouchIn(board.A1)

# repeat forever
while True:
    # print the value of the touchPin to serial
    print(touchPin.value)

    time.sleep(0.1)