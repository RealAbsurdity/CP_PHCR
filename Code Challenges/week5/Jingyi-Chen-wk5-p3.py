import board
import touchio
import neopixel
import time
import random
pix = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)

touchValue = [False, False, False, False, False, False]
t1 = touchio.TouchIn(board.A1)
t2 = touchio.TouchIn(board.A2)
t3 = touchio.TouchIn(board.A3)
t4 = touchio.TouchIn(board.A4)
t5 = touchio.TouchIn(board.A5)
t6 = touchio.TouchIn(board.A6)
touchPin = [t1, t2, t3, t4, t5, t6]
CLEAR = (0, 0, 0)
BLUE = (0, 0, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GameON = False
PLIST = [pix[0], pix[2], pix[4], pix[5], pix[7], pix[9]]
p1Count = 0
p1indicatortime = 0
while True:
    if t1.value:
        pix[9] = GREEN
    if t2.value:
        pix[7] = GREEN
    if t3.value:
        pix[5] = GREEN
    if t4.value:
        pix[4] = GREEN
    if t5.value:
        pix[2] = GREEN
    if t6.value:
        pix[0] = GREEN
    for x in range(6):
        touchValue[x] = touchPin[x].value
    if GameON:
        if time.time() >= p1Count:
            if t1.value and pix[9] == BLUE:
                pix[9] = GREEN
                p1indicatortime = time.time() + 2
            if time.time() == p1indicatortime:
                p1Count = time.time() + random.randint(3, 5)
            elif time.time() > p1indicatortime:
                pix[9] = BLUE
            if time.time() > p1Count + 5 and pix[9] == BLUE:
                pix[9] = RED
                p1indicatortime = time.time() + 2
        else:
            pix[9] = CLEAR
    time.sleep(0.01)