
from tkinter import *
# by Canvas I can't save image, so i use PIL
import PIL
import threading
from PIL import Image, ImageDraw


class Screen:
    def __init__(self, socket):
        self.root = Tk()
        self.cv = Canvas(self.root, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
        self.x = 0
        self.y = 0
        self.server_socket = socket
        self.main()

    def main(self):
        # if left button on the mouse is being clicked, it goes to the function 'paint'.
        self.cv.bind('<B1-Motion>', self.send_coordinates)
        self.cv.pack(expand=YES, fill=BOTH)
        server_handler = threading.Thread(target=self.paint1)
        server_handler.start()
        self.root.mainloop()

    def send_coordinates(self, event):
        """

        :param event:
        :return:
        """
        self.x, self.y = event.x, event.y
        x_and_y = str(self.x) + " " + str(self.y)
        print(x_and_y)
        self.server_socket.send(x_and_y.encode())

    # def paint(self, event):
    #     """
    #
    #     :param event: contains the mouse x and y coordinates.
    #     :return: painting the screen in black in the requested coordinates.
    #     """
    #     self.x, self.y = event.x, event.y
    #     x2, y2 = (event.x + 1), (event.y + 1)
    #     self.cv.create_oval((self.x, self.y, x2, y2), fill='black', width=5)
    #     #  --- PIL
    #     # draw.line((self.x, self.y, x2, y2), fill='black', width=10)
    #     print("mouse position: (%s %s)" % (event.x, event.y))
    #     x_and_y = str(self.x) + " " + str(self.y)
    #     self.server_socket.send(x_and_y.encode())

    def paint1(self):
        """

        :return: painting the screen in black in the requested coordinates.
        """
        while True:
            x_and_y = self.server_socket.recv(1024).decode()
            pos = x_and_y.split(" ")  # separating x and y
            x = int(pos[0])
            y = int(pos[1])
            print(x, y)
            self.x, self.y = x, y
            x2, y2 = (x + 1), (y + 1)
            self.cv.create_oval((self.x, self.y, x2, y2), fill='black', width=5)
            print("other mouse position: (%s %s)" % (x, y))
            #  --- PIL
            # draw.line((self.x, self.y, x2, y2), fill='black', width=10)




























"""def save():
    filename = 'image.png'
    image1.save(filename)


def paint(event):
    x1, y1 = (event.x), (event.y)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=10)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=10)


root = Tk()

cv = Canvas(root, width=640, height=480, bg='white')
# --- PIL
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
# ----
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()"""