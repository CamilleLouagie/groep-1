# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:27:40 2021

@author: Ruben Leenknecht
"""
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


#tijd voor turnleft en right nog aan te passen
#opgepast: bij de meeste functies worden GPIO.output telkens opnieuw geconfigureerd als je ze oproept, maar bij lefmotorspeed en rightmotorspeed niet
#normaal zou dit toch geen probleem mogen opleveren: bij de server doe je telkens stopmotor en bij een kruispunt doe je eerst vooruit



#initialisatiepinnen
#A staat voor motor 1, de linkermotor
#B staat voor motor 2, de rechtermotor
AForwardPin = 31
ABackwardsPin = 33

BForwardPin = 38
BBackwardsPin = 40
EnablePinA = 29
EnablePinB = 36


def motorinitialisatie():
    global pwma
    global pwmb
    GPIO.setup(AForwardPin, GPIO.OUT)
    GPIO.setup(ABackwardsPin, GPIO.OUT)
    GPIO.setup(BForwardPin, GPIO.OUT)
    GPIO.setup(BBackwardsPin, GPIO.OUT)
    GPIO.setup(EnablePinA, GPIO.OUT)
    GPIO.setup(EnablePinB, GPIO.OUT)


    #pwm initialisatie (indien met de L293B kan dit op enable pin )
    pwma = GPIO.PWM(EnablePinA, 100)
    pwmb = GPIO.PWM(EnablePinB, 100)
    
    
    pwma.start(0) #pwm.start(snelheidsfrequentie)
    pwmb.start(0)







#vooruit
def forward(speed = 70):
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    
    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed)




def backwards(speed = 70):
    GPIO.output(AForwardPin, GPIO.LOW)
    GPIO.output(ABackwardsPin, GPIO.HIGH)
    GPIO.output(BForwardPin, GPIO.LOW)
    GPIO.output(BBackwardsPin, GPIO.HIGH)

    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed)


def leftmotorspeed(speed): #voor het PID-algoritme
    pwma.ChangeDutyCycle(speed)

def rightmotorspeed(speed): #voor het PID-algoritme
    pwmb.ChangeDutyCycle(speed)



def turnRight(): #voor de server
    #links vooruit, rechts achteruit
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.LOW)
    GPIO.output(BBackwardsPin, GPIO.HIGH)
    pwma.ChangeDutyCycle(30)
    pwmb.ChangeDutyCycle(30)




def turnRightNinety():
    #links vooruit, rechts achteruit
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.LOW)
    GPIO.output(BBackwardsPin, GPIO.HIGH)
    pwma.ChangeDutyCycle(70)
    pwmb.ChangeDutyCycle(70)
    time.sleep(4.8)
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
        

def turnLeft():
    #links achteruit, rechts vooruit
    GPIO.output(AForwardPin, GPIO.LOW)
    GPIO.output(ABackwardsPin, GPIO.HIGH)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    pwma.ChangeDutyCycle(30)
    pwmb.ChangeDutyCycle(30)

    
def turnLeftNinety():
    #links achteruit, rechts vooruit
    GPIO.output(AForwardPin, GPIO.LOW)
    GPIO.output(ABackwardsPin, GPIO.HIGH)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    pwma.ChangeDutyCycle(70)
    pwmb.ChangeDutyCycle(70)
    time.sleep(2.4)
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
        
    
def stopMotor():
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)

    #herconfigureren voor vooruit
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)



def motorcleanup():
    #stop van het programma
    pwma.stop()
    pwmb.stop()


if __name__ == '__main__':
    motorinitialisatie()

    print("vooruit")
    forward(100)
    time.sleep(5)
    print("achteruit")
    backwards(100)
    time.sleep(5)


    print("linkshoek_negentig")
    turnLeftNinety()
    time.sleep(0.1)

    print("rechtshoek_negentig")
    turnRightNinety()
    time.sleep(2)

    print("links")
    turnLeft()
    time.sleep(2)

    print("rechts")
    turnRight()
    time.sleep(2)

    motorcleanup()