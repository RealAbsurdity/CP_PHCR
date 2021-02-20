# read an analog input and print the value to serial

# import modules and libraries
import board
import time
import analogio

# declare analog input object on pin A1
analog_in = analogio.AnalogIn(board.A1)

# repeat this code forever
while True:
    # gather and print input
    print(analog_in.value)

    # sleep to prevent buffer overrun
    time.sleep(0.1)