# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:34:49
2021

@author: otto.meerschman
"""

import time
import Adafruit_TCS34725

import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_TCS34725.TCS34725()
#sensor.set_gain(0x02)
sensor.set_integration_time(0xF6)

def detectiekleuren(sensor):
    """Leest de kleursensor uit en geeft een string terug naarmate de kleur groen of rood is.

    Parameters
    ----------
    sensor: TCS34725-object
        de sensor die de data inleest

    Returns
    -------
    string
        'groen' als de gedetecteerde kleur groen is, 'rood' als de gedetecteerde kleur rood is .

    """

    while True:
        vorige_data = []
        r, g, b, c = sensor.get_raw_data()  # of rgb_golor_bytes
        print(r,g,b,c)
        vorige_data.append(r)
        vorige_data.append(g)
        vorige_data.append(b)
        vorige_data.append(c)
        r, g, b, c = sensor.get_raw_data()

        if g - vorige_data[1] >= 5 and r - vorige_data[0] < 5:
            break


if __name__ == '__main__':
    detectiekleuren(sensor)
