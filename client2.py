#############################################################################
# Client - that connect to the multi-threading server
############################################################################
import socket


class Client (object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        try:
            print('connecting to ip %s port %s' % (ip, port))
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            print('connected to server')
            # send receive example
            msg = sock.recv(1024).decode()
            print('received message: %s' % msg)
            sock.sendall('Hello this is client'.encode())
            #implement here your main logic
            while True:
                self.handleServerJob(sock)
        except socket.error as e:
            print(e)

    def handleServerJob(self, serverSocket):
        while True:
            x = input("print someting")
            serverSocket.send(x.encode())
            m = serverSocket.recv(1024).decode()
            print(m)
            if m == 'finish':
                return 'finish'


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 1730
    c = Client(ip, port)
    c.start()
