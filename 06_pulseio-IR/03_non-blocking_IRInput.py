# program to read IR pulses from an IR sensor
# will NOT prevent code below Try: Except: from executing
# this is a more robust and controlled way to read the IR sensor

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
    # READ the IR Sensor input
    pulses = decoder.read_pulses(irIn, blocking=False)

    if pulses != None:
        print("Pulse received:", '\n', pulses)

        # then try to use the adafruit_irremote library to decode the pulses!
        try:
            incomingCode = decoder.decode_bits(pulses)  # Attempt to convert received pulses into numbers
        except adafruit_irremote.IRNECRepeatException:
            print("NEC repeat!")   # We got an unusual short code, probably a 'repeat' signal
        except adafruit_irremote.IRDecodeException as e:
            print("Failed to decode: ", e.args)  # Something got distorted or maybe its not an NEC-type remote?
        except:
            # a generic catch-all for other exceptions, pass here
            print("unknown exception")
            pass

        if incomingCode != None:
            # IF THE CODE IS NOT EMPTY, PRINT IT
            print("NEC Infrared code received:", '\n', incomingCode)
            # THEN reset the incomingCode to 0
            incomingCode = None