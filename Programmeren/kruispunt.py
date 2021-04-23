from Kleurensensor.Kleurensensor import detectiekleuren
import MotorControl.PWM_algoritme as motor
from Lijnsensor.Lijnsensor_pycharm import zoeklijn
import Afstandssensor_en_ADC.afstandssensor as adc
import time


def kruispunt(nummer, kleurensensor, kanaal):
    # Wanneer rood
    while detectiekleuren(kleurensensor) == 'rood':
        pass

    # Wanneer groen
    #bij elk kruispuntnummer moet oversteken(), rechtsInslaan() of linksInslaan() gebruikt worden
    if nummer == 1:
        pass
    elif nummer == 2:
        pass
    elif nummer == 3:
        pass
    elif nummer == 4:
        pass
    elif nummer == 5:
        pass
    elif nummer == 6:
        pass
    elif nummer == 7:
        pass
    elif nummer == 8:
        pass
    elif nummer == 9:
        pass
    elif nummer == 10:
        pass
    elif nummer == 11:
        pass
    elif nummer == 12:
        pass
    elif nummer == 13:
        pass
    elif nummer == 14:
        pass
    elif nummer == 15:
        pass
    elif nummer == 16:
        pass
    elif nummer == 17:
        pass
    elif nummer == 18:
        pass
    elif nummer == 19:
        pass
    elif nummer == 20:
        pass
    elif nummer == 21:
        pass
    elif nummer == 22:
        pass
    elif nummer == 23:
        pass
    elif nummer == 24:
        pass
    elif nummer == 25:
        pass


def oversteken(kanaal):
    while zoeklijn():
        motor.forward(10)

    while not zoeklijn():

        motor.forward(30)

        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()

def rechtsInslaan(kanaal):
    while zoeklijn():
        motor.forward(10)

    while not zoeklijn():

        motor.forward(30)
        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
        time.sleep(0.2)
        motor.turnRightNinety()
        motor.forward(30)
        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()

def linksInslaan(kanaal):
    while zoeklijn():
        motor.forward(10)

    while not zoeklijn():

        motor.forward(30)
        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
        time.sleep(0.2)
        motor.turnLeftNinety()
        motor.forward(30)
        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
