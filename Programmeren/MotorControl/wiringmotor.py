

import RPi.GPIO as GPIO
import time
import wiringpi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# initialisatiepinnen
# A staat voor motor 1, de linkermotor
# B staat voor motor 2, de rechtermotor
AForwardPin = 1
ABackwardsPin = 23
BForwardPin = 29
BBackwardsPin = 31


# EnablePinA =
# EnablePinB =




def motorinitialisatie():
    global pwma
    global pwmb
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(AForwardPin, 2)  # PWM mode
    wiringpi.pinMode(ABackwardsPin, 1)

    wiringpi.pwmWrite(AForwardPin, 0)




# vooruit
def forward(speed=60):
    # GPIO.output(AForwardPin, GPIO.HIGH)
    # GPIO.output(ABackwardsPin, GPIO.LOW)
    # GPIO.output(BForwardPin, GPIO.HIGH)
    # GPIO.output(BBackwardsPin, GPIO.LOW)

    wiringpi.pwmWrite(AForwardPin, 0)
    print("vooruit")
    time.sleep(5)

    wiringpi.pwmWrite(AForwardPin, 0)
    time.sleep(5)


motorinitialisatie()
wiringpi.pwmWrite(AForwardPin, 0)
