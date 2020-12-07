
from tkinter import *
# by Canvas I can't save image, so i use PIL
import PIL
from PIL import Image, ImageDraw



def paint(event):
    """

    :param event: contains the mouse x and y coordinates.
    :return: painting the screen in black in the requested coordinates.
    """
    x1, y1 = event.x, event.y
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval((x1, y1, x2, y2), fill='black', width=5)
    #  --- PIL
    draw.line((x1, y1, x2, y2), fill='black', width=10)


root = Tk()
cv = Canvas(root, width=500, height=500, bg='white')  # creating a blank white canvas, size: 500x500.
# --- PIL
cv.bind('<Button-1>', paint)  # if left button on the mouse is being clicked, it goes to the function 'paint'.
image1 = PIL.Image.new('RGB', (640, 480), 'white')
draw = ImageDraw.Draw(image1)
# ----
cv.bind('<B1-Motion>', paint)
cv.pack(expand=YES, fill=BOTH)

root.mainloop()

























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