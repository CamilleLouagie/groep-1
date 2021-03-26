from Kleurensensor.Kleurensensor import detectiekleuren
import MotorControl.PWM_algoritme as motor
from Lijnsensor.Lijnsensor_pycharm import zoeklijn
import Afstandssensor_en_ADC.afstandssensor as adc


def kruispunt(nummer, kleurensensor, kanaal):
    # Wanneer rood
    while detectiekleuren(kleurensensor) == 'rood':
        pass

    # Wanneer groen
    if nummer == 1:     # Check op berichten halverwege algoritme

        while not zoeklijn():
            # Check op manuele override
            motor.forward(30)
            while adc.getAfstand(kanaal) <= 12:
                motor.stopMotor()


    elif nummer == 2:
        pass
    elif nummer == 3:
        pass
    elif nummer == 4:
        pass
    elif nummer == 5:
        pass

    # ...



