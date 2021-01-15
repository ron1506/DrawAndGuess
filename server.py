############################################################################
# Basic Server that supports threads
############################################################################
import socket
import threading
from users import Users


class Server(object):

    def __init__(self, ip, port):
        """
        constructor. initializing variables of the class.
        :param ip:
        :param port:
        """
        self.ip = ip
        self.port = port
        self.list_all_clients = []  # creating a list with all client's info.
        self.u = Users

    def start(self):
        """
        building the socket, communicating with the client, the main function.
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
        """

        :param client_socket:
        :param client_address:
        :return:
        """
        while True:
            try:
                request = client_socket.recv(1024).decode()  # getting the coordinates from the client,
                if 'login' in request:  # asks to log in.
                    lst = request.split(" ")
                    if self.u.is_exist(lst[1]):  # לבדוק אם משתמש קיים
                        if self.u.check_password(lst[2]):  # לבדוק אם סיסמה תקינה
                            pass  # sends the client that the client is connected 'true'.
                        else:
                            pass  # sends the client that the password is wrong 'false'.
                    else:
                        pass  # sends the client that user doesn't exist 'false'.
                elif 'register' in request:
                    if (not self.u.is_username_exist(lst[1])) and (not self.u.is_email_exist(lst[3])):
                        self.u.insert_user(lst[1], lst[2], lst[3])
                    else:
                        pass  # sends the server that the username is already taken.
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
