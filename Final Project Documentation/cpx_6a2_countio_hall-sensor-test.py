# Adafruit hall sensor countio test
# WORKS!

import board
import neopixel
import countio
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = 0.05, auto_write=False)
pixels.fill((0, 0, 255))
pixels.show()

# declare a countio object to count shaft turns
shaft_count = countio.Counter(board.A2)


while True:

    if shaft_count.count >= 192:
        print(shaft_count.count)
        print("1 turn")
        shaft_count.reset()
