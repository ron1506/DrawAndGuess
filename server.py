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
        self.list_all_clients = []

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
                self.list_all_clients.append([client_socket, client_address])
                print('new client entered')
                self.handle_client(client_socket, client_address)
        except socket.error as e:
            print(e)

    def handle_client(self, client_sock, client_address):
        """
        method that helps the server deal with what the clint sends him.
        :param client_sock:
        :param current:
        :return:
        """
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(client_sock, client_address))
        # without comma you'd get a... TypeError: handle_client_connection()
        # argument after * must be a sequence, not _socketobject
        client_handler.start()

    def handle_client_connection(self, client_socket, client_address):
         while True:
            try:
                request = client_socket.recv(1024)  # getting the coordinates from the client,
                print(self.list_all_clients)
                print(len(self.list_all_clients))
                for i in range(len(self.list_all_clients)):
                    self.list_all_clients[i][0].send(request)
            except Exception as e:
                print(e)


if __name__ == '__main__':
   ip = '0.0.0.0'
   port = 1730
   s = Server(ip, port)
   s.start()
