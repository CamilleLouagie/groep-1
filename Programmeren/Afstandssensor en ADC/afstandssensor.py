# digitale output code = (1024*V_sensor)/V_ADC
# linearisering afstand = ~27 V*cm/V_sensor (we kunnen waarde nog aanpassen en evt. constante toevoegen.)


import spidev
import RPi.GPIO as GPIO
import time

# SPI-object maken

CE = 0  #Eerste kanaal op ADC selecteren
spi = spidev.SpiDev()
spi.open(0, CE)
spi.max_speed_hz = 1000000


# ADC uitlezen
def getWaarden(adcnum):
    if adcnum > 1 or adcnum < 0:    # De ADC heeft maar 2 kanalen CE0 en CE1
        return -1

    r = spi.xfer2([1, 8 + adcnum << 4, 0])  # SPI-transactie van het digitale signaal
    adc_uit = ((r[1] & 3) << 8) + r[2]
    return adc_uit


while True:
    v = getWaarden(0) * (3.3 / 1023.0)  # Zet digitale waarde variërend van 0 tot 1023 om naar volt
    afstand = 27/v  # Eerste versie van de linearisering van de tweede grafiek in de bijgeleverde documenten bij de
                    # sensor, waarschijnlijk nog aan te passen.
    time.sleep(1)
