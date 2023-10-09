from tkinter import *

wind = Tk()
wind.geometry("400x300")
wind.config(bg="yellow")

my_image = PhotoImage(file="C:\Users\cristopher\Desktop\intro_web\tareas\jake.png")
lbl=Label(image=my_image).pack()

wind.mainloop()