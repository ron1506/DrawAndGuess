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
        self.count = 0

    def start(self):
        """
        building the socket, communicating with the client
        :return:
        """
        try:
           print('server starts up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((self.ip, self.port))
           sock.listen(3)
           while True:
                print('waiting for a new client')
                # block
                client_socket, client_address = sock.accept()

                print('new client entered')

                # send receive example
                client_socket.sendall('Hello this is server'.encode())
                msg = client_socket.recv(1024).decode()
                print('received message: %s' % msg)

                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handle_client(client_socket, self.count)
        except socket.error as e:
            print(e)

    def handle_client(self, client_sock, current):
        """
        method that helps the server deal with what the clint sends him.
        :param client_sock:
        :param current:
        :return:
        """
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(client_sock, current,))
        # without comma you'd get a... TypeError: handle_client_connection()
        # argument after * must be a sequence, not _socketobject
        client_handler.start()

    @staticmethod
    def handle_client_connection(client_socket, current):
         while True:
            print("start")
            request = client_socket.recv(1024).decode()
            if request.upper() == "RND":
                client_socket.send(str(random.randint(0, 100)).encode())
            elif request.upper() == "TIME":
                client_socket.send(str(datetime.datetime.now().time()).encode())

            elif request.upper() == "DATE":
                client_socket.send(str(datetime.datetime.now().date()).encode())
            else:
                client_socket.sendall(request.encode())
            print('Received {}'.format(request))


if __name__ == '__main__':
   ip = '0.0.0.0'
   port = 1730
   s = Server(ip, port)
   s.start()
