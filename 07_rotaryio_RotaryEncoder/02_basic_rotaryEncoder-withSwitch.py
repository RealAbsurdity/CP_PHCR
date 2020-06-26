# Use the rotaryio and digitalio library with a basic incremental rotary encoder

# import modules
import board
import time
from digitalio import DigitalInOut, Direction, Pull
import rotaryio

# declare objects and variables
button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

click = False
buttonPre = False

knob = rotaryio.IncrementalEncoder(board.A1, board.A2)

# constants to constrain knob.position value
POSMIN = 0
POSMAX = 255

# repeat forever
while True:

    # gather input
    # get the position value from the rotary encoder
    count = knob.position

    # check if the button is changed
    if button.value != buttonPre:
        buttonPre = button.value
        if button.value:
            click = True


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

    if click:
        print("CLICK!")
        click = False

    time.sleep(0.1)