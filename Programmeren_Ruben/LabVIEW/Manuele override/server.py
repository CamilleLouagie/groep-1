#! /usr/bin/python3
"""Contains the Server object. When this file is executed, it listens for five
seconds and, if a message is received, responds with 'message received'.  """
import socket
import time

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

if __name__ == "__main__":
    server = Server()
    while True:
        mess = server.listen(timeout=0.2)
        if mess is not None:
            message = mess
            print(mess)
            # server.send(message)
            if mess == "b'vooruit'" or mess == "b'achteruit'":
                server.send('5')
            elif mess == "b'links'":
                server.send('1.5')
            elif mess == "b'linksvooruit'" or mess == "b'linksachteruit'":
                server.send('3.5')
            elif mess == "b'rechtsvooruit'" or mess == "b'rechtsachteruit'":
                server.send('6.5')
            elif mess == "b'rechts'":
                server.send('8.5')
            else:
                None


