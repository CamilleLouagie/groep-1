import afstandssensor as adc
from Lijnsensor_pycharm import volglijn, lijninterpretatie, calibrate, zoeklijn
#from opkuisen import opkuis
from kruispunt import kruispunt
from PWM_algoritme import forward, turnLeft, turnRight, motorinitialisatie, stopMotor, backwards, motorcleanup, rightmotorspeed, leftmotorspeed, turnRightNinety, turnLeftNinety # Een functie voor achterwaarts te gaan moet nog geïmp
from fourierkleurensensor2 import verkeerslicht


import socket
import RPi.GPIO as GPIO
import time
import spidev
import Adafruit_TCS34725

class Server(object):
    """A server to send and receive UDP message. Sending of messages is only
    possible when a message has been received.
    """
    def __init__(self, port=8080, message_size=128):
        """Initialises the Server object

        Parameters
        ----------
        port : type
            The port the server is listening to.
        message_size : type
            The maximum size of a message

        Returns
        -------
        type
            A Server object
        """
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(('', port))
        self._client_adr = None
        self._size = message_size

    def listen(self, timeout=0):
        """Listens to possible clients for a certain duration.

        Parameters
        ----------
        self : type
            The Server object.
        int timeout : type
            The time in seconds to wait on input. If zero (default), it
            listens indefinitely.

        Returns
        -------
        type
            A string with the message or None when nothing was sent.
        """
        self._socket.settimeout(timeout)
        try:
            message, self._client_adr = self._socket.recvfrom(self._size)
        except socket.timeout:
            return None
        return repr(message)

    def send(self, message, timeout=0):
        """Sends a message to the client.

        Parameters
        ----------
        self : Server
            The server object
        message : string
            The message to be sent to the client
        timeout : float
            The time in seconds the Server tries to connect to the client.

        Returns
        -------
        bool
            True if the message was successfully sent, False if partially sent
            or if no message was received (i.e. the _socket is None).

        """
        if self._socket is None:
            return False
        self._socket.settimeout(timeout)
        self._socket.connect(self._client_adr)
        mess_bytes = bytearray(message, 'utf-8')
        for i in range(0, len(mess_bytes), self._size):
            sent = self._socket.send(mess_bytes[i:i+self._size])
            if sent < len(mess_bytes[i:i+self._size]):
                return False
        return True














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
    global override
    override = False
    print('vooruit over stopstreep')

    for i in range(6):

        rightmotorspeed(90)
        leftmotorspeed(80)
        time.sleep(1)
        ber3 = server.listen(timeout=0.250)
        ber3 = str(ber3)
        if ber3.find('start') >= 0:
            override = True
            break

    print('op kruispunt')

    while not zoeklijn() and override == False:
        ber4 = server.listen(timeout=0.250)
        ber4 = str(ber4)
        if ber4.find('start') >= 0:
            override = True
            break

        if adc.getAfstand(kanaal) <= 12:
            print('adc')
            print(adc.getAfstand(kanaal))
            stopMotor()
            time.sleep(2)
        else:
            rightmotorspeed(95)
            leftmotorspeed(30)
            time.sleep(0.2)
            rightmotorspeed(75)
            leftmotorspeed(90)
            time.sleep(0.2)


def rechtsInslaan(kanaal=0, tijd=1):
    global override
    override = False
    print('rechts inslaan')

    rightmotorspeed(90)
    leftmotorspeed(82)
    time.sleep(2)

    time.sleep(tijd)
    stopMotor()
    turnRightNinety()
    stopMotor()

    while not zoeklijn() and override == False:
        ber5 = server.listen(timeout=0.250)
        ber5 = str(ber5)
        if ber5.find('start') >= 0:
            override = True
            break



        if adc.getAfstand(kanaal) <= 12:
            stopMotor()
            time.sleep(1)
        else:

            rightmotorspeed(93)
            leftmotorspeed(30)
            time.sleep(0.2)
            rightmotorspeed(75)
            leftmotorspeed(90)
            time.sleep(0.2)


def linksInslaan(kanaal=0, tijd=3.1):
    print('rechts inslaan')
    global override
    override = False

    rightmotorspeed(90)
    leftmotorspeed(82)
    time.sleep(1)

    if adc.getAfstand(kanaal) <= 12:
        stopMotor()
        time.sleep(2)

    rightmotorspeed(90)
    leftmotorspeed(82)
    time.sleep(tijd)
    stopMotor()
    turnLeftNinety()
    stopMotor()

    while not zoeklijn() and override == False:
        ber5 = server.listen(timeout=0.250)
        ber5 = str(ber5)
        if ber5.find('start') >= 0:
            override = True
            break

        if adc.getAfstand(kanaal) <= 12:
            stopMotor()
            time.sleep(1)
        else:
            forward()
            time.sleep(1)
            rightmotorspeed(93)
            leftmotorspeed(60)
            time.sleep(0.2)
            rightmotorspeed(80)
            leftmotorspeed(90)
            time.sleep(0.2)















def main():

    global server
    global override


    # override is en blijft False totdat er een bericht 'start' binnenkomt uit de manuele override
    override = False
    kruispuntnr = 1
    einde = False   # True waarde nog te implementeren
    GPIO.setmode(GPIO.BOARD)

    # SPI-object maken voor afstandssensor

    CE = 0  # Eerste kanaal op ADC selecteren
    spi = spidev.SpiDev(0, CE)
    spi.max_speed_hz = 1000000
    kanaal = 0  # Eerste analoge signaal

    # Kleurensensor initialiseren
    kleurensensor = Adafruit_TCS34725.TCS34725()

    # Server initialiseren
    server = Server()



    last_error = 0  # Nodig voor de eerst keer volglijn uit te voeren
    while not einde:
        bericht = server.listen(timeout=0.250)
        print(bericht)
        mesg = str(bericht)
        if mesg.find('start') >= 0:
            kruispunt_reserve = kruispuntnr
            override = True

        # Manuele override
        while override:
            msg = str(server.listen(timeout=0.2))
            print(msg)
            if msg.find('vooruit') >= 0:
                forward()
                server.send('Vooruit.')

            elif msg.find('achteruit') >= 0:
                backwards()
                server.send('Achteruit.')

            elif msg.find('links') >= 0:
                turnLeft()
                server.send('Links.')

            elif msg.find('rechts') >= 0:
                turnRight()
                server.send('Rechts.')

            elif msg.find('stop') >= 0:

                kruispunt_manueel = 0
                print(msg[-3])
                print(msg[-2])
                try:
                    cijfer = int(msg[-3])
                    kruispunt_manueel += cijfer * 10
                except:
                    pass

                try:
                    cijfer = int(msg[-2])
                    kruispunt_manueel += cijfer
                except:
                    pass

                if kruispunt_manueel != 0:
                    kruispuntnr = kruispunt_manueel
                else:
                    kruispuntnr = kruispunt_reserve

                finaalBericht = str(kruispuntnr)
                server.send('Kruispunt = ' + finaalBericht)

                override = False

            else:
                server.send(str(kruispuntnr))
                stopMotor()




        # Volg de lijn 20 keer
        for i in range(9):
            #print("lijnvolg")
            returnwaarde = lijninterpretatie()
            if returnwaarde == "stopstreep":
                print("kruispunt")
                stopMotor()
                print(kruispuntnr)
                while True:
                    kleur = verkeerslicht(kleurensensor)
                    if kleur == "groen":
                        break

                    #indien we altijd door rood rijden: bovenstaande 3 lijntjes verwijderen

                    ber = server.listen(timeout=0.200)
                    ber = str(ber)
                    if ber.find('groen') >= 0:
                        break

                    if ber.find('start') >=0:
                        override = True
                        break

                if override == False:
                    kruispunt(kruispuntnr)

                kruispuntnr += 1
                server.send(str(kruispuntnr))
                if kruispuntnr >= 26:
                    einde = True
                    break
                last_error = 0  # Herinitialisatie van lijnvolgalgoritme
            else:
                volglijn(returnwaarde)

        # Na 20 maal lijn te volgen, check de sensoren
        if adc.getAfstand(kanaal) < 15:
            print("afstandssensor")
            stopMotor()
            while adc.getAfstand(kanaal) < 20:
                print('korte afstand')
                bericht_afstand = server.listen(timeout=0.250)
                bericht_afstand = str(bericht_afstand)
                if bericht_afstand.find('start') >= 0:
                    override = True
                    break

                pass

    raise Exception("Fout in de code.")




if __name__ == "__main__":
    # Dit wordt enkel uitgevoerd als het programma uitgevoerd wordt, niet als het geïmporteerd wordt.
    try:
        calibrate()
        motorinitialisatie()
        main()
    except Exception as err:
        print("De volgende fout werd tegengekomen: ", err)
    else:
        print('Geen fout.')
    finally:
        stopMotor()
        motorcleanup()
        GPIO.cleanup()

