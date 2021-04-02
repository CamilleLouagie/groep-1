import RPi.GPIO as GPIO
#from PWM_algoritme import leftmotorspeed
#from PWM_algoritme.py import rightmotorspeed
import time

GPIO.setmode(GPIO.BOARD)


#pulse_end nog aanpassen voor errors, net zoals time.time()


def leesSensor(dataPIN):  # function to get value from IR sensor
    GPIO.setup(dataPIN, GPIO.OUT)  # Set your chosen pin to an output
    GPIO.output(dataPIN, GPIO.HIGH)  # turn on the power 5v to the sensor
    time.sleep(0.00001)  # opladen
    pulse_start = time.time()  # start the stopwatch
    GPIO.setup(dataPIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # set pin to pull down to ground 0v
    while GPIO.input(dataPIN) > 0: #and time.time() < 0.5:  # NOG AAN TE PASSEN
        pass  # wait while the capacitor discharges to zero

    if GPIO.input(dataPIN) == 0:
        pulse_end = time.time()  # when it hits zero stop the stopwatch
    tijdsduur = pulse_end - pulse_start
    print ("tijdsduur:", tijdsduur)
    return tijdsduur


def lijndataTabel():  # vul nog de pins in, daarna geeft deze functie een lijst terug met als elementen de tijdsdata per sensor
    # verzamelt sensorendata in een lijst
    pinlijst = [7, 8, 10, 11, 12, 13, 15, 16]  # vul hier DE PINNUMMERS in, pin 7 is nummer 8 van het bord en 16 is nummer1
    tijdsdatalijst = []
    for pin in pinlijst:
        tijdsdatalijst.append(leesSensor(pin))

    return tijdsdatalijst

print(lijndataTabel())