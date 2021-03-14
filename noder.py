"""
Name: Ron Aizen
Date: November 6 2020
PyGame Multiplayer Drawing and guessing game Project 1.0
"""
import socket
import tkinter as tk
import threading
from tkinter import messagebox
from pickle import loads
from screendraft import Screen


class Surface:
    def __init__(self, ip, port):
        """
        constructor. initializing variables of the class.
        building the socket, connecting to server, the main function.
        :param ip:
        :param port:
        """
        self.ip = ip
        self.port = port
        self.root = tk.Tk()
        self.username = ""
        self.password = ""
        self.confirm_password = ""
        self.email_address = ""
        try:
            # Create a TCP/IP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating the socket
            self.sock.connect((self.ip, self.port))  # connecting to server
            print('connected to server')  # to see if client connected successfully.
            self.open_screen()
            self.root.mainloop()
        except socket.error as e:
            print(e)

    def open_screen(self):
        """
        creating the main window, the first window that the user sees.
        :return:
        """
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Main Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (255, 255, 255)
        self.root["background"] = tk_rgb

        img = tk.PhotoImage(file='draw-and-guess.png')
        home_screen = tk.Label(self.root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                               fg="black")  # creating home screen
        home_screen.photo = img
        home_screen.place(x=0, y=0)

        registration_text = tk.Label(self.root, text="First Game?",
                                     font=('cooper black', 15), fg="black")  # registration text
        registration_text.place(x=210, y=435)

        registration_button = tk.Button(self.root, text="Press here to register", relief="solid",
                                        font=('cooper black', 22), fg="white", bg="#%02x%02x%02x" % (60, 53, 53),
                                        command=self.register_screen)  # registration button
        registration_button.place(x=115, y=485)

        log_in_text = tk.Label(self.root, text="Already Logged In?",
                               font=('cooper black', 15), fg="black", bg=None)  # log in text
        log_in_text.place(x=610, y=435)

        log_in_button = tk.Button(self.root, text="Press here to Log In", relief="solid",
                                  font=('cooper black', 22), fg="white", bg="#%02x%02x%02x" % (60, 53, 53),
                                  command=self.login_screen)  # log in button
        log_in_button.place(x=565, y=485)

        info_img = tk.PhotoImage(file='question-mark.png')
        info_button = tk.Button(self.root, image=info_img, bg="#%02x%02x%02x" % (255, 165, 0),  # creating info button
                                fg="black", command=self.info_screen)
        info_button.photo = info_img
        info_button.place(x=850, y=50)

        # tk.mainloop()  # last line

    def info_screen(self):
        """
        creating the screen that will open after pressing the info button, with directions how to play.
        :return: nothing.
        """
        instructions = """The game is a multiplayer game in which \n 
                    each user registers by creating a new player \n
                    or by connecting to an existing player (what makes \n 
                    him part of the users database). \n
                    Each game one player is selected among the others \n
                    and presented randomly a word from a prepared \n
                    database with words from different types of groups \n
                    such as, items, animals, objects, professions, and more... \n
                    He must express the word by drawing it on\n
                    the board while the other participants must guess \n
                    the word by writing it in the chat."""
        self.root.geometry("650x650+100+30")  # size: 751x650, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Info Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (255, 165, 0)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        """info_bg = tk.PhotoImage(file='how-it-works-1.png')
        info_sc = tk.Label(self.root, image=info_bg)  # creating home screen
        info_sc.place(x=100, y=30)"""

        info_headline = tk.Label(text='HOW TO PLAY?!', font=('bubble', 20), bg='orange', fg="black", relief="solid")
        info_headline.place(x=270, y=5)

        info_text = tk.Label(text=instructions, font=('times new roman', 18), bg="orange",
                             fg="black")  # creating instructions
        info_text.place(x=0, y=50)

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Button(self.root, image=home_button_img, relief="solid",
                                   bg='orange', command=self.open_screen)  # creating home screen
        home_sc_button.photo = home_button_img
        home_sc_button.place(x=20, y=20)

        dice_img = tk.PhotoImage(file='dice-icon.png')  # adding decorations, dice photo
        dice_button = tk.Label(self.root, image=dice_img, relief="solid",
                               bg="#%02x%02x%02x" % (255, 165, 0))  # creating dice image
        dice_button.photo = dice_img
        dice_button.place(x=50, y=560)

        # tk.mainloop()  # last line.

    def login_screen(self):
        """
        creating the screen that will open after pressing the log in button, with option to log in to the game.
        :return:
        """
        #self.clear_screen()
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Log In Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)

        tk_rgb = "#%02x%02x%02x" % (255, 148, 7)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        img = tk.PhotoImage(file='draw-and-guess.png')
        login_screen = tk.Label(self.root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                                fg="black")  # creating home screen
        login_screen.photo = img
        login_screen.place(x=0, y=0)

        login_headline = tk.Label(text='Please Enter The Name Of An Existing Player', font=('bubble', 23), bg='orange',
                                  fg="black", relief="solid")  # the title of the screen.
        login_headline.place(x=190, y=120)  # positioning the title of the screen.

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Button(self.root, image=home_button_img, relief="solid",
                                   bg="#%02x%02x%02x" % (255, 165, 0), command=self.open_screen)  # creating home screen
        home_sc_button.photo = home_button_img
        home_sc_button.place(x=20, y=20)

        username_label = tk.Label(relief='raise', text='Username: ', font=('bubble', 28), bg='orange', fg="black")
        username_label.place(x=150, y=380)

        username = tk.Entry(relief='solid', font=('bubble', 20), bg='orange', fg="black")
        username.place(x=400, y=380)

        password_label = tk.Label(relief='raise', text='Password: ', font=('bubble', 28), bg='orange', fg="black")
        password_label.place(x=150, y=480)

        password = tk.Entry(relief='solid', font=('bubble', 20), bg='orange', fg="black", show='*')
        password.place(x=400, y=480)

        arrow_img = tk.PhotoImage(file='arrow.png')
        continue_button = tk.Button(self.root, image=arrow_img, relief="solid",
                                    bg="#%02x%02x%02x" % (255, 255, 255),
                                    command=lambda: self.submit_log_in(username, password))  # creating arrow button
        continue_button.photo = arrow_img
        continue_button.place(x=800, y=500)
        # tk.mainloop()  # last line.

    def submit_log_in(self, username, password):
        """
        :param username:
        :param password:
        :return:
        """
        self.username = username.get()
        self.password = password.get()
        msg = "login;" + self.username + ";" + self.password + ";" + str(self.sock)
        self.sock.send(msg.encode())
        is_ok = self.sock.recv(1024).decode()
        print("thats what i get: ", is_ok)
        if is_ok == "False":  # 'true' if managed to log in and 'false' otherwise.
            messagebox.showinfo(title="Log in failed.",
                                message="username or password are wrong, or user already connected.")
            self.login_screen()
        else:
            messagebox.showinfo(title="Log in went successfully.", message="welcome to 'draw and guess'.")
            self.waiting_screen()

    def register_screen(self):
        """
        creating the screen that will open after pressing the log in button, with option to log in to the game.
        :return:
        """
        #self.clear_screen()
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Registration Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (255, 148, 7)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        img = tk.PhotoImage(file='draw-and-guess.png')
        register_screen = tk.Label(self.root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                                   fg="black")  # creating home screen
        register_screen.photo = img
        register_screen.place(x=0, y=0)

        registration_headline = tk.Label(text='Please Enter The Details Of The New Player', font=('bubble', 20),
                                         bg='orange', fg="black", relief="solid")  # the title of the screen.
        registration_headline.place(x=200, y=30)  # positioning the title of the screen.

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Button(self.root, image=home_button_img, relief="solid",
                                   bg="#%02x%02x%02x" % (255, 255, 255),
                                   command=self.open_screen)  # creating home screen button
        home_sc_button.photo = home_button_img
        home_sc_button.place(x=20, y=20)

        email_button = tk.Label(relief='raise', text="Email: ", font=('bubble', 28), bg='orange', fg="black")
        email_button.place(x=270, y=150)

        email_adress = tk.Entry(relief='solid', font=('bubble', 20), bg='orange', fg="black")
        email_adress.place(x=400, y=150)

        username_button = tk.Label(relief='raise', text="User's Name: ", font=('bubble', 28), bg='orange', fg="black")
        username_button.place(x=150, y=250)

        username = tk.Entry(relief='solid', font=('bubble', 20)
                            , bg='orange', fg="black")
        username.place(x=400, y=250)

        password_button = tk.Label(relief='raise', text='Password: ', font=('bubble', 28), bg='orange', fg="black")
        password_button.place(x=200, y=350)

        password = tk.Entry(relief='solid', font=('bubble', 20), bg='orange', fg="black", show='*')
        password.place(x=400, y=350)

        confirm_password_button = tk.Label(relief='raise', text='Confirm Password: ', font=('bubble', 28), bg='orange',
                                           fg="black")
        confirm_password_button.place(x=60, y=450)

        confirm_password = tk.Entry(relief='solid', font=('bubble', 20), bg='orange', fg="black", show='*')
        confirm_password.place(x=400, y=450)

        arrow_img = tk.PhotoImage(file='arrow.png')
        # creating arrow button
        continue_button = tk.Button(self.root, image=arrow_img, relief="solid",
                                    bg="#%02x%02x%02x" % (255, 255, 255),
                                    command=lambda: self.submit_register(username, password, confirm_password,
                                                                         email_adress))
        continue_button.photo = arrow_img
        continue_button.place(x=800, y=500)
        # tk.mainloop()  # last line.

    def submit_register(self, username, password, confirm_password, email_address):
        """
        :param username:
        :param password:
        :param confirm_password:
        :param email_address:
        :return:
        """
        self.username = username.get()
        self.password = password.get()
        self.confirm_password = confirm_password.get()
        self.email_address = email_address.get()
        if self.password != self.confirm_password:
            messagebox.showinfo(title=" password not identical.",
                                message="the password confirm should be exactly like the password")
            self.register_screen()
        if ('@' not in self.email_address) or ('.com' not in self.email_address):
            messagebox.showinfo(title="Invalid Email address", message="Must contain '@' and '.com'")
            self.register_screen()
        msg = "register;" + self.username + ";" + self.password + ";" + self.email_address
        print(msg)
        self.sock.send(msg.encode())
        if_ok = self.sock.recv(1024).decode()  # 'true' if managed to register and 'false' otherwise.
        if if_ok == 'True':  # managed to register.
            messagebox.showinfo(title="Registration went successfully.", message="welcome to 'draw and guess'.")
            self.clear_screen()
            self.waiting_screen()
        else:  #
            messagebox.showinfo(title="Registration failed.", message="try again.")
            self.register_screen()

    def waiting_screen(self):
        #  self.clear_screen()
        self.root.title("Drawing & Guessing Game- Waiting Window")  # caption of the window
        img = tk.PhotoImage(file='draw-and-guess.png')
        background = tk.Label(self.root, image=img)  # creating home screen
        background.photo = img
        background.place(x=0, y=0)

        lbl = tk.Label(self.root, text="waiting for more participants! ", font=("bubble", 20), bg='orange')
        lbl.pack(padx=100, pady=200)
        thread_wait_for_instructions = threading.Thread(target=self.play_screen)
        # thread_wait_for_instructions.daemon = True
        thread_wait_for_instructions.start()
        # self.root.mainloop()

    def play_screen(self):
        # print("im in play screen")
        play_sign = self.sock.recv(4).decode()
        print(play_sign)
        self.root.after(0, self.root.destroy)
        print("root destroyed in the mall")
        score = 0
        for i in range(2):
            mode = self.sock.recv(1024).decode()
            print(mode)
            who_am_i, word_chosen = mode.split(";")   # who_am_i: either a 'draw' or 'guess'
            s = Screen(self.sock, self.username, who_am_i, word_chosen, score)

    def clear_screen(self):
        lst = self.root.pack_slaves()
        for i in lst:
            i.destroy()
        lst1 = self.root.place_slaves()
        for j in lst1:
            j.destroy()


def main():
    ip = '127.0.0.1'
    port = 1730
    s = Surface(ip, port)


if __name__ == '__main__':
    main()