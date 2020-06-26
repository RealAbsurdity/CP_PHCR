# read an analog input and print the value to serial

# import modules and libraries
import board
import time
import analogio

# declare variables and objects

analogIn = analogio.AnalogIn(board.A1)
analogOut = analogio.AnalogOut(board.A0)

# repeat this code forever
while True:
    # gather and print input
    print(analogIn.value)

    time.sleep(0.1)