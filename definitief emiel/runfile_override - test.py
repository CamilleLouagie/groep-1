#from PWM_algoritme import forward, turnLeft, turnRight, motorinitialisatie, stopMotor, backwards, motorcleanup # Een functie voor achterwaarts te gaan moet nog geïmp
import socket
#import RPi.GPIO as GPIO
#import time

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


server = Server()
override = False
while True:
    bericht = server.listen(timeout=0.250)
    print(bericht)
    print('bericht')
    mesg = str(bericht)
    if mesg.find('start') >= 0:
        override = True

    # Manuele override
    while override:
        msg = str(server.listen(timeout=0.2))
        print(msg)
        if msg.find('vooruit') >= 0:
            #forward()
            server.send('Vooruit.')

        elif msg.find('achteruit') >= 0:
            #backwards()
            server.send('Achteruit.')

        elif msg.find('links') >= 0:
            #turnLeft()
            server.send('Links.')

        elif msg.find('rechts') >= 0:
            #turnRight()
            server.send('Rechts.')

        elif msg.find('stop') >= 0:
            #stopMotor()
            override = False
            
        else:
            #stopMotor()



