"""
Name: Ron Aizen
Date: December 4 2020
GUI Practice- tkinter
"""
import tkinter as tk

root = tk.Tk()
root.geometry("300x130+100+30")  # size: 943x600, Location: (100, 30)
root.title("Ron Aizen")
root.resizable(width=tk.FALSE, height=tk.FALSE)
tk_rgb = "#%02x%02x%02x" % (255, 255, 255)
root["background"] = tk_rgb

# first task
"""lb1 = tk.Label(root, text="", width=10, height=4, bg="yellow")
lb2 = tk.Label(root, text="", width=10, height=4, bg="blue")
lb3 = tk.Label(root, text="", width=10, height=4, bg="green")
lb4 = tk.Label(root, text="", width=10, height=4, bg="red")
lb1.pack(side=tk.LEFT)
lb2.pack(side=tk.RIGHT)
lb3.pack(side=tk.TOP)
lb4.pack(side=tk.BOTTOM)"""

# second task
lb1 = tk.Label(root, text="", width=10, height=4, bg="yellow")
lb2 = tk.Label(root, text="", width=10, height=4, bg="blue")
lb3 = tk.Label(root, text="", width=10, height=4, bg="green")
lb4 = tk.Label(root, text="", width=10, height=4, bg="red")
lb1.place(x=0, y=0)
lb2.place(x=0, y=65)
lb3.place(x=75, y=0)
lb4.place(x=75, y=65)
tk.mainloop()



