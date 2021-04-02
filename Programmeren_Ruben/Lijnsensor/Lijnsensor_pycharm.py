# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:27:09 2021

@author: Ruben Leenknecht
"""


#de datapins moeten nog ingevuld worden en de waarde voor zwart/wit en dat maximale wachttijd en de CALIBRATEDMAX, CALIBDRATEDMIN
#zwart betekent hoge tijd, wit betekent lage tijd

#opgelet, vaak worden de pins niet uigelezen, vandaar PULSE_END!!!


#NUTTIGE COMMANDO: volglijn!!!

import RPi.GPIO as GPIO
from PWM_algoritme import leftmotorspeed
from PWM_algoritme import rightmotorspeed
from PWM_algoritme import forward
from PWM_algoritme import backwards
from PWM_algoritme import stopMotor
from PWM_algoritme import motorcleanup
import time

GPIO.setmode(GPIO.BOARD)


#pulse_end nog aanpassen voor errors, net zoals time.time()


def leesSensor(dataPIN): #function to get value from IR sensor
    GPIO.setup(dataPIN, GPIO.OUT) #Set your chosen pin to an output
    GPIO.output(dataPIN, GPIO.HIGH) #turn on the power 5v to the sensor
    time.sleep(0.00001) #opladen 
    pulse_start = time.time() #start the stopwatch
    GPIO.setup(dataPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to pull down to ground 0v
    while GPIO.input(dataPIN)> 0: # and time.time()< 0.5: #NOG AAN TE PASSEN
        pass #wait while the capacitor discharges to zero
        
    if  GPIO.input(dataPIN)==0:
        pulse_end = time.time() #when it hits zero stop the stopwatch

    #als dit wegdoet, werkt het niet meer
    else:
        pulse_end =pulse_start
    tijdsduur= pulse_end - pulse_start
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
    for i in range(len(lijndataTabel)):
        herschaaldewaarde = (lijndataTabel[i] - minimum[i]) / (maximum[i] - minimum[i]) * 1000
        if herschaaldewaarde < 0:
            herschaaldewaarde = 0
        if herschaaldewaarde > 1000:
            herschaaldewaarde = 0
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





def calibrate():
    global CALIBRATEDMAXIMUM
    global CALIBRATEDMINIMUM
    CALIBRATEDMINIMUM = [0.00045800209045410156, 0.00043201446533203125, 0.00043702125549316406, 0.0004038810729980469, 0.0004088878631591797, 0.00042819976806640625, 0.0004119873046875, 0.000431060791015625]
    CALIBRATEDMAXIMUM = [0.0005309581756591797, 0.0005199909210205078, 0.0005052089691162109, 0.0005011558532714844, 0.0005130767822265625, 0.0004990100860595703, 0.0005171298980712891, 0.0004990100860595703]









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
    KP = 0.1 #nog in te vullen
    KD = 0 #nog in te vullen
    SETPOINTPOSITIE = 3500 # 3*1000*sensor3 + 4*1000*sensor4 /(sensor3 + sensor 4)
    LINKSBASISSPEED = 50
    RECHTSBASISSPEED = 50



    positie = readpositie(tijdsdatalijst, MINIMUM, MAXIMUM) #de gekalibreerde positiewaarde
    print(positie)
    error = (positie-SETPOINTPOSITIE)/1000
    print error
    last_error = error

    correctiespeedlinks = LINKSBASISSPEED + KP*error + KD*(error - last_error)
    correctiespeedrechts = RECHTSBASISSPEED - KP*error + KD*(error - last_error)
    if correctiespeedlinks > 100:
        correctiespeedlinks = 100
    if correctiespeedrechts < 0:
        correctiespeedrechts = 0
    if correctiespeedlinks < 0 :
        correctiespeedlinks = 0
    if correctiespeedrechts > 100:
        correctiespeedrechts = 100
    leftmotorspeed(correctiespeedlinks)
    rightmotorspeed(correctiespeedrechts)









def zoeklijn():
    MINIMUM = CALIBRATEDMINIMUM  # nog in te vullen
    MAXIMUM = CALIBRATEDMAXIMUM  # nog in te vullen
    tijdsdatalijst = lijndataTabel()
    herschaaltabel = herschaalwaarde(tijdsdatalijst, MINIMUM, MAXIMUM)
    for waarde in herschaaltabel:
        if waarde > 300:
            return True

    return False






calibrate()
last_error = 0


for k in range(200):
    data = lijndataTabel()
    volglijn(data)

GPIO.cleanup()
motorcleanup()