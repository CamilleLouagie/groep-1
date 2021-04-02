import RPi.GPIO as GPIO
import time

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
    GPIO.setup(AForwardPin, GPIO.OUT)
    GPIO.setup(ABackwardsPin, GPIO.OUT)
    GPIO.setup(BForwardPin, GPIO.OUT)
    GPIO.setup(BBackwardsPin, GPIO.OUT)
    # GPIO.setup(EnablePinA, GPIO.OUT)
    # GPIO.setup(EnablePinB, GPIO.OUT)

    # pwm initialisatie (indien met de L293B kan dit op enable pin )
    # pwma = GPIO.PWM(EnablePinA, 100)
    # pwmb = GPIO.PWM(EnablePinB, 100)

    # met de DRV:
    pwma = GPIO.PWM(AForwardPin, 100)  # (pinnumber, frequentie)
    pwmb = GPIO.PWM(BForwardPin, 100)

    pwma.start(0)  # pwm.start(snelheidsfrequentie)
    pwmb.start(0)


# vooruit
def forward(speed=60):
    # GPIO.output(AForwardPin, GPIO.HIGH)
    # GPIO.output(ABackwardsPin, GPIO.LOW)
    # GPIO.output(BForwardPin, GPIO.HIGH)
    # GPIO.output(BBackwardsPin, GPIO.LOW)

    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed)
    time.sleep(5)

motorinitialisatie()
forward(100)

pwma.ChangeDutyCycle(0)
pwmb.ChangeDutyCycle(0)