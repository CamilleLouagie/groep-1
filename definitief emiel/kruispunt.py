from Kleurensensor import detectiekleuren
import PWM_algoritme as motor
from Lijnsensor_pycharm import zoeklijn
import afstandssensor as adc
import time


def kruispunt(nummer):
    # Wanneer groen
    #bij elk kruispuntnummer moet oversteken(), rechtsInslaan() of linksInslaan() gebruikt worden
    if nummer == 1:
        oversteken()

    elif nummer == 2:
        linksInslaan()

    elif nummer == 3:
        linksInslaan()

    elif nummer == 4:
        rechtsInslaan()

    elif nummer == 5:
        rechtsInslaan()

    elif nummer == 6:
        rechtsInslaan()

    elif nummer == 7:
        oversteken()

    elif nummer == 8:
        linksInslaan()

    elif nummer == 9:
        linksInslaan()

    elif nummer == 10:
        oversteken()

    elif nummer == 11:
        linksInslaan()

    elif nummer == 12:
        linksInslaan()

    elif nummer == 13:
        linksInslaan()

    elif nummer == 14:
        rechtsInslaan()

    elif nummer == 15:
        rechtsInslaan()

    elif nummer == 16:
        oversteken()

    elif nummer == 17:
        rechtsInslaan()

    elif nummer == 18:
        oversteken()

    elif nummer == 19:
        rechtsInslaan()

    elif nummer == 20:
        oversteken()

    elif nummer == 21:
        rechtsInslaan()

    elif nummer == 22:
        linksInslaan()

    elif nummer == 23:
        oversteken()

    elif nummer == 24:
        oversteken()

    elif nummer == 25:
        linksInslaan()

    elif nummer == 26:
        rechtsInslaan()


def oversteken(kanaal=0):
    print('vooruit over stopstreep')
    motor.rightmotorspeed(90.5)
    motor.leftmotorspeed(82)
    time.sleep(3)
    print('uit zoeklijn')

    while not zoeklijn():
        while adc.getAfstand(kanaal) <= 12:
            print('adc')
            print(adc.getAfstand(kanaal))
            motor.stopMotor()
            time.sleep(1)
        motor.rightmotorspeed(90)
        motor.leftmotorspeed(82)


def rechtsInslaan(kanaal=0, tijd=1):
    motor.rightmotorspeed(90)
    motor.leftmotorspeed(82)
    time.sleep(2)

    while adc.getAfstand(kanaal) <= 12:
        motor.stopMotor()
        time.sleep(1)

    time.sleep(tijd)
    motor.stopMotor()
    motor.turnRightNinety()
    motor.stopMotor()

    while not zoeklijn():

        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
            time.sleep(1)
        motor.rightmotorspeed(90)
        motor.leftmotorspeed(82)


def linksInslaan(kanaal=0, tijd=3.4):
    motor.rightmotorspeed(90)
    motor.leftmotorspeed(82)
    time.sleep(3)

    while adc.getAfstand(kanaal) <= 12:
        motor.stopMotor()
        time.sleep(1)

    time.sleep(tijd)
    motor.stopMotor()
    motor.turnLeftNinety()
    motor.stopMotor()

    while not zoeklijn():

        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
            time.sleep(1)
        motor.rightmotorspeed(90)
        motor.leftmotorspeed(82)

