import board
import neopixel
import analogio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# save a series of index values in a tuple
pixel_index = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

BLUE = (0, 0, 255)
RED = (255, 0, 0)

# create analogio object for KNOB
knob = analogio.AnalogIn(board.A1)

while True:
    # calculate the top pixel index value from the knob value
    level = int(knob.value / 63000 * 10)  # ranges 0 - 10
    print("Level is", level)

    # look for the level in the pixel index
    if level in pixel_index:
        # clear the pixels
        pixels.fill(0)
        print("Level pixel", level, "is BLUE")
        pixels[level] = BLUE
    else:
        # level value not found, fill RED
        print("Level not found, fill RED")
        pixels.fill(RED)

    pixels.show()
    time.sleep(0.01)