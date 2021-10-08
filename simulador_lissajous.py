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

global delta

def lissajous_delta(value):

    if(value == 1):
        delta = 0*(math.pi)
    elif(value == 2):
        delta = (1/4)*(math.pi)
    elif(value == 3):
        delta = (1/2)*(math.pi)
    elif(value == 4):
        delta = (3/4)*(math.pi)
    elif(value == 5):
        delta = math.pi

    print("delta: ", delta)

def calculos(Vaceleracion, Vhorizontal, Vvertical):
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

    acelaraciony = abs(carga * vy) / (masa * distanciaplacas)
    acelaracionx = abs(carga * vx) / (masa * distanciaplacas)

    distanciay = (acelaraciony / 2) * (tiempo ** 2)
    distanciax = (acelaracionx / 2) * (tiempo ** 2)

    angulox = math.degrees(math.atan(distanciax / ladoplaca))
    anguloy = math.degrees(math.atan(distanciay / ladoplaca))

    return distanciax, distanciay, angulox, anguloy


def grafico(distanciax, distanciay, angulox, anguloy, A, B, frecuencia, intervalo): #Función que dibuja las Lissajous.
    
    plt.close()
    plt.clf()

    plt.title("Tubo de Rayos Catodicos", color='black', size=16,family="Arial")
    x = distanciax
    y = distanciay

    plt.subplot(2, 2, 1)
    plt.plot(x, y, 'o')
    

    vistah, vistav = angulo(angulox, anguloy, distanciax, distanciay)

    plt.subplot(2, 2, 2)
    plt.plot(vistah)

    plt.subplot(2, 2, 3)
    plt.plot(vistav)

    pi = (np.pi/2)
    t = np.arange(0, 20, 0.1)
    x = ((distanciax)*(np.sin((A * t) + (np.pi)/2)))
    y = ((distanciay)*(np.sin(B * t)))
    plt.subplot(2, 2, 4)
    plt.plot(x, y)

    fig, ax = plt.subplots()
    datosx, datosy = [], []
    datos, = plt.plot([], [], 'ro')

    def init():
        ax.set_xlim(-0.5, 0.5)
        ax.set_ylim(-0.5, 0.5)
        return datos,

    def update(frame):
        datosx.append((distanciax)*(np.sin((A * frame) + (np.pi)/2)))
        datosy.append((distanciay)*(np.sin(B * frame)))
        datos.set_data(datosx, datosy)
        return datos,

    ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)

    plt.show()


def angulo(anguloh, angulov, distanciax, distanciay):

    anguloh = abs(anguloh)
    angulox = np.linspace(0, anguloh, 300)
    desplamientoh = np.linspace(0, distanciax, 300)
    desplazamientox = desplamientoh*angulox

    angulov = abs(angulov)
    anguloy = np.linspace(0, angulov, 300)
    desplamientov = np.linspace(0, distanciay, 300)
    desplazamientoy = desplamientov*anguloy

    return desplazamientox, desplazamientoy


def opennewwindow(ventana, Va, Vx, Vy, A, B, Frecuencia, Intervalo):
    
    dx, dy, ax, ay = calculos(Va, Vx, Vy)

    grafico(dx, dy, ax, ay, A, B, Frecuencia, Intervalo)
    


ventana = Tk()
ventana.geometry('1080x720')
ventana.wm_title('Proyecto Fisica 3 / Pedro Arriola (20188) y Oscar López (20679)')
ventana.minsize(width=1080, height=720)

# Títulos

static_title = tkinter.Label(master=ventana, text="⌁ PARÁMETROS MODIFICABLES ⌁", font=("Arial", 20), fg="#3892EA")
static_title.place(relx=0.50, rely=0.12, relwidth=1.1, relheight=0.125, anchor=tkinter.CENTER)

# Voltajes

x_voltage = tkinter.Label(master=ventana, text="Vx", font=("Arial", 14), fg="black")
x_voltage.place(relx=0.09375, rely=0.367, anchor=tkinter.CENTER)

y_voltage = tkinter.Label(master=ventana, text="Vy", font=("Arial", 14), fg="black")
y_voltage.place(relx=0.09375, rely=0.46, anchor=tkinter.CENTER)

a_voltage = tkinter.Label(master=ventana, text="Va", font=("Arial", 14), fg="black")
a_voltage.place(relx=0.09375, rely=0.55, anchor=tkinter.CENTER)

# Sliders

x_slider = tkinter.Scale(master=ventana, from_=-1000, to=1000, orient=tkinter.HORIZONTAL)
x_slider.place(relx=0.3, rely=0.4, relwidth=0.25, relheight=0.15, anchor=tkinter.CENTER)

y_slider = tkinter.Scale(master=ventana, from_=-1000, to=1000, orient=tkinter.HORIZONTAL)
y_slider.place(relx=0.3, rely=0.5, relwidth=0.25, relheight=0.15, anchor=tkinter.CENTER)

a_slider = tkinter.Scale(master=ventana, from_=-1000, to=1000, orient=tkinter.HORIZONTAL)
a_slider.place(relx=0.3, rely=0.6, relwidth=0.25, relheight=0.15, anchor=tkinter.CENTER)

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

a_input = tkinter.Entry(master=ventana, justify='center')
a_input.place(relx=0.6, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

b_input = tkinter.Entry(master=ventana, justify='center')
b_input.place(relx=0.75, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

frequency_input = tkinter.Entry(master=ventana, justify='center')
frequency_input.place(relx=0.225, rely=0.675, relwidth=0.1, anchor=tkinter.CENTER)

interval_input = tkinter.Entry(master=ventana, justify='center')
interval_input.place(relx=0.225, rely=0.780, relwidth=0.1, anchor=tkinter.CENTER)

# Botones

delta_inputone = tkinter.Button(master=ventana, text='0', command=lissajous_delta(1))
delta_inputone.place(relx=0.9, rely=0.5, relwidth=0.1, anchor=tkinter.CENTER)

delta_inputtwo = tkinter.Button(master=ventana, text='π/4', command=lissajous_delta(2))
delta_inputtwo.place(relx=0.9, rely=0.60, relwidth=0.1, anchor=tkinter.CENTER)

delta_inputthree = tkinter.Button(master=ventana, text='π/2', command=lissajous_delta(3))
delta_inputthree.place(relx=0.9, rely=0.70, relwidth=0.1, anchor=tkinter.CENTER)

delta_inputfour = tkinter.Button(master=ventana, text='3π/4', command=lissajous_delta(4))
delta_inputfour.place(relx=0.9, rely=0.80, relwidth=0.1, anchor=tkinter.CENTER)

delta_inputfive = tkinter.Button(master=ventana, text='π', command=lissajous_delta(5))
delta_inputfive.place(relx=0.9, rely=0.9, relwidth=0.1, anchor=tkinter.CENTER)

# define font
myFont = font.Font(family='Helvetica', size=5, weight='bold')

graficar = tkinter.Button(master=ventana, text='⌁ Graficar datos ⌁', bg='#3892EA', command=lambda: opennewwindow (ventana, a_slider.get(), x_slider.get(), y_slider.get(), float(a_input.get()), float(b_input.get()), frequency_input.get(), interval_input.get()))
graficar.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.1, anchor=tkinter.CENTER)

graficar['font'] = myFont


ventana.mainloop()
