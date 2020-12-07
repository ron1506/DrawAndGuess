import tkinter as tk


class Surf:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
        self.root.title("Drawing & Guessing Gme- Main Window")  # caption of the window
        self.root.resizable(width=tk.FALSE, height=tk.FALSE)
        tk_rgb = "#%02x%02x%02x" % (128, 192, 200)
        self.root["background"] = tk_rgb
        img = tk.PhotoImage(file='draw-and-guess.png')
        lb = tk.Label(self.root, text="Hello, welcome to the Draw and Guess game !", image=img,
                      bg="#%02x%02x%02x" % (128, 192, 200), fg="black", font=('times new roman', 20))
        lb1 = tk.Label(self.root, text="The sunken", relief="sunken")
        lb2 = tk.Label(self.root, text="The flat", relief="flat")
        lb3 = tk.Label(self.root, text="The raised", relief="raised")
        lb4 = tk.Label(self.root, text="The groove", relief="groove")
        lb5 = tk.Label(self.root, text="The ridge", relief="ridge")
        lb6 = tk.Label(self.root, text="The solid", relief="solid")
        lb1.pack(side='left')
        lb2.pack(side='left')
        lb3.pack(side='left')
        lb4.pack(side='left')
        lb5.pack(side='left')
        lb6.pack(side='left')

        lb.pack()
        tk.mainloop()  # last line


def main():
    s1 = Surf()


if __name__ == '__main__':
    main()