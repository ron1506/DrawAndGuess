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


class Client (object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        # Create a 500 by 500 matrix occupied by lists of 3 values representing an rgb value
        # initialized with [255, 255, 255] (white)
        self.pixels = np.full((500, 500, 3), 255)
        self.root = Tk()
        # creating a blank white canvas, size: 1000x1000.
        self.cv = Canvas(self.root, width=500, height=500, bg='white')
        self.root.mainloop()

    def paint(self, event):
        """

        :param event: contains the mouse x and y coordinates.
        :return: painting the screen in black in the requested coordinates.
        """
        x1, y1 = event.x, event.y  # start coordinates.
        x2, y2 = (event.x + 1), (event.y + 1)  # end coordinates.
        self.cv.create_line((x1, y1, x2, y2), fill='black', width=5)
        self.pixels[x1, y1] = [0, 0, 0]

    def start(self):
        """
        connecting to server.
        :return:
        """
        try:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024).decode()
            print('received message: %s' % msg)
            sock.sendall('Hello this is client'.encode())
            # implement here your main logic
            while True:
                self.handle_server_job(sock)
        except socket.error as e:
            print(e)

    def handle_server_job(self, server_socket):
        """
        deals with the server job.
        sending info, and receiveing.
        :param serverSocket:
        :return:
        """
        while True:
            # if left button on the mouse is being clicked, it goes to the function 'paint'.
            self.cv.bind('<Button-1>', self.paint)
            print('connecting to ip %s port %s' % (ip, port))
            self.cv.bind('<B1-Motion>', self.paint)
            self.cv.pack(expand=YES, fill=BOTH)
            x = input("print something")
            server_socket.send(x.encode())
            m = server_socket.recv(1024).decode()
            print(m)
            if m == 'finish':
                return 'finish'


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
    c.start()