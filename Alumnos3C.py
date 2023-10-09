from tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import PhotoImage 




ventana=tk.Tk()
ventana.title("Alumnos 3C")
ventana.geometry("1080x600")
ventana.config(bg="darkorchid")

ancho_boton=40
alto_boton=3
alto_label=100
img = PhotoImage(file="LCD.png")
def btnClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)

input_text=StringVar()
operador=""

Label(ventana, image=img).pack()
nombre=tk.StringVar()
apellido=tk.StringVar()
edad=tk.StringVar()
rut=tk.StringVar()
curso=tk.Entry()
foto=tk.Entry()
flechaisquierda=Button()
flechaderecha=Button()
texto1=tk.Label()
texto2=tk.Label()
texto3=tk.Label()
texto4=tk.Label()
texto5=tk.Label()


NOMBRE=tk.Entry(ventana,textvariable=nombre,width=ancho_boton).place(x=600,y=50)
APELLIDO=tk.Entry(ventana,textvariable=apellido,width=ancho_boton).place(x=600,y=150)   
EDAD=tk.Entry(ventana,textvariable=edad,width=ancho_boton).place(x=600,y=250)
RUT=tk.Entry(ventana,textvariable=rut,width=ancho_boton).place(x=600,y=350)
CURSO=tk.Entry(ventana,textvariable=curso,width=ancho_boton).place(x=600,y=450)
FOTO=tk.Entry(ventana,textvariable=foto).place(x=100,y=50,width=400,height=400)
FLECHA=Button(ventana,text="<",command=lambda:btnClick("<")).place(x=240,y=500,width=50,height=50)
FLECHO=Button(ventana,text=">",command=lambda:btnClick(">")).place(x=310,y=500,width=50,height=50)
TEXTO1=Label(ventana,text="Nombre").place(x=600,y=20)
TEXTO2=Label(ventana,text="Apellido").place(x=600,y=120)
TEXTO3=Label(ventana,text="Edad").place(x=600,y=220)
TEXTO4=Label(ventana,text="RUT").place(x=600,y=320)
TEXTO5=Label(ventana,text="Curso").place(x=600,y=420)

ventana.mainloop()