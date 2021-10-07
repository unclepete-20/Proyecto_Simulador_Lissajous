"""
@author: Pedro Pablo Arriola Jimenez (20188)
@author: Oscar Fernando López Barrios (20679)

@filename: simulador_lissajous.py

Fecha: 30/09/2021
Curso: Física 3 (Laboratorio)
Sección: 10
Catedrático: Luis Mijangos

Descrición del proyecto:

Este proyecto del laboratorio de Física 3 consiste en diseñar
y simular el comportamiento de un tubo de rayos catódicos que
posteriormente mostrarán unas formas llamadas "Lissajous" en
pantalla por medio de las modificaciones que realice el usuario
al momento de ejecutar el programa. En este proyecto se aplicarán
todos los conocimientos que hasta el momento se ha visto en el curso
como por ejemplo el potencial eléctrico, campo eléctrico, capacitancia,
entre otros.

"""
#Librerias importadas para poder utilizar funciones especiales que permitirán crear los Lissajous.
import tkinter
from logging import root
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from tqdm import tqdm, trange
import time
# import tkinter as tk
from tkinter import Tk, Frame, Button, Label, ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial


"""ventana = tk.Tk()
ventana.geometry('700x700')
ventana.wm_title('Simulacion del Comportamiento de un Tubo de Rayos Catodicos')
ventana.minsize(width=700,height=700)

frame = tk.Frame(ventana, bg='white', bd=3)
frame.pack(expand=1, fill='both')"""

def grafico(A, B, Delta, Vaceleracion, Vvertical, Vhorizontal): #Función que dibuja las Lissajous.

    #Variables que modifica el usuario.
    vy = Vvertical #Voltaje vertical (Se modifica)
    vx = Vhorizontal #Voltaje horizontal (Se modifica)
    va = Vaceleracion #Voltaje de aceleracion (Se modifica)
    
    #Variables que no se modifican
    carga = -1.6E-19
    masa = 9.1E-31
    distanciaplacas = 0.02
    ladoplaca = 0.1

    velocidad = math.sqrt(abs((2 * carga * va) / masa))
    tiempo = ladoplaca / velocidad

    acelaraciony = (carga * vy) / (masa * distanciaplacas)
    acelaracionx = (carga * vx) / (masa * distanciaplacas)

    distanciay = (acelaraciony / 2) * (tiempo ** 2)
    distanciax = (acelaracionx / 2) * (tiempo ** 2)

    angulo = math.degrees(math.atan(distanciay / ladoplaca))
    angulo2 = math.degrees(math.atan(distanciay / ladoplaca))


    fig, ax = plt.subplots()
    plt.title("Tubo de Rayos Catolicos", color='black', size=16,family="Arial")
    x = distanciax
    y = distanciay
    datos, = plt.plot([], [], 'ro')

    print(x, y)

    def init():
        ax.set_xlim(-0.25, 0.25)
        ax.set_ylim(-0.25, 0.25)
        return datos,

    def update(frame):
        datos.set_data(x, y)
        return datos,

    #ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)
    #plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')

    #Parte de Lissojous
    a = A
    b = B
    delta = Delta*(3.14)

    fig, ax = plt.subplots()
    datosx, datosy = [], []
    datos, = plt.plot([], [], 'ro')

    def init():
        ax.set_xlim(-0.25, 0.25)
        ax.set_ylim(-0.25, 0.25)
        return datos,

    def update(frame):
        datosx.append((distanciax)*(np.sin((a*frame) + delta)))
        datosy.append((distanciay)*(np.sin(b*frame)))
        datos.set_data(datosx, datosy)
        return datos,

    def iniciar(canvas):
        ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)
        canvas.draw()



    ventana = Tk()
    ventana.geometry('1920x1080')
    ventana.wm_title('Proyecto Fisica 3 / Pedro Arriola (20188) y Oscar López (20679)')
    ventana.minsize(width=1920, height=1080)

    def opennewwindow(ventana):
        # Toplevel object which will
        # be treated as a new window
        graficas = tkinter.Toplevel(ventana)

        # sets the title of the
        # Toplevel widget
        graficas.wm_title('Proyecto Fisica 3')

        # sets the geometry of toplevel
        graficas.geometry('1920x1080')
        graficas.minsize(width=1920, height=1080)

        frame = Frame(graficas, bg='white', bd=3)
        frame.pack(expand=1, fill='both')

        canvas = FigureCanvasTkAgg(fig, master = frame)
        canvas.get_tk_widget().pack(padx=5, pady=10, expand=1, fill='both', side=tkinter.RIGHT)

        iniciar(canvas)

    # Títulos

    static_title = tkinter.Label(master=ventana, text="⌁ PARÁMETROS MODIFICABLES ⌁", font=("Arial", 20), fg="#3892EA")
    static_title.place(relx=0.50, rely=0.12, relwidth=1.1, relheight=0.125, anchor=tkinter.CENTER)

    # Voltajes

    x_voltage = tkinter.Label(master=ventana, text="Vx", font=("Arial", 14), fg="black")
    x_voltage.place(relx=0.09375, rely=0.367, anchor=tkinter.CENTER)

    y_voltage = tkinter.Label(master=ventana, text="Vy", font=("Arial", 14), fg="black")
    y_voltage.place(relx=0.09375, rely=0.52, anchor=tkinter.CENTER)

    # Sliders

    x_slider = tkinter.Scale(master=ventana, from_=-8000, to=8000, orient=tkinter.HORIZONTAL)
    x_slider.place(relx=0.3, rely=0.4, relwidth=0.25, relheight=0.15, anchor=tkinter.CENTER)

    y_slider = tkinter.Scale(master=ventana, from_=-8000, to=8000, orient=tkinter.HORIZONTAL)
    y_slider.place(relx=0.3, rely=0.55, relwidth=0.25, relheight=0.15, anchor=tkinter.CENTER)

    # Parámetros

    a_label = tkinter.Label(master=ventana, text="A", font=("Arial", 20), fg="black")
    a_label.place(relx=0.6, rely=0.35, anchor=tkinter.CENTER)

    b_label = tkinter.Label(master=ventana, text="B", font=("Arial", 20), fg="black")
    b_label.place(relx=0.75, rely=0.35, anchor=tkinter.CENTER)

    c_label = tkinter.Label(master=ventana, text="Delta\n(δ)", font=("Arial", 20), fg="black")
    c_label.place(relx=0.9, rely=0.35, anchor=tkinter.CENTER)

    frequency_label = tkinter.Label(master=ventana, text="Frecuencia", font=("Arial", 14), fg="black")
    frequency_label.place(relx=0.09375, rely=0.675, anchor=tkinter.CENTER)

    interval_label = tkinter.Label(master=ventana, text="Intervalo", font=("Arial", 14), fg="black")
    interval_label.place(relx=0.09375, rely=0.780, anchor=tkinter.CENTER)

    # Function inputs

    a_input = tkinter.Entry(master=ventana)
    a_input.place(relx=0.6, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

    b_input = tkinter.Entry(master=ventana)
    b_input.place(relx=0.75, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

    frequency_input = tkinter.Entry(master=ventana)
    frequency_input.place(relx=0.225, rely=0.675, relwidth=0.1, anchor=tkinter.CENTER)

    interval_input = tkinter.Entry(master=ventana)
    interval_input.place(relx=0.225, rely=0.780, relwidth=0.1, anchor=tkinter.CENTER)

    # Botones

    delta_inputone = tkinter.Button(master=ventana, text='0')
    delta_inputone.place(relx=0.9, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

    delta_inputtwo = tkinter.Button(master=ventana, text='π/4')
    delta_inputtwo.place(relx=0.9, rely=0.60, relwidth=0.1, anchor=tkinter.CENTER)

    delta_inputthree = tkinter.Button(master=ventana, text='π/2')
    delta_inputthree.place(relx=0.9, rely=0.70, relwidth=0.1, anchor=tkinter.CENTER)

    delta_inputfour = tkinter.Button(master=ventana, text='3π/4')
    delta_inputfour.place(relx=0.9, rely=0.80, relwidth=0.1, anchor=tkinter.CENTER)

    delta_inputfive = tkinter.Button(master=ventana, text='π')
    delta_inputfive.place(relx=0.9, rely=0.9, relwidth=0.1, anchor=tkinter.CENTER)

    # define font
    myFont = font.Font(family='Helvetica', size=5, weight='bold')

    graficar = tkinter.Button(master=ventana, text='⌁ Graficar datos ⌁', bg='#3892EA', command=partial(opennewwindow, ventana))
    graficar.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.1, anchor=tkinter.CENTER)

    graficar['font'] = myFont

    ventana.mainloop()

    #plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')
    #plt.show()\

grafico(1, 3, (1/2), 100, 100, 100)