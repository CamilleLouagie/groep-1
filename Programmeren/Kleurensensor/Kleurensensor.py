# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:34:49 2021

@author: otto.meerschman
"""

import time
import Adafruit_TCS34725

import RPi.GPIO as GPIO
import busio

GPIO.setmode(GPIO.BOARD)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tcs34725.TCS34725(i2c)
def functie():# functie die zegt wanneer moet detecteren = wanneer aan stoplijn

    return  # true of false


def detectiekleuren(sensor, functie):
    while functie == true:
        r, g, b, c = sensor.get_raw_data()  # of rgb_golor_bytes

        if g > r and g > b and g > c:
            time.sleep(1)
            if g < 50: #kan aangepast worden
                time.sleep(1)
                if g > r and g > b and g > c:
                    return true

        else:
            return false
         