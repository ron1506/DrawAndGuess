"""
Made by: Ron Aizen
7th, December 2020
client with threads
"""
#############################################################################
# Client - that connect to the multi-threading server
############################################################################
import socket
from typing import List
from tkinter import *
import numpy as np
from screen import Screen


class Client (object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.start()

    def start(self):
        """
        connecting to server.
        :return:
        """
        try:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))  # connecting to server
            print('connected to server')
            Screen(sock)
        except socket.error as e:
            print(e)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
