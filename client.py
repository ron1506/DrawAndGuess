"""
Made by: Ron Aizen
7th, December 2020
client with threads
"""
#############################################################################
# Client - that connect to the multi-threading server
############################################################################
import socket
from screen import Screen
from surface import Surface


class Client (object):
    def __init__(self, ip, port):
        """
        constructor. initializing variables of the class.
        :param ip:
        :param port:
        """
        self.ip = ip
        self.port = port
        self.start()

    def start(self):
        """
        building the socket, connecting to server, the main function.
        :return:
        """
        try:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating the socket
            sock.connect((ip, port))  # connecting to server
            print('connected to server')  # to see if client connected successfully.
            s = Surface(sock)
            Screen(sock, s.username)  # creating a new screen.
        except socket.error as e:
            print(e)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
