import Afstandssensor_en_ADC.afstandssensor as adc
from Lijnsensor.Lijnsensor_pycharm import volglijn, lijninterpretatie
from opkuisen import opkuis
from kruispunt import kruispunt
from MotorControl.PWM_algoritme import stopMotor


import RPI.GPIO as GPIO
import time
import spidev
import busio


def main():
    kruispuntnr = 1
    einde = False   # True waarde nog te implementeren
    GPIO.setmode(GPIO.BOARD)

    # SPI-object maken voor afstandssensor
    CE = 0  # Eerste kanaal op ADC selecteren
    spi = spidev.SpiDev0(0, CE)
    spi.max_speed_hz = 1000000
    kanaal = 0  # Eerste analoge signaal

    # Kleurensensor initialiseren
    i2c = busio.I2C(5, 3)
    kleurensensor = adafruit_tcs34725.TCS34725(i2c)

    last_error = 0  # Nodig voor de eerst keer volglijn uit te voeren
    while not einde:
        while True:
            # Manuele override
            message = server.listen()
            if message:
                last_error = 0
                break

            # Volg de lijn 10 keer
            for i in range(10):
                returnwaarde = lijninterpretatie()
                if returnwaarde == "stopstreep":
                    stopMotor()
                    kruispunt(kruispuntnr, kleurensensor, kanaal)
                    kruispuntnr += 1
                    last_error = 0  #Herinitialisatie van lijnvolgalgoritme
                else:
                    volglijn(returnwaarde)

            # Na 10 maal lijn te volgen, check de sensoren
            if adc.getAfstand(kanaal) < 15:
                stopMotor()
                while adc.getAfstand(kanaal) < 20:
                    pass

        #Bericht uitlezen
        while message != 'Ga door':
            # ...
            message = server.listen()

        raise Exception("Fout in de code.")


if __name__ == "__main__":
    # Dit wordt enkel uitgevoerd als het programma uitgevoerd wordt, niet als het geïmporteerd wordt.
    try:
        main()
    except Exception as err:
        print("De volgende fout werd tegengekomen: ", err)
    else:
        print('Geen fout.')
    finally:
        opkuis()
