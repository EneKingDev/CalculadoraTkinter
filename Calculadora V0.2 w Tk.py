import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

import sv_ttk

ventana = tk.Tk()
ventana.title("Calculadora V0.2")
ventana.geometry("280x280")
ventana.iconbitmap("icon.ico")

cantidad_filas = 4
cantidad_columnas = 3
for i in range (cantidad_filas):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(cantidad_columnas):
    ventana.grid_columnconfigure(i, weight=1) 

caja_ingreso_numeros = ttk.Entry(justify=tk.RIGHT, font=("Calibri", 20))
caja_ingreso_numeros.grid(column=0,row=0,columnspan=3, sticky="nsew")

def clickBoton(number):
    caja_ingreso_numeros.insert(tk.END,number)

def clickClear():
    caja_ingreso_numeros.delete(0,tk.END)

def clickIgual():
    try:
        y=str(eval(caja_ingreso_numeros.get()))
        caja_ingreso_numeros.delete(0,tk.END)
        caja_ingreso_numeros.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

btn_numero_1 = ttk.Button(text = "7", command=lambda:clickBoton(7))
btn_numero_1.grid(column=0, row=1,sticky="nsew")

btn_numero_8 = ttk.Button(text = "8", command=lambda:clickBoton(8))
btn_numero_8.grid(column=1, row=1,sticky="nsew")

btn_numero_9 = ttk.Button(text = "9", command=lambda:clickBoton(9))
btn_numero_9.grid(column=2, row=1,sticky="nsew")

btn_numero_4 = ttk.Button(text = "4", command=lambda:clickBoton(4))
btn_numero_4.grid(column=0, row=2,sticky="nsew")

btn_numero_5 = ttk.Button(text = "5", command=lambda:clickBoton(5))
btn_numero_5.grid(column=1, row=2,sticky="nsew")

btn_numero_6 = ttk.Button(text = "6", command=lambda:clickBoton(6))
btn_numero_6.grid(column=2, row=2,sticky="nsew")

btn_numero_1 = ttk.Button(text = "1", command=lambda:clickBoton(1))
btn_numero_1.grid(column=0, row=3,sticky="nsew")

btn_numero_2 = ttk.Button(text = "2", command=lambda:clickBoton(2))
btn_numero_2.grid(column=1, row=3,sticky="nsew")

btn_numero_3 = ttk.Button(text = "3", command=lambda:clickBoton(3))
btn_numero_3.grid(column=2, row=3,sticky="nsew")

btn_numero_clear = ttk.Button(text = "Clr", command=clickClear)
btn_numero_clear.grid(column=0, row=4, sticky="nsew")

btn_numero_0 = ttk.Button(text="0", command=lambda:clickBoton(0))
btn_numero_0.grid(column=1, row=4,sticky="nsew")

btn_numero_punto = ttk.Button(text=".", command=lambda:clickBoton('.'))
btn_numero_punto.grid(column=2, row=4,sticky="nsew")

btn_numero_igual = ttk.Button(text="=", command=clickIgual)
btn_numero_igual.grid(column=3, row=4,sticky="nsew")

btn_numero_suma = ttk.Button(text="+", command=lambda:clickBoton("+"))
btn_numero_suma.grid(column=3, row=3,sticky="nsew")

btn_numero_resta = ttk.Button(text="-", command=lambda:clickBoton("-"))
btn_numero_resta.grid(column=3, row=2,sticky="nsew")

btn_numero_multiplicacion = ttk.Button(text="*", command=lambda:clickBoton("*"))
btn_numero_multiplicacion.grid(column=3, row=1,sticky="nsew")

btn_numero_division = ttk.Button(text="/", command=lambda:clickBoton("/"))
btn_numero_division.grid(column=3, row=0,sticky="nsew")


sv_ttk.set_theme("light")

ventana.mainloop()

