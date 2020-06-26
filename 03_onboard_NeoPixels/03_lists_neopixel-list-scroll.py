# use lists to animate a set of neopixels

# import modules
import board
import time
import neopixel

# declare objects and variables
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)

# declare a list of 10 fading cotton candy color tuples
# this is also known as a lookup table
colors = [(0, 255, 0), (28, 227, 0),
            (56, 199, 0), (84, 171, 0),
            (112, 143, 0), (140, 115, 0),
            (168, 87, 0), (196, 59, 0),
            (224, 31, 0), (255, 0, 0)]

# loop colors and apply them to pixels
for x in range(len(pixels):
    pixels[x] = colors[x]

pixels.show()

time.sleep(1)

# repeat forever
while True:
    # pop the first value from the color list
    popColor = colors.pop(0)

    # append the popped color to the end of the list
    colors.append(popColor)

    # loop colors and apply them to pixels
    for x in range(len(pixels):
        pixels[x] = colors[x]
    pixels.show()

    time.sleep(0.1)