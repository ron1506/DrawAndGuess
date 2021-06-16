from tkinter import *
import threading
import socket
import time


class Screen:
    def __init__(self, socket, username, mode, word, score=0, game_number=1):
        self.color = 'black'
        self.strikes = 3
        self.score = score
        self.game_number = game_number
        self.root2 = Tk()
        self.username = username
        self.cv = Canvas(self.root2, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
        self.root2.resizable(width=FALSE, height=FALSE)
        self.x = 0  # initializing coordinates.
        self.y = 0  # initializing coordinates.
        self.server_socket = socket
        self.word = word
        if mode == "draw":
            self.draw_mode()
        else:
            self.guess_mode()
        self.root2.mainloop()

    def timer(self, seconds=80):
        if seconds >= 0:
            timer_label = Label(self.root2, text=str(seconds), font=('bubble', 15), bg='white', width=5)
            timer_label.place(x=235, y=40)
            self.root2.after(1000, lambda: self.timer(seconds-1))
        else:
            self.between_rounds_screen()

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
            try:
                x = int(pos[0])
                y = int(pos[1])
                print("recv: ", x, y)
                self.x, self.y = x, y
                x2, y2 = (x + 1), (y + 1)
                self.cv.create_oval((self.x, self.y, x2, y2), fill='black', width=5)
            except ValueError:
                self.score += int(pos[1])
                score_headline = Label(self.root2, text='score: ' + str(self.score), font=('bubble', 15),  # the score
                                       bg='white', fg="black", relief="solid")
                score_headline.place(x=10, y=50)
            # painting the screen in the coordinates.
            # print("other mouse position: (%s %s)" % (x, y))

    def check_guess(self, guess):
        print("got to check guess")
        print("word", self.word)
        print("guess", guess.get())
        if guess.get() == self.word:
            self.server_socket.send(('True;' + self.username).encode())
            self.clear_screen()
            # saying that the game has ended.
            you_guessed_correctly = Label(self.root2, text=' you guessed the word correctly!!', font=('bubble', 15),
                                     bg='white', fg="navy", relief="solid")
            you_guessed_correctly.place(x=150, y=200)
            you_guessed_correctly.after(1500, you_guessed_correctly.destroy)
            self.clear_screen()
            round_finish_label = Label(self.root2, text="ROUND IS OVER", font=('bubble', 15))
            round_finish_label.pack(padx=100, pady=100)
        else:
            self.server_socket.send(('False;' + self.username).encode())
            self.strikes -= 1
            you_guessed_wrongfully = Label(self.root2, text=' you guessed the word incorrectly!!', font=('bubble', 15),
                                     bg='white', fg="red", relief="solid")
            you_guessed_wrongfully.place(x=150, y=200)
            you_guessed_wrongfully.after(1500, you_guessed_wrongfully.destroy)
            strikes_headline = Label(self.root2, text='strikes: ' + str(self.strikes), font=('bubble', 15),
                                     bg='white', fg="black", relief="solid")  # the strikes the user have left.
            strikes_headline.place(x=10, y=20)

    def clear_screen(self):
        lst = self.root2.pack_slaves()
        for i in lst:
            i.destroy()
        lst1 = self.root2.place_slaves()
        for j in lst1:
            j.destroy()

    def draw_mode(self):
        time_thread = threading.Thread(target=self.timer)
        time_thread.daemon = True
        time_thread.start()
        headline = Label(self.root2, text=self.username)  # the name of the user on top of the screen.
        headline.pack()
        # print("helloooooooo")
        print("word = ", self.word)
        red_button = Button(self.root2, command=lambda: self.change_color('red'), bg='red')
        red_button.place(x=450, y=20)
        word_label = Label(self.root2, text="you need to draw: " + self.word)
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
        # self.root2.mainloop()
        return self.score

    def guess_mode(self):
        time_thread = threading.Thread(target=self.timer)
        time_thread.daemon = True
        time_thread.start()
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
        # self.root2.mainloop()

    def change_color(self, color):
        self.color = color

    def between_rounds_screen(self): pass
    #     self.root2.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
    #     self.root2.title("Drawing & Guessing Game- Between Rounds Window")  # caption of the window
    #     self.root2.resizable(width=FALSE, height=FALSE)
    #     tk_rgb = "#%02x%02x%02x" % (255, 255, 255)
    #     self.root2["background"] = tk_rgb
    #     another_round_button = Button(self.root2, relief="solid",
    #                                 bg="#%02x%02x%02x" % (255, 255, 255),
    #                                 command=lambda: self.__init__(self.server_socket, self.username, self.))
