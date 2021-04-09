from tkinter import *
import threading
import socket
import time


class Screen:
    def __init__(self, sock, username):
        self.color = 'black'
        self.game_number = 1
        self.strikes = 3
        self.score = 0
        self.to_stop = False
        self.root2 = Tk()
        self.username = username
        self.cv = Canvas(self.root2, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
        self.root2.resizable(width=FALSE, height=FALSE)
        self.x = 0  # initializing coordinates.
        self.y = 0  # initializing coordinates.
        self.server_socket = sock
        self.word = ""
        self.every_round()
        self.root2.mainloop()

    def every_round(self):
        """
        in the start of every round.
        :return:
        """
        if self.game_number < 3:
            self.game_number += 1
            self.strikes = 3
            mode = self.server_socket.recv(1024).decode()
            print(mode)
            who_am_i, word_chosen = mode.split(";")   # who_am_i: either a 'draw' or 'guess'
            self.word = word_chosen
            if who_am_i == "draw":  # the drawer
                self.draw_mode()
            else:  # the guesser
                self.guess_mode()

    def draw_mode(self):
        """
        the screen of the drawer.
        :return:
        """
        timer_thread = threading.Thread(target=self.timer)  # starting a timer
        timer_thread.daemon = True
        timer_thread.start()
        headline = Label(self.root2, text=self.username)  # the name of the user on top of the screen.
        headline.pack()
        print("word = ", self.word)
        #  change color button.
        red_button = Button(self.root2, command=lambda: self.change_color('red'), bg='red')
        red_button.place(x=450, y=20)

        word_label = Label(self.root2, text="you need to draw: " + self.word)
        word_label.pack()

        score_headline = Label(self.root2, text='score: ' + str(self.score), font=('bubble', 15),  # the score
                               bg='white', fg="black", relief="solid")  # the title of the screen.
        score_headline.place(x=10, y=50)

        # if left button on the mouse is being clicked, it goes to the function 'send_coordinates '.
        self.cv.bind('<B1-Motion>', self.send_coordinates)
        self.cv.pack(expand=YES, fill=BOTH)
        server_handler = threading.Thread(target=self.paint, args=('draw',))
        server_handler.daemon = True
        # creating a thread that handles with the data the server sends to the client, w function 'paint'.
        server_handler.start()
        self.root2.mainloop()

    def guess_mode(self):
        timer_thread = threading.Thread(target=self.timer)  # starting a timer
        timer_thread.daemon = True
        timer_thread.start()

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
                               command=lambda: self.check_guess(guess, submit_button))
        submit_button.place(x=400, y=400)
        server_handler = threading.Thread(target=self.paint, args=('guess',))
        server_handler.daemon = True
        # creating a thread that handles with the data the server sends to the client, w function 'paint'.
        server_handler.start()
        self.root2.mainloop()

    def every_game(self):
        """
        in the start of every round.
        :return:
        """
        play_sign = self.server_socket.recv(4).decode()
        print(play_sign)
        print("root destroyed in the mall")
        self.clear_screen()
        self.strikes = 3
        mode = self.server_socket.recv(1024).decode()
        print(mode)
        who_am_i, word_chosen = mode.split(";")   # who_am_i: either a 'draw' or 'guess'
        self.word = word_chosen
        if who_am_i == "draw":
            self.draw_mode()
        else:
            self.guess_mode()

    def timer(self, seconds=80):
        if seconds <= 0 or self.to_stop:
            self.server_socket.send('end'.encode())
            self.every_game()
        else:
            timer_label = Label(self.root2, text=str(seconds), font=('bubble', 15), bg='white', width=5)
            timer_label.place(x=235, y=40)
            self.root2.after(1000, lambda: self.timer(seconds - 1))

    def send_coordinates(self, event):

        """
        the function sending the coordinates, of the mouse when clicked on the board to the server.
        :param event: when clicking the left button an event is created contains the coordinates of the place.
        :return:
        """
        self.x, self.y = event.x, event.y
        x_and_y = str(self.x) + ";" + str(self.y) + ";"
        print("send: ", x_and_y)
        self.server_socket.send(x_and_y.encode())  # sending the server the coordinates.

    def paint(self, mode):
        """
        receiving coordinates from server and painting the screen in black in them.
        :return:
        """
        print("paint is in process")
        finish = False
        while not finish:
            x_and_y = self.server_socket.recv(1024).decode()  # decrypting the data from the server.
            pos = x_and_y.split(";")  # separating x and y
            print("pos ", pos)
            if pos[0] == 'score':
                print("score was received")
                self.score += int(pos[1])
                score_headline = Label(self.root2, text='score: ' + str(self.score), font=('bubble', 15),  # the score
                                       bg='white', fg="black", relief="solid")
                score_headline.place(x=10, y=50)
            elif pos[0] == 'end':
                if mode == "draw":
                    self.cv.unbind('<B1-Motion>')
                finish = True
                self.to_stop = True
                self.every_round()
            else:
                try:
                    for i in range(0, len(pos)-2, 2):
                        x = int(pos[i])
                        y = int(pos[i + 1])
                        print("recv: ", x, y)
                        self.x, self.y = x, y
                        x2, y2 = (x + 1), (y + 1)
                        self.cv.create_oval((self.x, self.y, x2, y2), fill='black', width=5)
                except ConnectionResetError:
                    print("user disconnected")

                # print("VE", pos)
                # if pos[0] == 'end':
                #     if mode == 'draw':
                #         print("i am a drawer")
                #         # self.cv.unbind('<B1-Motion>')
                #     # finish = True
                # else:
        # painting the screen in the coordinates.
        # print("other mouse position: (%s %s)" % (x, y))

    def check_guess(self, guess, submit_button):
        """

        :param guess:
        :param submit_button:
        :return:
        """
        thread_cg = threading.Thread(target=self.check_guess1, args=(guess, submit_button))
        thread_cg.daemon = True
        thread_cg.start()

    def check_guess1(self, guess, submit_button):
        """
        checking the guess of the guesser.
        :param guess:
        :param submit_button:
        :return:
        """
        print("got to check guess")
        print("word", self.word)
        print("guess", guess.get())
        if guess.get() == self.word:
            self.server_socket.send(('True;' + self.username).encode())
            # self.cv.delete("all")
            # saying that the game has ended.
            you_guessed_correctly = Label(self.root2, text=' you guessed the word correctly!!', font=('bubble', 15),
                                     bg='white', fg="navy", relief="solid")
            you_guessed_correctly.place(x=150, y=200)
            you_guessed_correctly.after(1500, you_guessed_correctly.destroy)
            # self.clear_screen()
            round_finish_label = Label(self.root2, text="ROUND IS OVER", font=('bubble', 25))
            round_finish_label.place(x=100, y=100)
            guess.destroy()
            submit_button.destroy()
            # if self.server_socket.recv(1024).decode() == "end":  # if everyone guessed already
            #     pass
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

    def change_color(self, color):
        self.color = color

    # def between_rounds_screen(self):
    #     self.cv.delete("all")
    #     self.root2.geometry("500x500")  # size: 500x500, Location: (100, 30)
    #     self.root2.title("Drawing & Guessing Game- Between Rounds Window")  # caption of the window
    #     self.root2.resizable(width=FALSE, height=FALSE)
    #     tk_rgb = "#%02x%02x%02x" % (255, 255, 255)
    #     self.root2["background"] = tk_rgb
    #     another_round_button = Button(self.root2, relief="solid", bg="#%02x%02x%02x" % (255, 255, 255), command=self.main())
    #     another_round_button.place(x=200, y=200)










"""
def save():
    filename = 'image.png'
    image1.save(filename)
"""