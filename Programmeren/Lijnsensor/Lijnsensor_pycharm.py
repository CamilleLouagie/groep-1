# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:27:09 2021

@author: Ruben Leenknecht
"""


#de datapins moeten nog ingevuld worden en de waarde voor zwart/wit en dat maximale wachttijd en de CALIBRATEDMAX, CALIBDRATEDMIN
#zwart betekent hoge tijd, wit betekent lage tijd


#NUTTIGE COMMANDO: volglijn!!!

import RPI.GPIO as GPIO
from PWM_algoritme.py import leftmotorspeed
from PWM_algoritme.py import rightmotorspeed
import time

GPIO.setmode(GPIO.BOARD)


#pulse_end nog aanpassen voor errors, net zoals time.time()


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
    





def lijndataTabel(): #vul nog de pins in, daarna geeft deze functie een lijst terug met als elementen de tijdsdata per sensor
    #verzamelt sensorendata in een lijst
    pinlijst = [7,8,10,11,12,13,15,16] #vul hier DE PINNUMMERS in
    tijdsdatalijst = []
    for pin in pinlijst:
        tijdsdatalijst.append(leesSensor(pin))

    return tijdsdatalijst










def herschaalwaarde(lijndataTabel, minimum, maximum):  # noteert iedere waarde als een getal tussen 0 en 1000 ("read calibrate")
    # hulpfunctie voor readpositie
    herschaaltabel = []
    for k in range(len(lijndataTabel)):
        herschaaldewaarde = (lijndataTabel[i] - minimum[i]) / (maximum[i] - minimum[i]) * 1000
        if herschaaldewaarde < minimum[i]:
            herschaaldewaarde = minimum[i]
        if herschaaldewaarde > maximum[i]:
            herschaaldewaarde = maximum[i]
        herschaaltabel.append(herschaaldewaarde)
    return herschaaltabel


def readpositie(lijndatatabel, minimum, maximum):
    # gebruikte formule: (0*value0 + 1000*value1+ 2000*value2..) /(value0 + value1 + value2 +...)
    # geeft een waarde voor de positie
    herschaaltabel = herschaalwaarde(lijndatatabel, minimum,maximum)  # geeft tabel met de gekalibreerde waardes: tussen 0 en 1000
    avg = 0
    som = 0
    for i in range(len(herschaaltabel)):
        if herschaaltabel[i] > 50:  # ruis wegwerken
            avg += (i * 1000) * herschaaltabel[i]
            som += herschaaltabel[i]
    if som == 0: #divide by 0
        som =1
    return avg / som





# while True
def lijninterpretatie(): #geeft weer of er een stopstreep is of anders een gewone lijn
    MINIMUM = CALIBRATEDMINIMUM #nog in te vullen
    MAXIMUM = CALIBRATEDMAXIMUM #nog in te vullen
    tijdsdatalijst = lijndataTabel()
    herschaaltabel = herschaalwaarde(tijdsdatalijst, MINIMUM, MAXIMUM)
    zwartewaarden = 0

    for waarde in herschaaltabel:
        if waarde > 500 :
            zwartewaarden += 1
    if zwartewaarden >= 7: # als zeven van de acht sensoren zwart detecteren zijn we al tevreden
        return "stopstreep"
    else:
        return tijdsdatalijst


def volglijn(tijdsdatalijst):
    global last_error
    MINIMUM = CALIBRATEDMINIMUM #nog in te vullen
    MAXIMUM = CALIBRATEDMAXIMUM #nog in te vullen
    KP = #nog in te vullen
    KD = #nog in te vullen
    SETPOINTPOSITIE = 3500 # 3*1000*sensor3 + 4*1000*sensor4 /(sensor3 + sensor 4)
    LINKSBASISSPEED = 50
    RECHTSBASISSPEED = 50



    positie = readpositie(tijdsdatalijst, MINIMUM, MAXIMUM) #de gekalibreerde positiewaarde
    error = positie-SETPOINTPOSITIE
    correctiespeed = KP*error + KD*(error - last_error)
    correctiespeed = 0
    last_error = error

    leftmotorspeed(LINKSBASISSPEED + correctiespeed)
    rightmotorspeed(RECHTSBASISSPEED - correctiespeed)



def zoeklijn():
    MINIMUM = CALIBRATEDMINIMUM  # nog in te vullen
    MAXIMUM = CALIBRATEDMAXIMUM  # nog in te vullen
    tijdsdatalijst = lijndataTabel()
    herschaaltabel = herschaalwaarde(tijdsdatalijst, MINIMUM, MAXIMUM)
    for waarde in herschaaltabel:
        if waarde > 300:
            return True

    return False







while True:
    print(lijndataTabel()) #geeft de tabel met waarden weer
    time.sleep(0.1) #pause for 0,1 second before repeating, use ctrl+z to stop

GPIO.cleanup() 