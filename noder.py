from tkinter import *

strikes = 3
score = 0
root = Tk()
username = 'ron'
cv = Canvas(root, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
root.resizable(width=FALSE, height=FALSE)

print("into guess mode")
headline = Label(cv, text=username)  # the name of the user on top of the screen.
headline.pack()
print("into guess mode 1")
score_headline = Label(cv, text='score: ' + str(score), font=('bubble', 15),  # the score
                       bg='white', fg="black", relief="solid")
score_headline.place(x=10, y=50)
print("into guess mode 2")
strikes_headline = Label(cv, text='strikes: ' + str(strikes), font=('bubble', 15),
                         bg='white', fg="black", relief="solid")  # the strikes the user have left.
strikes_headline.place(x=10, y=20)
print("into guess mode 3")
guess = Entry(cv, relief='solid', font=('bubble', 10), bg='white', fg="black")
guess.delete(0, END)
guess.insert(0, 'enter a guess')
guess.place(x=100, y=400)
print("into guess mode 4")
submit_button = Button(cv, text="submit", relief="solid",
                       font=('cooper black', 10), fg="black", bg="#%02x%02x%02x" % (255, 255, 255),
                       command=lambda: check_guess(guess))
submit_button.place(x=400, y=400)
root.mainloop()


def check_guess(guess):
    pass
    # msg = "guess;" + guess.get() + ";" + username
    # server_socket.send(msg.encode())
    # response = server_socket.recv(1024).split(";")  # containing whether the guess is true or not and the score
    # if response[0] == "True":  # if the guess is empty returning false.
    #     score += response[1]
    # else:
    #     strikes -= 1
    #     if trikes != 0:
    #         guess_mode()