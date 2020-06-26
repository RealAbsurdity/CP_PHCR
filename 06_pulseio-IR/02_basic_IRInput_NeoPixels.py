# basic program strcuture for CPE

# import modules
import board
import time
import pulseio
import adafruit_irremote
import neopixel

# declare objects and variables
irIn = pulseio.PulseIn(board.A1, maxlen=120, idle_state=True)

decoder = adafruit_irremote.GenericDecode()

# constants to compare incomingCodes against
NEC_PWR = [255, 0, 157, 98]

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

# pixel colors
WHITE = (255, 255, 255)
CLEAR = (0, 0, 0)

color = CLEAR

lightMode = False


# repeat forever
while True:
    # gather input
    pulses = decoder.read_pulses(irIn)
    # print the raw pulses for educational value
    print(pulses)
    # then try to use the adafruit_irremote library to decode the pulses!
    try:
        # Attempt to convert received pulses into numbers
        incomingCode = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        print("NEC repeat!")
        continue
    except adafruit_irremote.IRDecodeException as e:
        # Something got distorted or maybe its not an NEC-type remote?
        print("Failed to decode: ", e.args)
        continue

    print("NEC Infrared code received: ", incomingCode)

    # do calculations
    if incomingCode == NEC_PWR:
        lightMode = not lightMode

    # do output
    if lightMode is True:
        color = WHITE
    else:
        color = CLEAR

    pixels.fill(color)