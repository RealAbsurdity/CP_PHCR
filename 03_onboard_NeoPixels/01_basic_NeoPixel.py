import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0, auto_write=False)

ACORANGE = (252, 70, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORS = [RED, GREEN, BLUE]

while True:

    color = 0
    pixel = 0
    # this is my main loop

    while pixel < 10:
        pixels[pixel] = COLORS[color]
        pixel += 1
        color += 1
        if color > 2:
            color = 0
    pixels.show()