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
from tkinter import Tk, Frame, Button, Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
    plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')

    """ax = fig.add_subplot(111)
    bar1 = FigureCanvasTkAgg(fig, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    
    ax.set_title('Punto Estatico')"""

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

    def iniciar():
        ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)
        canvas.draw()

    ventana = Tk()
    ventana.geometry('1000x800')
    ventana.wm_title('Proyecto Fisica 3')
    ventana.minsize(width=1200, height=500)

    frame = Frame(ventana, bg='white', bd=3)
    frame.pack(expand=1, fill='both')

    canvas = FigureCanvasTkAgg(fig, master = frame)
    canvas.get_tk_widget().pack(padx=5, pady=10, expand=1, fill='both', side=tkinter.RIGHT)

    button_graficar = Button(frame, text='Graficar datos', width=15, bg='purple4', fg='white', command=iniciar).pack(pady=5,
                                                                                                   side='left', expand=3)

    ventana.mainloop()



    #plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')
    #plt.show()



 
  


'''figure2 = plt.Figure(figsize=(5,4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax2.set_title('Year Vs. Unemployment Rate')

figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Stock_Index_Price']) 
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')'''

#root1.mainloop()

'''def menu():
    verificar_salida = True

    while(verificar_salida):

        opcion_menu = 0

        print("\n⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁ CRT Simulator (Lissajous Figure Representation) ⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁⌁\n")

        print("1. Simular comportamiento de un CRT")
        print("2. Salir\n")
        
        while(True):
            
            
            #Se manejan los errores en esta seccion.
            try:
                opcion_menu = input("Ingrese una opción: ")
                opcion_menu = int(opcion_menu)

                if(opcion_menu == 1 or opcion_menu == 2):
                    print("Aceptando su solicitud...\n")
                    for i in tqdm([1,2,3,4,5]):
                        time.sleep(0.3)
                    print("\n\n")
                    break
                if(opcion_menu < 1 or opcion_menu > 2):
                    print("¡Opcion invalida! Ingrese una de las opciones existentes :)\n")

            except ValueError:
                print("¡Solo se aceptan valores numericos! Ingrese de nuevo una opcion\n")
            
        #Se llevan a cabo las opciones seleccionados.
        if(opcion_menu == 1):
            A = input()
            A = int(A)
            B = input()
            B = int(B)
        elif(opcion_menu == 2):
            print("\n¡Gracias por utilizar el simulador, regresa pronto!\n")
            verificar_salida = False'''


grafico(1, 3, (1/2), 100, 100, 100)