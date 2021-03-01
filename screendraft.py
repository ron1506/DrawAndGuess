from tkinter import *
import threading
import socket


class Screen:
    def __init__(self, socket, username, score):
        self.color = 'black'
        self.strikes = 3
        self.score = score
        self.root2 = Tk()
        self.username = username
        self.cv = Canvas(self.root2, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
        self.root2.resizable(width=FALSE, height=FALSE)
        self.x = 0  # initializing coordinates.
        self.y = 0  # initializing coordinates.
        self.server_socket = socket
        # self.root2.mainloop()
        # self.main()  # calling the main function.

    def send_coordinates(self, event):
        """
        the function sending the coordinates, of the mouse when clicked on the board to the server.
        :param event: when clicking the left button an event is created contains the coordinates of the place.
        :return:
        """
        self.x, self.y = event.x, event.y
        x_and_y = str(self.x) + ";" + str(self.y)
        print("send: ", x_and_y)
        self.server_socket.send(x_and_y.encode())  # sending the server the coordinates.

    def paint(self):
        """
        receiving coordinates from server and painting the screen in black in them.
        :return:
        """
        while True:
            x_and_y = self.server_socket.recv(1024).decode()  # decrypting the data from the server.
            pos = x_and_y.split(";")  # separating x and y
            print("pos ", pos)
            x = int(pos[0])
            y = int(pos[1])
            print("recv: ", x, y)
            self.x, self.y = x, y
            x2, y2 = (x + 1), (y + 1)
            self.cv.create_oval((self.x, self.y, x2, y2), fill='black', width=5)
            # painting the screen in the coordinates.
            # print("other mouse position: (%s %s)" % (x, y))

    def check_guess(self, guess):
        print("got to check guess")
        msg = "guess;" + guess.get() + ";" + self.username
        self.server_socket.send(msg.encode())
        response = str(self.server_socket.recv(1024).decode()).split(";")  # containing whether the guess is true or not and the score
        if response[0] == "True":  # if the guess is empty returning false.
            self.score += response[1]
            self.guess_mode()
        else:
            self.strikes -= 1
            if self.strikes != 0:
                self.guess_mode()

    def draw_mode(self, word):
        headline = Label(self.root2, text=self.username)  # the name of the user on top of the screen.
        headline.pack()
        # print("helloooooooo")

        print("word = ", word)
        red_button = Button(self.root2, command=lambda: self.change_color('red'), bg='red')
        red_button.place(x=450, y=20)
        word_label = Label(self.root2, text="you need to draw: " + word)
        word_label.pack()
        score_headline = Label(self.root2, text='score: ' + str(self.score), font=('bubble', 15),  # the score
                               bg='white', fg="black", relief="solid")  # the title of the screen.
        score_headline.place(x=10, y=50)

        # strikes_headline = Label(text='strikes: ' + str(strikes), font=('bubble', 15),
        #                          bg='white', fg="black", relief="solid")  # the strikes the user have left.
        # strikes_headline.place(x=10, y=20)

        # if left button on the mouse is being clicked, it goes to the function 'send_coordinates '.
        self.cv.bind('<B1-Motion>', self.send_coordinates)
        self.cv.pack(expand=YES, fill=BOTH)
        server_handler = threading.Thread(target=self.paint)
        server_handler.daemon = True
        # creating a thread that handles with the data the server sends to the client, w function 'paint'.
        server_handler.start()
        self.root2.mainloop()
        return self.score

    def guess_mode(self):
        print("into guess mode")
        headline = Label(self.root2, text=self.username)  # the name of the user on top of the screen.
        headline.pack()
        self.cv.pack()
        score_headline = Label(self.root2, text='score: ' + str(self.score), font=('bubble', 15),  # the score
                               bg='white', fg="black", relief="solid")
        score_headline.place(x=10, y=50)
        strikes_headline = Label(self.root2, text='strikes: ' + str(self.strikes), font=('bubble', 15),
                                 bg='white', fg="black", relief="solid")  # the strikes the user have left.
        strikes_headline.place(x=10, y=20)
        guess = Entry(self.root2, relief='solid', font=('bubble', 10), bg='white', fg="black")
        guess.delete(0, END)
        guess.insert(0, 'enter a guess')
        guess.place(x=100, y=400)
        submit_button = Button(self.root2, text="submit", relief="solid",
                               font=('cooper black', 10), fg="black", bg="#%02x%02x%02x" % (255, 255, 255),
                               command=lambda: self.check_guess(guess))
        submit_button.place(x=400, y=400)
        server_handler = threading.Thread(target=self.paint)
        server_handler.daemon = True
        # creating a thread that handles with the data the server sends to the client, w function 'paint'.
        server_handler.start()
        self.root2.mainloop()
        return self.score

    def change_color(self, color):
        self.color = color



























"""def save():
    filename = 'image.png'
    image1.save(filename)


def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=10)


root22 = Tk()

cv = Canvas(root22, width=640, height=480, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
# ----
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root22.mainloop()"""