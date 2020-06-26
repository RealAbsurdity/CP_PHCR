# Use the rotaryio and digitalio library with a basic incremental rotary encoder

# import modules
import board
import time
import rotaryio

knob = rotaryio.IncrementalEncoder(board.A2, board.A3)

# constants to constrain knob.position value
POSMIN = 0
POSMAX = 255

# repeat forever
while True:

    # gather input
    # get the position value from the rotary encoder
    count = knob.position


    # do calculations
    # constrain the count and knob.position
    if count < POSMIN:
        count = POSMIN
    elif count > POSMAX:
        count = POSMAX

    # save the count to the knob.position
    knob.position = count


    # do output
    print(count)

    time.sleep(0.1)