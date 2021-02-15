import tkinter as tk

root = tk.Tk()
root.geometry("943x600+100+30")  # size: 943x600, Location: (100, 30)
root.title("Drawing & Guessing Game- Waiting Window")  # caption of the window
root.resizable(width=tk.FALSE, height=tk.FALSE)
img = tk.PhotoImage(file='draw-and-guess.png')
background = tk.Label(root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                      fg="black")  # creating home screen
background.place(x=0, y=0)

lst = root.pack_slaves()
for i in lst:
    i.destroy()
lst1 = root.place_slaves()
for j in lst1:
    j.destroy()


img = tk.PhotoImage(file='draw-and-guess.png')
background = tk.Label(root, image=img, bg="#%02x%02x%02x" % (255, 255, 255),
                      fg="black")  # creating home screen
background.place(x=0, y=0)

lbl = tk.Label(root, text="waiting for more participants! ", font=("bubble", 20), bg='orange')
lbl.pack(padx=50, pady=100)

root.mainloop()