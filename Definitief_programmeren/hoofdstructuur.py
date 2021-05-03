import afstandssensor as adc
from Lijnsensor_pycharm import volglijn, lijninterpretatie, calibrate
#from opkuisen import opkuis
from kruispunt import kruispunt
from PWM_algoritme import forward, turnLeft, turnRight, motorinitialisatie, stopMotor, backwards, motorcleanup # Een functie voor achterwaarts te gaan moet nog geïmp
from Kleurensensor import detectiekleuren

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



def main():

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
        bericht = server.listen(timeout=0.01)
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
        for i in range(20):
            print("lijnvolg")
            returnwaarde = lijninterpretatie()
            print(returnwaarde)
            if returnwaarde == "stopstreep":
                print("kruispunt")
                stopMotor()

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
                print('nog steeds')
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

