"""
Name: Ron Aizen
Date: November 6 2020
PyGame Multiplayer Drawing and guessing game Project 1.0
"""
import tkinter as tk


# hello its jasmin taking over ur computer maybe u will notice maybe not ar shall i say perhaps? good luck with
# # your psychometry


class Surface:
    def __init__(self):
        self.root = tk.Tk()

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
        home_screen.place(x=0, y=0)

        registration_text = tk.Label(self.root, text="First Game?",
                font=('cooper black', 15), fg="black")  # registration text
        registration_text.place(x=210, y=435)

        registration_button = tk.Label(self.root, text="Press here to register", relief="solid",
                font=('cooper black', 22), fg="white", bg="#%02x%02x%02x" % (60, 53, 53))  # registration button
        registration_button.place(x=115, y=485)

        log_in_text = tk.Label(self.root, text="Already Logged In?",
                font=('cooper black', 15), fg="black", bg=None)  # log in text
        log_in_text.place(x=610, y=435)

        log_in_button = tk.Label(self.root, text="Press here to Log In", relief="solid",
                font=('cooper black', 22), fg="white", bg="#%02x%02x%02x" % (60, 53, 53))  # log in button
        log_in_button.place(x=565, y=485)

        info_img = tk.PhotoImage(file='question-mark.png')
        info_button = tk.Label(self.root, image=info_img, bg="#%02x%02x%02x" % (255, 255, 255),  # creating info button
                               fg="black")
        info_button.place(x=850, y=50)

        tk.mainloop()  # last line

    def quit_screen(self):
        """

        :return:
        """
        pass

    def home_button(self):
        pass

    def return_button(self):
        pass

    def info_button(self):
        pass

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
        self.root.geometry("751x650+100+30")  # size: 751x650, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Info Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (255, 148, 7)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        """info_bg = tk.PhotoImage(file='how-it-works-1.png')
        info_sc = tk.Label(self.root, image=info_bg)  # creating home screen
        info_sc.place(x=0, y=0)"""

        info_headline = tk.Label(text='HOW TO PLAY?!', font=('bubble', 20), bg='orange', fg="black", relief="solid")
        info_headline.place(x=270, y=5)

        info_text = tk.Label(text=instructions, font=('times new roman', 18), bg="orange",
                             fg="black")  # creating instructions
        info_text.place(x=0, y=50)

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Label(self.root, image=home_button_img, relief="solid",
                                  bg="#%02x%02x%02x" % (255, 255, 255))  # creating home screen
        home_sc_button.place(x=20, y=20)

        dice_img = tk.PhotoImage(file='dice-icon.png')  # adding decorations, dice photo
        dice_button = tk.Label(self.root, image=dice_img, relief="solid",
                               bg="#%02x%02x%02x" % (255, 255, 255))  # creating dice image
        dice_button.place(x=650, y=560)

        tk.mainloop()  # last line.

    def login_button(self):
        pass

    def login_screen(self):
        """
        creating the screen that will open after pressing the log in button, with option to log in to the game.
        :return:
        """
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Log In Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)

        tk_rgb = "#%02x%02x%02x" % (255, 148, 7)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        img = tk.PhotoImage(file='draw-and-guess.png')
        login_screen = tk.Label(self.root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                                fg="black")  # creating home screen
        login_screen.place(x=0, y=0)

        login_headline = tk.Label(text='Please Enter The Name Of An Existing Player', font=('bubble', 23), bg='orange',
                                 fg="black", relief="solid")  # the title of the screen.
        login_headline.place(x=190, y=120)  # positioning the title of the screen.

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Label(self.root, image=home_button_img, relief="solid",
                                  bg="#%02x%02x%02x" % (255, 255, 255))  # creating home screen
        home_sc_button.place(x=20, y=20)

        username_button = tk.Label(relief='raise', text='Username: ', font=('bubble', 28), bg='orange', fg="black")
        username_button.place(x=150, y=380)

        username_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        username_blank_space.place(x=400, y=380)

        password_button = tk.Label(relief='raise', text='Password: ', font=('bubble', 28), bg='orange', fg="black")
        password_button.place(x=150, y=480)

        password_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        password_blank_space.place(x=400, y=480)

        tk.mainloop()  # last line.

    def register_button(self):
        pass

    def register_screen(self):
        """
        creating the screen that will open after pressing the log in button, with option to log in to the game.
        :return:
        """
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Game- Registration Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (255, 148, 7)  # picking background color.
        self.root["background"] = tk_rgb  # applying the background color on the screen

        img = tk.PhotoImage(file='draw-and-guess.png')
        register_screen = tk.Label(self.root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                                fg="black")  # creating home screen
        register_screen.place(x=0, y=0)

        registration_headline = tk.Label(text='Please Enter The Details Of The New Player', font=('bubble', 20),
                                         bg='orange', fg="black", relief="solid")  # the title of the screen.
        registration_headline.place(x=200, y=30)  # positioning the title of the screen.

        home_button_img = tk.PhotoImage(file='home-icon.png')
        home_sc_button = tk.Label(self.root, image=home_button_img, relief="solid",
                                  bg="#%02x%02x%02x" % (255, 255, 255))  # creating home screen
        home_sc_button.place(x=20, y=20)

        email_button = tk.Label(relief='raise', text="Email: ", font=('bubble', 28), bg='orange', fg="black")
        email_button.place(x=270, y=150)

        email_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        email_blank_space.place(x=400, y=150)

        username_button = tk.Label(relief='raise', text="User's Name: ", font=('bubble', 28), bg='orange', fg="black")
        username_button.place(x=150, y=250)

        username_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        username_blank_space.place(x=400, y=250)

        password_button = tk.Label(relief='raise', text='Password: ', font=('bubble', 28), bg='orange', fg="black")
        password_button.place(x=200, y=350)

        password_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        password_blank_space.place(x=400, y=350)

        password_button = tk.Label(relief='raise', text='Confirm Password: ', font=('bubble', 28), bg='orange', fg="black")
        password_button.place(x=60, y=450)

        password_blank_space = tk.Label(relief='solid', text="                       ", font=('bubble', 28)
                                        , bg='orange', fg="black")
        password_blank_space.place(x=400, y=450)

        tk.mainloop()  # last line.

    def draw_on_board(self):
        pass

    def enter_game_button(self):
        pass

    def write_text(self, text, pos):
        pass

    def check_where_pressed(self):
        pass


def main():
    s = Surface()
    s.open_screen()
    s.draw_on_board()
    s.info_screen()
    s.login_screen()
    s.register_screen()


if __name__ == '__main__':
    main()


