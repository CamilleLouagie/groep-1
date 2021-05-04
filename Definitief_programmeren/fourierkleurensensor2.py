import time
from scipy import rfft
from numpy import abs
import Adafruit_TCS34725

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_TCS34725.TCS34725()
sensor.set_integration_time(0xF6)   # 24 ms
sensor.set_gain(0x01)   # x2 gain


def verkeerslicht(sensor):
    intervaldict = {}
    for i in range(4):
        intervalduur = 5
        roodwaarden = []
        while time.time() < intervalduur:
            r,g,b,c = sensor.get_raw_data()
            roodwaarden.append(r)
        mag_rood = (np.abs(nummer) for nummer in rfft(roodwaarden))
        intervaldict[i+1] = mag_rood

        mag_123 = []
        for j in range(1,4):
            mag_123 += intervaldict[j]

        if numpy.abs(mean(mag_123) - mean(intervaldict[4])) > 4:   # 4 kan nog aangepast worden naarmate de gevoeligheid
            return 'groen'                              # van de sensor hoger wordt gezet of niet

        else:
            pass
            # Ka