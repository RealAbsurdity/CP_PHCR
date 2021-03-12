import board
import touchio
import neopixel
import time
import digitalio
import random
pix = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.1)
button_a = digitalio.DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=digitalio.Pull.DOWN)
button_pre = False
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
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)
GameON = False
GAMEOVER = False
GAMESCORESHOW = False
PLIST = [pix[0], pix[2], pix[4], pix[5], pix[7], pix[9]]
ClearList = [CLEAR, CLEAR, CLEAR, CLEAR, CLEAR, CLEAR]
EndOfGAMEOVER = 0
EndOfSCORESHOW = 0
p1Count = 0
p2Count = 0
p3Count = 0
p4Count = 0
p5Count = 0
p6Count = 0
p1itime = 0
p2itime = 0
p3itime = 0
p4itime = 0
p5itime = 0
p6itime = 0
Life = 9
Score = 0
Setter = True
Setter2 = True
CounterList = [p1Count, p2Count, p3Count, p4Count, p5Count, p6Count]
IndicatorList = [p1itime, p2itime, p3itime, p4itime, p5itime, p6itime]
while True:
    # when button a is pressed and released, set game mode
    if button_a.value != button_pre:
        button_pre = button_a.value
        if button_a.value:
            GameON = not GameON

    # read touch input to a list
    for x in range(6):
        touchValue[x] = touchPin[x].value

    # if game mode ON, run the code
    if GameON:
        # when the current time is over the time set for light start
        if time.monotonic() >= p1Count:
            # if touch pin 1 and pixel is currently BLUE
            # light change to green
            # and set indicator timer to current time + 2
            # and get +1 score
            if t1.value and pix[9] == BLUE:
                pix[9] = GREEN
                p1itime = time.monotonic() + 2
                Score += 1
            # when current time = end of indicator time
            # set the light to CLEAR
            if int(time.monotonic()) == int(p1itime):
                p1Count = time.monotonic() + random.randint(3, 5)
            # indicator time only reset when player act
            # so current time before the indicator time reset
            # will be always greater than indicator time
            # and set the period of time after light up
            # and before indicator time reset as BLUE
            elif time.monotonic() > p1itime:
                pix[9] = BLUE
            # if 5 second after the light and it is still BLUE
            # reset the indicator timer and set it to red
            # and get - 1 life
            # when three life is used, player will game over
            if time.monotonic() > p1Count + 5 and pix[9] == BLUE:
                pix[9] = RED
                p1itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[9] = CLEAR
        # for pix 7 and pin 2
        if time.monotonic() >= p2Count:
            if t2.value and pix[7] == BLUE:
                pix[7] = GREEN
                p2itime = time.monotonic() + 2
                Score += 1
            if int(time.monotonic()) == int(p2itime):
                p2Count = time.monotonic() + random.randint(3, 5)
            elif time.monotonic() > p2itime:
                pix[7] = BLUE
            if time.monotonic() > p2Count + 5 and pix[7] == BLUE:
                pix[7] = RED
                p2itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[7] = CLEAR
        # for pix 5 and pin 3
        if time.monotonic() >= p3Count:
            if t3.value and pix[5] == BLUE:
                pix[5] = GREEN
                p3itime = time.monotonic() + 2
                Score += 1
            if int(time.monotonic()) == int(p3itime):
                p3Count = time.monotonic() + random.randint(3, 5)
            elif time.monotonic() > p3itime:
                pix[5] = BLUE
            if time.monotonic() > p3Count + 5 and pix[5] == BLUE:
                pix[5] = RED
                p3itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[5] = CLEAR
        # for pix 4 and pin 4
        if time.monotonic() >= p4Count:
            if t4.value and pix[4] == BLUE:
                pix[4] = GREEN
                p4itime = time.monotonic() + 2
                Score += 1
            if int(time.monotonic()) == int(p4itime):
                p4Count = time.monotonic() + random.randint(3, 5)
            elif time.monotonic() > p4itime:
                pix[4] = BLUE
            if time.monotonic() > p4Count + 5 and pix[4] == BLUE:
                pix[4] = RED
                p4itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[4] = CLEAR
        # for pix 2 and pin 5
        if time.monotonic() >= p5Count:
            if t5.value and pix[2] == BLUE:
                pix[2] = GREEN
                p5itime = time.monotonic() + 2
                Score += 1
            if int(time.monotonic()) == int(p5itime):
                p5Count = time.monotonic() + random.randint(3, 5)
            elif time.monotonic() > p5itime:
                pix[2] = BLUE
            if time.monotonic() > p5Count + 5 and pix[2] == BLUE:
                pix[2] = RED
                p5itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[2] = CLEAR
        # for pix 0 and pin 6
        if time.monotonic() >= p6Count:
            if t6.value and pix[0] == BLUE:
                pix[0] = GREEN
                p6itime = time.monotonic() + 2
                Score += 1
            if int(time.monotonic()) == int(p6itime):
                p6Count = time.monotonic() + random.randint(3, 5)
            elif time.monotonic() > p6itime:
                pix[0] = BLUE
            if time.monotonic() > p6Count + 5 and pix[0] == BLUE:
                pix[0] = RED
                p6itime = time.monotonic() + 2
                Life -= 1
        else:
            pix[0] = CLEAR
        if Life < 1:
            if time.monotonic() > IndicatorList[0]:
                GameON = False
                GAMEOVER = True
    # when game is not ON, set all light to off and reset all timer to 0
    # reset life and score and reopen the initializer setter
    # life is set to 9 because when game start, the current time
    # will always be over 0 and will light up as red and reset timer
    # so it is a simple way to indicate game is ON
    # and give random openingt time to the lights
    if not GameON:
        # when game is OFF and GAMEOVER is True
        # Flase red for 2 second and enable Score show
        if GAMEOVER:
            for x in range(10):
                pix[x] = CLEAR
            for x in range(10):
                pix[x] = RED
            if Setter:
                EndOfGAMEOVER = int(time.monotonic() + 2)
                print(EndOfGAMEOVER)
                Setter = False
            if int(time.monotonic()) == EndOfGAMEOVER:
                GAMEOVER = False
                GAMESCORESHOW = True
                Setter2 = True
                print(GAMESCORESHOW)
                print(Setter2)
        # when score show is enabled, Flash to show score
        elif GAMESCORESHOW:
            # if score over 100, it will be orange for all pix
            if Score > 100:
                for x in range(10):
                    pix[x] = ORANGE
            # if Over 10, for each 10 score it will flase yellow
            elif Score > 10:
                for x in range(10):
                    pix[x] = CLEAR
                for x in range(int(Score / 10)):
                    pix[x] = YELLOW
            # if less than 10, nothing will happen
            else:
                for x in range(10):
                    pix[x] = CLEAR
            if Setter2:
                EndOfSCORESHOW = int(time.monotonic() + 2)
                print(EndOfSCORESHOW)
                Setter2 = False
            if int(time.monotonic()) == EndOfSCORESHOW:
                GAMESCORESHOW = False
        else:
            # when game is completely OFF, reset all data
            for x in range(10):
                pix[x] = CLEAR
            p1Count = 0
            p2Count = 0
            p3Count = 0
            p4Count = 0
            p5Count = 0
            p6Count = 0
            p1itime = 0
            p2itime = 0
            p3itime = 0
            p4itime = 0
            p5itime = 0
            p6itime = 0
            Life = 9
            Score = 0
            Setter = True
    time.sleep(0.01)