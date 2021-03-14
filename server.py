############################################################################
# Basic Server that supports threads
############################################################################
import socket
import threading
from users import Users
import random
import time


class Server(object):
    def __init__(self, ip, port):
        """
        constructor. initializing variables of the class.
        :param ip:
        :param port:
        """
        self. gussed_correctly = []
        self.word = ""
        self.list_of_words = ['banana', 'ice cream', 'chocolate', 'apple', 'ball']  # list of items
        self.ip = ip  # the ip of the server 0.0.0.0
        self.port = port  # the port of the server 1730
        self.list_all_clients = []  # creating a list with all client's info.
        self.online_users = []  # list of the users that are online
        self.online_players = []  # list of the users that play in the game
        self.game_thread = threading.Thread(target=self.game)
        self.daemon = True
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
            self.game_thread.start()
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
                request = str(client_socket.recv(1024).decode())
                # getting a request from the client, either log in or registers separated by ';'.
                # print(request)
                lst = request.split(";")
                if lst[0] == 'login':  # asks to log in.
                    # print("got to login")
                    if u.to_log_in(lst[1], lst[2]) and not self.is_online(
                            lst[1]):  # לבדוק אם משתמש קיים וסיסמה תקינה ולא מחובר
                        # print("user should be appended")
                        user_name = lst[1]
                        self.online_users.append((user_name, client_socket))
                        # adds the user to the list of online clients.
                        client_socket.send("True".encode())  # sends the client that the user is connected,'true'.
                        finished = True
                    else:
                        # print("user should not be appended")
                        # sends the client that the username\ email\ password is wrong 'false'.
                        client_socket.send("False".encode())  # sends the client that the user isn't connected,'false'.
                elif lst[0] == 'register':  # the user asks to register.
                    # print("got to register")
                    if u.to_register(lst[1], lst[2], lst[3]):  # לבדוק אם משתמש ודוא"ל לא קיימים וניתן להירשם
                        user_name = lst[1]
                        self.online_users.append((user_name, client_socket))
                        finished = True
                        # adds the user to the list of online clients.
                        client_socket.send("True".encode())  # sends the client that the user is connected,'true'.
                    else:
                        client_socket.send("False".encode())
                        # sends the client that the username/mail is already taken.
            except Exception as e:
                finished = True
                if user_name != "":  # if the user quit, then he is removed from the list of online users.
                    self.online_users.remove((user_name, client_socket))
                print(e)

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

    def game(self):
        """
        chooses the drawer and notifies him.
        :return:
        """
        finish = False
        while not finish:
            if len(self.online_users) >= 2:
                for i in range(len(self.online_users)):  # 80 sec
                    finish = True
                    self.online_players = self.online_users[:]
                    print("lets play")
                    drawer = self.online_players[random.choice([i for i in range(len(self.online_players))])] #  tuple (username,socket)
                    for player in self.online_players:
                        player[1].send("play".encode())

                    self.word = self.choose_word()
                    for user in self.online_players:
                        if user[0] == drawer[0]:
                            user[1].send(('draw;'+self.word).encode())
                            drawer_thread = threading.Thread(target=self.handle_drawer, args=(user[1],))
                            drawer_thread.start()
                            # self.handle_drawer(self.online_players, user[1])
                        else:
                            user[1].send(('guess;'+self.word).encode())
                            guess_thread = threading.Thread(target=self.handle_guesser, args=(user[1], drawer[1]))
                            guess_thread.start()
                            # self.handle_guesser(user[1])
                    time.sleep(80)

    def choose_word(self):
        """
        chooses a word from the list of the words that exists.
        :return:
        """
        return random.choice(self.list_of_words)

    def handle_drawer(self, client_socket):
        # print(len(self.list_all_clients))
        finish = False
        while not finish:
            try:
                request = str(client_socket.recv(1024).decode())  # getting the coordinates from the client,
                for i in self.online_players:
                    i[1].send(request.encode())
            except ConnectionResetError:
                finish = True
                for i in self.online_players:
                    if i[1] == client_socket:
                        self.online_players.remove(i)
                for j in self.online_users:
                    if j[1] == client_socket:
                        self.online_users.remove(j)

    def handle_guesser(self, guesser_socket, drawer_socket):
        print("handling guesser")
        finish = False
        # while not finish:
        did_guess = False
        number_guesses = 0
        while not did_guess and number_guesses < 3 and not finish:
            print("I am in loop")
            try:
                request = guesser_socket.recv(1024).decode()  # if guessed correctly or not
                number_guesses += 1
                print(request)
                lst = request.split(";")
                if lst[0] == 'True':
                    self.gussed_correctly.append(lst[1])
                    score = (3 - len(self.gussed_correctly)) * 25
                    guesser_socket.send(('score;' + str(score)).encode())
                    drawer_socket.send(('score;' + str(30)).encode())
                    did_guess = True
                else:
                    guesser_socket.send(('score;' + str(0)).encode())
            except ConnectionResetError:
                print("an error occurred")
                finish = True
                for i in self.online_players:
                    if i[1] == guesser_socket:
                        self.online_players.remove(i)
                for j in self.online_users:
                    if j[1] == guesser_socket:
                        self.online_users.remove(j)


if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 1730
    s = Server(ip, port)
