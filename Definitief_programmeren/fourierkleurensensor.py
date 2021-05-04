"""
Op basis van groenwaarden lukt een onderscheidt maken niet. Daarom dacht ik om een cyclus volledig uit te meten in 4 delen.
We meten in blokken van 5 seconden. We kunnen op die manier via fourier de gemiddelde magnitude per blok berekenen. Indien
het eerste blok de laagste gemiddelde magnitude voor rood heeft dan mag de robot meteen na de meting vertrekken. Maw de wachttijd
is dus 5*("nummer van het laatste blok") seconden indien groen tussen 2 blokken. Indien volledig in 1 blok, wachttijd is
dan 5*("nummer van het blok") - 2.5 seconden.
"""

import numpy as np
from scipy.fft import rfft, rfftfreq
import time
import Adafruit_TCS34725
import matplotlib.pyplot as plt

#import RPi.GPIO as GPIO


#GPIO.setmode(GPIO.BOARD)

#sensor = Adafruit_TCS34725.TCS34725()
#sensor.set_gain(0x01)


def getOverallMagnitude(datalist):
    """
    SAMPLE_RATE NOG TE BEPALEN (aantal datapunten voor 1 Hz), DURATION IS 5 (s)

    Berekent het gemiddelde van de magnitude (mate van wat de hoogste waarde is voor rood). Moet 4 keer gerund worden
    om een cyclus lang te analyseren.
    """
    DURATION = 5
    SAMPLE_RATE = 1000
    N = SAMPLE_RATE * DURATION      # Aantal datasamples in de toon

    fourierdata = rfft(datalist)
    #frequentiedata = rfftfreq(N, 1/SAMPLE_RATE)
    magnitudedata = []
    for element in fourierdata:
        magnitudedata += np.absolute(element)

    gemmagnitude = mean(magnitudedata)

    return gemmagnitude


"""def meetCyclus(sensor):
    blokkenlijst = []
    delay = 1/20    # meten in 4 blokken van 5 seconden indien cyclus = 20 sec
    for i in range(3):
        close_time = time.time() + delay
        bloklijst = []
        while close_time > time.time():
            tempdata = sensor.get_raw_data()
            bloklijst.append(tempdata[0])
            time.sleep(0.001)                   # Sample-rate van 1000
        blokkenlijst.append(bloklijst)

    return blokkenlijst
"""

def berekenMagnitudes(blokkenlijst):
    magnitude1 = getOverallMagnitude(blokkenlijst[0])
    magnitude2 = getOverallMagnitude(blokkenlijst[1])
    magnitude3 = getOverallMagnitude(blokkenlijst[2])
    magnitude4 = getOverallMagnitude(blokkenlijst[3])

    return [magnitude1,magnitude2,magnitude3,magnitude4]


def interpretatie(magnitudelijst):
    # Blok 1
    if magnitudelijst[0] < magnitudelijst[1] and magnitudelijst[0] < magnitudelijst[3]:
        return [1]
    elif magnitudelijst[0] < magnitudelijst[1] and magnitudelijst[3] < magnitudelijst[2] and magnitudelijst[3] < magnitudelijst[1]:
        return [1,4]
    elif magnitudelijst[0] < magnitudelijst[3] and magnitudelijst[1] < magnitudelijst[2] and magnitudelijst[1] < magnitudelijst[3]:
        return [1,2]

    # Blok 2
    if magnitudelijst[1] < magnitudelijst[2] and magnitudelijst[1] < magnitudelijst[0]:
        return [2]
    elif magnitudelijst[1] < magnitudelijst[2] and magnitudelijst[0] < magnitudelijst[3] and magnitudelijst[0] < \
            magnitudelijst[2]:
        return [1, 2]
    elif magnitudelijst[1] < magnitudelijst[0] and magnitudelijst[2] < magnitudelijst[3] and magnitudelijst[2] < \
            magnitudelijst[0]:
        return [2, 3]

    # Blok 3
    if magnitudelijst[2] < magnitudelijst[3] and magnitudelijst[2] < magnitudelijst[1]:
        return [3]
    elif magnitudelijst[2] < magnitudelijst[3] and magnitudelijst[1] < magnitudelijst[0] and magnitudelijst[1] < \
            magnitudelijst[3]:
        return [2, 3]
    elif magnitudelijst[2] < magnitudelijst[1] and magnitudelijst[3] < magnitudelijst[0] and magnitudelijst[3] < \
            magnitudelijst[1]:
        return [3, 4]

    # Blok 4
    if magnitudelijst[3] < magnitudelijst[0] and magnitudelijst[3] < magnitudelijst[2]:
        return [4]
    elif magnitudelijst[3] < magnitudelijst[0] and magnitudelijst[2] < magnitudelijst[1] and magnitudelijst[2] < \
            magnitudelijst[0]:
        return [3, 4]
    elif magnitudelijst[3] < magnitudelijst[2] and magnitudelijst[0] < magnitudelijst[1] and magnitudelijst[0] < \
            magnitudelijst[2]:
        return [4, 1]


def berekenWachttijd(interpretatielijst):
    if interpretatielijst == [4,1]:
        return 0
    if len(interpretatielijst) == 1:
        return interpretatielijst[0]*5-2.5
    else:
        return interpretatielijst[1]*5


def leesKleurenUit(sensor):
    """
    Return de tijd dat de auto moet wachten aan het kruispunt nadat hij een volledige cyclus heeft gemeten.
    """
    return berekenWachttijd(interpretatie(berekenMagnitudes(meetCyclus(sensor))))



if __name__ == '__main__':
    roodlist = []
    inputlist = [(41, 30, 26, 64),
    (41, 30, 26, 64),
    (45, 33, 28, 71),
    (47, 33, 29, 72),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 72),
    (47, 33, 29, 73),
    (45, 33, 29, 71),
    (45, 33, 29, 71),
    (45, 33, 29, 72),
    (45, 33, 29, 72),
    (45, 33, 29, 71),
    (45, 33, 29, 72),
    (45, 33, 29, 71),
    (45, 33, 29, 71),
    (45, 33, 29, 71),
    (45, 33, 29, 72),
    (46, 33, 29, 72),
    (45, 33, 29, 72),
    (45, 33, 29, 72),
    (45, 33, 29, 71),
    (46, 33, 29, 71),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (47, 34, 30, 74),
    (47, 34, 29, 73),
    (47, 34, 30, 74),
    (47, 34, 30, 74),
    (47, 34, 30, 73),
    (47, 34, 29, 73),
    (47, 34, 30, 73),
    (47, 34, 30, 73),
    (47, 33, 29, 73),
    (47, 33, 29, 73),
    (48, 34, 30, 77),
    (49, 35, 30, 77),
    (49, 35, 31, 77),
    (49, 35, 31, 77),
    (49, 35, 31, 78),
    (49, 35, 31, 78),
    (49, 35, 31, 77),
    (49, 35, 31, 77),
    (45, 35, 30, 73),
    (45, 35, 30, 74),
    (45, 35, 30, 74),
    (45, 35, 30, 74),
    (45, 35, 30, 73),
    (45, 35, 30, 74),
    (46, 35, 30, 73),
    (45, 35, 30, 74),
    (45, 35, 30, 74),
    (45, 35, 30, 74),
    (45, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (45, 35, 30, 74),
    (46, 35, 30, 74),
    (45, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 75),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 75),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 74),
    (46, 35, 30, 75),
    (46, 35, 31, 74),
    (46, 35, 30, 75),
    (46, 35, 30, 75),
    (46, 35, 30, 74),
    (50, 35, 31, 78),
    (50, 36, 31, 79),
    (50, 35, 31, 79),
    (50, 35, 31, 79),
    (50, 35, 31, 79),
    (50, 35, 31, 78),
    (50, 35, 31, 78),
    (50, 36, 31, 79),
    (50, 36, 31, 78),
    (50, 36, 31, 79),
    (50, 35, 31, 79),
    (50, 36, 31, 78),
    (50, 35, 31, 78),
    (50, 36, 31, 79),
    (50, 36, 31, 78),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 35, 31, 78),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 78),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 78),
    (46, 36, 31, 75),
    (47, 36, 31, 75),
    (46, 36, 31, 75),
    (47, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (47, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (47, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (50, 36, 31, 79),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 35, 31, 75),
    (46, 35, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75),
    (46, 36, 31, 75),
    (46, 36, 31, 75),
    (46, 35, 31, 75)]
    for element in inputlist:
        roodlist.append(element[0])
    roodlist = roodlist[:15]
    xlist = np.arange(len(roodlist))
    plt.plot(xlist, roodlist)
    plt.show()
    plt.plot(rfftfreq(15,1),np.abs(rfft(roodlist)))
    plt.show()

    x = np.linspace(0, 5, 10*5, endpoint=False)
    y = np.sin(2* np.pi * x)
    plt.plot(x, y)
    plt.show()
    plt.plot(rfftfreq(10*5,1/10),np.abs(rfft(y)))
    plt.show()
