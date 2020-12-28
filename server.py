############################################################################
# Basic Server that supports threads
############################################################################
import socket
import threading
import random
import datetime


class Server(object):

    def __init__(self, ip, port):
        """
        constructor
        :param ip:
        :param port:
        """
        self.ip = ip
        self.port = port

    def start(self):
        """
        building the socket, communicating with the client
        :return:
        """
        try:
           print('server starts up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((self.ip, self.port))  # connecting to client
           sock.listen(3)
           while True:
                print('waiting for a new client')
                client_socket, client_address = sock.accept()
                print('new client entered')
                self.handle_client(client_socket)
        except socket.error as e:
            print(e)

    def handle_client(self, client_sock):
        """
        method that helps the server deal with what the clint sends him.
        :param client_sock:
        :param current:
        :return:
        """
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(client_sock,))
        # without comma you'd get a... TypeError: handle_client_connection()
        # argument after * must be a sequence, not _socketobject
        client_handler.start()

    @staticmethod
    def handle_client_connection(client_socket):
         while True:
            request = client_socket.recv(1024).decode()
            x, y = request.split(" ")
            x = int(x)
            y = int(y)


if __name__ == '__main__':
   ip = '0.0.0.0'
   port = 1730
   s = Server(ip, port)
   s.start()
