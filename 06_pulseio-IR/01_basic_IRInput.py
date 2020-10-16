# basic program strcuture for CPE

# import modules
import board
import time
import pulseio
import adafruit_irremote

# declare objects and variables
irIn = pulseio.PulseIn(board.A1, maxlen=120, idle_state=True)

decoder = adafruit_irremote.GenericDecode()

# repeat forever
while True:
    # gather input
    pulses = decoder.read_pulses(irIn)
    """
    note:
    decoder.read_pulses(pin) will block further code execution by default
    add ,blocking=False) to prevent this behavior.
    """
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

        """
        note:
        Continue will stop code BELOW the continue statement from executing.
        To change this behavior alter it to: pass to allow code below to execute\.
        """

    print("NEC Infrared code received: ", incomingCode)
