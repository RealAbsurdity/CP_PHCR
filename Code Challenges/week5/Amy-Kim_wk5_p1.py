"""
# problem 1:
the code currently allows the color to change even when the leds are off...
Try it! Set the slide switch to the ON position and press button A.
Next set the slide switch to the OFF position and press button B.
Now set the slide switch to the ON position again. What happened? Why?
How can we make it so the device only changes the color when the slide
switch is in the ON position? Do it without adding a single line of code...
"""

# import modules and libraries
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

# declare neopixel with onboard neopixel pin
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# declare digital input object on pin D7, slideswitch
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

buttonA = DigitalInOut(board.BUTTON_A)
buttonA.direction = Direction.INPUT
buttonA.pull = Pull.DOWN
buttonA_pre = buttonA.value

buttonB = DigitalInOut(board.BUTTON_B)
buttonB.direction = Direction.INPUT
buttonB.pull = Pull.DOWN
buttonB_pre = buttonB.value

# create a color variable and fill the pixels with the color
BLUE = (0, 0, 255)
ORANGE = (255, 255, 0)
GREEN = (0, 255, 0)
color = ORANGE
pixels.fill(color)

# loop forever
while True:
    pass
    if switch.value:
        pixels.fill(color)

        if buttonA.value != buttonA_pre:
            buttonA_pre = buttonA.value
            if buttonA.value:
                color = BLUE
                print(color)

        if buttonB.value != buttonB_pre:
            buttonB_pre = buttonB.value
            if buttonB.value:
                color = ORANGE
                print(color)

        if buttonA_pre and buttonB_pre:
            color = GREEN
            
    else:
        pixels.fill(0)
        
    time.sleep(0.1)
