from Kleurensensor import detectiekleuren
import PWM_algoritme as motor
from Lijnsensor_pycharm import zoeklijn
import afstandssensor as adc
import time


def kruispunt(nummer):
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
        motor.forward(30)

    while not zoeklijn():
        while adc.getAfstand(kanaal) <= 12:
            motor.stopMotor()
            time.sleep(1)
        motor.forward(30)


def rechtsInslaan(kanaal, tijd=2):
    while zoeklijn():
        motor.forward(30)

    motor.forward(30)

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
        motor.forward(30)


def linksInslaan(kanaal, tijd=3):
    while zoeklijn():
        motor.forward(30)

    motor.forward(30)

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
        motor.forward(30)
