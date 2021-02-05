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
        self.online_users = []  # list of the users that are online
        self.start()

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
        # print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(client_sock, client_address))
        # without comma you'd get a... TypeError: handle_client_connection()
        # argument after * must be a sequence, not _socketobject
        client_handler.start()

    def handle_client_connection(self, client_socket, client_address):
        """
        deals with the connection of the user to the game, helps him to register or to log in.
        :param client_socket:
        :param client_address:
        :return:
        """
        u = Users()
        finished = False
        user_name = ""
        while not finished:
            # print(self.online_users)
            try:
                request = str(client_socket.recv(1024).decode())  # getting the coordinates from the client,
                print(request)
                lst = request.split(" ")
                if lst[0] == 'login':  # asks to log in.
                    # print("got to login")

                    if u.to_log_in(lst[1], lst[2]) and not  self.is_online(lst[1]):  #  לבדוק אם משתמש קיים וסיסמה תקינה ולא מחובר
                        # print("user should be appended")
                        user_name = lst[1]
                        self.online_users.append((user_name, client_socket))
                        client_socket.send("True".encode())  # sends the client that the client is connected 'true'.
                    else:
                        # print("user should not be appended")
                        # sends the client that the username\ email\ password is wrong 'false'.
                        client_socket.send("False".encode())
                elif lst[0] == 'register':
                    # print("got to register")
                    if u.to_register(lst[1], lst[2], lst[3]):
                        user_name = lst[1]
                        self.online_users.append((user_name, client_socket))
                        client_socket.send("True".encode())
                    else:
                        client_socket.send("False".encode())  # sends the client that the username is already taken.
                else:
                    # print(self.list_all_clients)
                    # print(len(self.list_all_clients))
                    for i in range(len(self.online_users)):
                        self.online_users[i][1].send(request.encode())
            except Exception as e:
                finished = True
                if user_name != "":
                    self.online_users.remove(user_name)
                print(e)

            print(self.online_users)

    def is_online(self, username):
        """
        checking if the username is in the list of the online clients.
        :param username: the username of the user that attempting to connect
        :return: true if online, false otherwise.
        """
        for i in self.online_users:
            if username in i:
                return True
        return False


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 1730
    s = Server(ip, port)
