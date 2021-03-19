# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:27:40 2021

@author: Ruben Leenknecht
"""
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


#initialisatiepinnen
#A staat voor motor 1, de linkermotor
#B staat voor motor 2, de rechtermotor
AForwardPin = 33
ABackwardsPin = 32
BForwardPin = 29
BBackwardsPin = 31
#EnablePinA =
#EnablePinB =


def motorinitialisatie():
    global pwma
    global pwmb
    GPIO.setup(AForwardPin, GPIO.OUT)
    GPIO.setup(ABackwardsPin, GPIO.OUT)
    GPIO.setup(BForwardPin, GPIO.OUT)
    GPIO.setup(BBackwardsPin, GPIO.OUT)
    #GPIO.setup(EnablePinA, GPIO.OUT)
    #GPIO.setup(EnablePinB, GPIO.OUT)


    #pwm initialisatie (indien met de L293B kan dit op enable pin )
    #pwma = GPIO.PWM(EnablePinA, 100)
    #pwmb = GPIO.PWM(EnablePinB, 100)
    
    #met de DRV:
    pwma = GPIO.PWM(AForwardPin, 100) # (pinnumber, frequentie)
    pwmb = GPIO.PWM(BForwardPin, 100)
    
    
    pwma.start(0) #pwm.start(snelheidsfrequentie)
    pwmb.start(0)







#vooruit
def forward(speed = 60):
    #GPIO.output(AForwardPin, GPIO.HIGH)
    #GPIO.output(ABackwardsPin, GPIO.LOW)
    #GPIO.output(BForwardPin, GPIO.HIGH)
    #GPIO.output(BBackwardsPin, GPIO.LOW)
    
    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed)



def backwards(speed = 20):
    #GPIO.output(AForwardPin, GPIO.LOW)
    #GPIO.output(ABackwardsPin, GPIO.HIGH)
    #GPIO.output(BForwardPin, GPIO.LOW)
    #GPIO.output(BBackwardsPin, GPIO.HIGH)
    pwma.ChangeDutyCycle(speed)
    pwmb.ChangeDutyCycle(speed)

def leftmotorspeed(speed):
    pwma.ChangeDutyCycle(speed)

def rightmotorspeed(speed):
    pwmb.ChangeDutyCycle(speed)





def turnRightNinety():
    #links vooruit, rechts achteruit
    #GPIO.output(AForwardPin, GPIO.HIGH)
    #GPIO.output(ABackwardsPin, GPIO.LOW)
    #GPIO.output(BForwardPin, GPIO.LOW)
    #GPIO.output(BBackwardsPin, GPIO.HIGH)
    pwma.ChangeDutyCycle(20)
    pwmb.ChangeDutyCycle(20)
    time.sleep(0.5)
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
        
    
    
def turnLeftNinety():
    #links achteruit, rechts vooruit
    #GPIO.output(AForwardPin, GPIO.LOW)
    #GPIO.output(ABackwardsPin, GPIO.HIGH)
    #GPIO.output(BForwardPin, GPIO.HIGH)
    #GPIO.output(BBackwardsPin, GPIO.LOW)
    pwma.ChangeDutyCycle(20)
    pwmb.ChangeDutyCycle(20)
    time.sleep(0.5)
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)
        
    
def stopMotor():
    pwma.ChangeDutyCycle(0)
    pwmb.ChangeDutyCycle(0)



def motorcleanup():
    #stop van het programma
    pwma.stop()
    pwmb.stop()
    pwm.cleanup()