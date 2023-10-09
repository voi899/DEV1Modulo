from tkinter import *
from tkinter import PhotoImage 

root = Tk()
root.title("ob")
img = PhotoImage(file="jake.png")
Label(root, image=img).pack()
mainloop()