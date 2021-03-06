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
    pwma = GPIO.PWM(EnablePinA, 150)
    pwmb = GPIO.PWM(EnablePinB, 150)
    
    
    pwma.start(0) #pwm.start(snelheidsfrequentie)
    pwmb.start(0)







#vooruit
def forward(speed = 82):
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    
    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed + 6.9)



def backwards(speed = 80):
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
    pwma.ChangeDutyCycle(80)
    pwmb.ChangeDutyCycle(80)




def turnRightNinety():
    #links vooruit, rechts achteruit
    GPIO.output(AForwardPin, GPIO.HIGH)
    GPIO.output(ABackwardsPin, GPIO.LOW)
    GPIO.output(BForwardPin, GPIO.LOW)
    GPIO.output(BBackwardsPin, GPIO.HIGH)
    pwma.ChangeDutyCycle(70)
    pwmb.ChangeDutyCycle(70)
    time.sleep(1.70)
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
        

def turnLeft():
    #links achteruit, rechts vooruit
    GPIO.output(AForwardPin, GPIO.LOW)
    GPIO.output(ABackwardsPin, GPIO.HIGH)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    pwma.ChangeDutyCycle(70)
    pwmb.ChangeDutyCycle(70)

    
def turnLeftNinety():
    #links achteruit, rechts vooruit
    GPIO.output(AForwardPin, GPIO.LOW)
    GPIO.output(ABackwardsPin, GPIO.HIGH)
    GPIO.output(BForwardPin, GPIO.HIGH)
    GPIO.output(BBackwardsPin, GPIO.LOW)
    pwma.ChangeDutyCycle(70)
    pwmb.ChangeDutyCycle(70)
    time.sleep(1.40)
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



#motorinitialisatie()

#forward(10)
#time.sleep(10)
#motorcleanup()