# use the onboard light sensor and write the data to the serial monitor

# import modules
import board
import time
import analogio

# declare objects and variables
# use analogio object to access onboard light sensor
lightSens = analogio.AnalogIn(board.A8)


# repeat forever
while True:
    # print the light sensor value as a tuple for the PLOTTER
    print((lightSens.value,))

    time.sleep(0.01)