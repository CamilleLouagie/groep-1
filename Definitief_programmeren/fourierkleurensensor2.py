import time
from numpy.fft import rfft,rfftfreq
from numpy import abs
import Adafruit_TCS34725

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_TCS34725.TCS34725()
sensor.set_integration_time(0xF6)   # 24 ms
sensor.set_gain(0x01)   # x2 gain


def verkeerslicht(sensor):
    intervalduur = 5
    roodwaarden = []
    while time.time() < intervalduur:
        r,g,b,c = sensor.get_raw_data()
        roodwaarden.append(r)
    mag_rood = [np.abs(nummer) for nummer in rfft(roodwaarden)]
    gemeten_gemiddelde = mean(mag_rood)

    freq_mag_rood = rfftfreq(intervalduur*41,1/41)
    while True:
        i = 0
        if freq_mag_rood[i] == 1:
            mag_1Hz = mag_rood[i]
            break

    # Vergelijken
    if numpy.abs(gemeten_gemiddelde - mag_1Hz) < 5:
        return "groen"

    else:
        return "rood"
