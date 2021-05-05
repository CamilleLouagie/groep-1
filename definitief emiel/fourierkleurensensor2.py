import time
import numpy as np
import Adafruit_TCS34725

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_TCS34725.TCS34725()
sensor.set_integration_time(0xF6)   # 24 ms
sensor.set_gain(0x02)   # x2 gain


def verkeerslicht(sensor):
    intervalduur = 5
    roodwaarden = []
    starttijd = time.time()
    while (time.time() - starttijd) < intervalduur:
        r,g,b,c = sensor.get_raw_data()
        roodwaarden.append(r)
    mag_rood = [np.abs(nummer) for nummer in np.fft.rfft(roodwaarden)]
    gemeten_gemiddelde = np.mean(mag_rood)
    print(gemeten_gemiddelde)

    freq_mag_rood = np.fft.rfftfreq(intervalduur*41,1/41)

    for i in range(len(freq_mag_rood)):
        if freq_mag_rood[i] == 1:
            mag_1Hz = mag_rood[i]
            break

    print(mag_1Hz)

    # Vergelijken
    print(gemeten_gemiddelde - mag_1Hz)
    print()
    """
    if numpy.abs(gemeten_gemiddelde - mag_1Hz) < 5:
        return "groen"

    else:
        return "rood"
"""

while True:
    verkeerslicht(sensor)