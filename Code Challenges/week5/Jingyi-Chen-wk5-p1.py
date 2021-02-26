import board
import neopixel
import analogio
import time
from simpleio import map_range
pix = neopixel.NeoPixel(board.NEOPIXEL, 10)
analog_in = analogio.AnalogIn(board.A1)
LDR_in = analogio.AnalogIn(board.A6)
color = (0, 0, 0)

smooth_val = analog_in.value
LDR_S = LDR_in.value
def weightedSmooth(in_val, weight):
    global smooth_val
    smooth_val = weight * in_val + ((1-weight) * smooth_val)
    return smooth_val
def weightedSmooth2(in_val, weight):
    global LDR_S
    LDR_S = weight * in_val + ((1-weight) * LDR_S)
    return LDR_S

while True:
    reading = analog_in.value
    LDR_R = LDR_in.value
    LDR_S = weightedSmooth2(LDR_R, 0.2)
    smooth_val = weightedSmooth(reading, 0.2)
    Brightness = map_range(LDR_S, 0, 65535, 0, 255)
    Brightness *= 0.01
    scaled_val = map_range(smooth_val, 0, 65535, 0, 255)
    scaled_val = int(scaled_val)
    color = (0, scaled_val, 150)
    pix.fill(color)
    brightness = Brightness
    print(brightness)
    time.sleep(0.05)