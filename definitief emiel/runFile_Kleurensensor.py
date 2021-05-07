# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:34:49
2021

@author: otto.meerschman
"""

import time
import Adafruit_TCS34725

import RPi.GPIO as GPIO
import numpy as np

GPIO.setmode(GPIO.BOARD)

sensor = Adafruit_TCS34725.TCS34725()
print(sensor.get_gain())
sensor.set_gain(0x02)
print(sensor.get_gain())
print(sensor.get_integration_time())
sensor.set_integration_time(0xF6)
print(sensor.get_integration_time())

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
    r, g, b, c = sensor.get_raw_data()  # of rgb_golor_bytes
    RGB= rgb_color_bytes

    if RGB[1]> r and g > b and g > c:
        time.sleep(1)
        if g < 50: #kan aangepast worden
            time.sleep(1)
            if g > r and g > b and g > c:
                return 'groen'
    if g < 50:
        time.sleep(1)
        if g > r and g > b and g > c:
            time.sleep(1)
            if g < 50:
                return 'rood'

    else:
        return 'rood'

start = time.time()
waarden = []
while (time.time() - start) < 120:
    waarden.append(sensor.get_raw_data()[0])

print(waarden)