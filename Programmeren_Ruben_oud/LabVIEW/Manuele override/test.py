import time
import socket


override = False
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
            True if the message was succesfuly sent, False if partially sent
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

#aanmaken van server
server = Server()


while True:
    kruispuntnr = 3
    bericht = server.listen(timeout=0.01)
    if bericht == "b'start'":
        kruispunt_reserve = kruispuntnr
        override = True
    else:
        None
    while override == True:
        mess = server.listen(timeout=0.2)
        if mess is not None:
            message = mess
            print(mess)
            # server.send(message)
            if mess == "b'vooruit'":
                server.send('Vooruit.')
            elif mess == "b'achteruit'":
                server.send('Achteruit.')
            elif mess == "b'links'":
                server.send('Links.')
            elif mess == "b'rechts'":
                server.send('Rechts.')
            elif mess == "b'linksvooruit'":
                server.send('Linksvooruit.')
            elif mess == "b'linksachteruit'":
                server.send('Linksachteruit')
            elif mess == "b'rechtsvooruit'":
                server.send('Rechtsvooruit.')
            elif mess == "b'rechtsachteruit'":
                server.send('Rechtsachteruit')
            elif mess[0:6] == "b'stop":
                server.send('Succesvol gestopt.')
                kruispunt_manueel = 0
                cijfer = 0
                print(mess[-3])
                print(mess[-2])
                try:
                    cijfer = int(mess[-3])
                    kruispunt_manueel += cijfer*10
                except:
                    None


                cijfer = 0

                try:
                    cijfer = int(mess[-2])
                    kruispunt_manueel += cijfer
                except:
                    None


                if kruispunt_manueel != 0:
                    kruispuntnr = kruispunt_manueel
                else:
                    kruispuntnr = kruispunt_reserve
                finaalBericht = str(kruispuntnr)
                server.send('Kruispunt = ' + ' ' + finaalBericht)
                override = False
            else:
                None
