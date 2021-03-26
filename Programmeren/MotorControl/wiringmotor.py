

import RPi.GPIO as GPIO
import time
import wiringpi

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# initialisatiepinnen
# A staat voor motor 1, de linkermotor
# B staat voor motor 2, de rechtermotor
AForwardPin = 33
ABackwardsPin = 32
BForwardPin = 29
BBackwardsPin = 31


# EnablePinA =
# EnablePinB =




def motorinitialisatie():
    global pwma
    global pwmb
    wiringpi.wiringPiSetup()
    wiringpi.pinMode(AForwardPin, 2)  # PWM mode

    GPIO.setup(ABackwardsPin, GPIO.OUT)

    wiringpi.pwmWrite(AForwardPin, 0)




# vooruit
def forward(speed=60):
    # GPIO.output(AForwardPin, GPIO.HIGH)
    # GPIO.output(ABackwardsPin, GPIO.LOW)
    # GPIO.output(BForwardPin, GPIO.HIGH)
    # GPIO.output(BBackwardsPin, GPIO.LOW)

    wiringpi.pwmWrite(AForwardPin, 100)
    print("vooruit")
    time.sleep(5)

    wiringpi.pwmWrite(AForwardPin, 20)
    time.sleep(5)


motorinitialisatie()
forward(100)
