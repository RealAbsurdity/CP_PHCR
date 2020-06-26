import time
from adafruit_circuitplayground import cp

while True:
    acclData = tuple(cp.acceleration)

    print(acclData)

    time.sleep(0.01)