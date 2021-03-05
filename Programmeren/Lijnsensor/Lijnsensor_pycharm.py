# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:27:09 2021

@author: Ruben Leenknecht
"""


#de datapins moeten nog ingevuld worden en de waarde voor zwart/wit en dat maximale wachttijd
#zwart betekent hoge tijd, wit betekent lage tijd


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


def leesSensor(dataPIN): #function to get value from IR sensor
    GPIO.setup(dataPIN, GPIO.OUT) #Set your chosen pin to an output
    GPIO.output(dataPIN, GPIO.HIGH) #turn on the power 5v to the sensor
    time.sleep(0.00001) #opladen 
    pulse_start = time.time() #start the stopwatch
    GPIO.setup(dataPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to pull down to ground 0v
    while GPIO.input(dataPIN)> 0 and time.time()< 0.5: #NOG AAN TE PASSEN
        pass #wait while the capacitor discharges to zero
        
    if  GPIO.input(dataPIN)==0:
        pulse_end = time.time() #when it hits zero stop the stopwatch
    tijdsduur= pulse_end - pulse_start
    print ("tijdsduur:", tijdsduur)
    return tijdsduur
    

def interpreteerTijdsduur(tijdsduur): #maakt van de gevonden tijdsduur een kleur
    if tijdsduur > 0.0006: #adjust this value to change the SENSITIVITY
        colour_seen = "black"
    else:
        colour_seen = "white"
    return colour_seen


def lijndataTabel(): #vul nog de pins in, daarna geeft deze functie een lijst terug met als elementen de tijdsdata per sensor
    #verzamelt sensorendata in een lijst
    pinlijst = [1,2,3,4,5,6,7,8] #vul hier DE PINNUMMERS in
    tijdsdatalijst = []
    for pin in pinlijst:
        tijdsdatalijst.append(leesSensor(pin))

    return tijdsdatalijst



while True:
    print(lijndataTabel()) #geeft de tabel met waarden weer
    time.sleep(0.1) #pause for 0,1 second before repeating, use ctrl+z to stop

GPIO.cleanup() 