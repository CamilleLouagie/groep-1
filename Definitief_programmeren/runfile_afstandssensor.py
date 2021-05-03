# digitale output code = (1024*V_sensor)/V_ADC
# linearisering afstand = ~27 V*cm/V_sensor (we kunnen waarde nog aanpassen en evt. constante toevoegen.)

import spidev
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


# SPI-object maken

CE = 0  #Eerste kanaal op ADC selecteren
spi = spidev.SpiDev(0,CE)
spi.max_speed_hz = 1000000
kanaal = 0


# ADC uitlezen
def getAfstand(adcnum):
    if adcnum != 0:    # De ADC heeft maar 2 kanalen CE0 en CE1
        adcnum = 1

    # SPI bericht
    # Eerste bit (Start): Logic high (1)
    # Tweede bit (SGL/DIFF): 1 want enkele modus
    # Derde bit (ODD/SIGN): Selecteer kanaal (0 or 1)
    # Vierde bit (MSFB): 0 for LSB first
    # Next 12 bits: 0 (niet belangrijk)
    bericht = 0b11
    bericht = ((bericht << 1) + adcnum ) << 5
    bericht = [bericht, 0b00000000]
    antwoord = spi.xfer2(bericht)

    # Converteren naar enkele waarde uit antwoord (2 bytes)
    adc = 0
    for n in antwoord:
        adc = (adc << 8) + n

    # Laatste bit is geen ADC waarde
    adc = adc >> 1

    # Voltage berekenen op basis van de digitale waarde
    voltage = (3.3 * adc)/1024

    # Eerste versie van de linearisering van de tweede grafiek in de bijgeleverde documenten bij de sensor,
    # waarschijnlijk nog aan te passen.
    if voltage == 0:
        return 0
    else:
        afstand = 27/voltage
        return afstand

def printAfstand(adcnum):
    print(getAfstand(adcnum))

while True:
    input('enter: ')
    for i in range(100):
        printAfstand(0)