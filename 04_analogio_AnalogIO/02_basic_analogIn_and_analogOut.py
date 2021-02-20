# read an analog input and print the value to serial

# import modules and libraries
import board
import time
import analogio
import pwmio

# declare analog input object on pin A1
analog_in = analogio.AnalogIn(board.A1)

# declare PWMOut object on pin A2
pwm_out = pwmio.PWMOut(board.A2)

# repeat this code forever
while True:
    # gather and print input
    print(analog_in.value)

    """
    change to tuple: print((analog_in.value,))
    to show in serial plotter
    """

    # set the analogOut value to match the analogIn value
    pwm_out.duty_cycle = analog_in.value

    # sleep to prevent serial buffer overflow
    time.sleep(0.1)