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
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.animation import FuncAnimation
from tqdm import tqdm, trange
import time


def lissajous(A, B, Delta): #Función que dibuja las Lissajous.
    a = A
    b = B
    delta = Delta*(3.14)

    fig, ax = plt.subplots()
    datosx, datosy = [], []
    datos, = plt.plot([], [], 'ro')

    def init():
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        return datos,

    def update(frame):
        datosx.append(np.sin((a*frame) + delta))
        datosy.append(np.sin(b*frame))
        datos.set_data(datosx, datosy)
        return datos,

    ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)
    #plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')
    plt.show()
    plt.clf()
    #fig = plt.figure()
    #plt.figure().clear()

def estatico(Vaceleracion, Vvertical, Vhorizontal): #Definición de variables estáticas y las modificables para el movimiento de electrones.
    
    #Variables que modifica el usuario.
    vy = Vvertical #Voltaje vertical (Se modifica)
    vx = Vhorizontal #Voltaje horizontal (Se modifica)
    va = Vaceleracion #Voltaje de aceleracion (Se modifica)
    
    #Variables que no se modifican
    carga = 1.6E-19
    masa = 9.1E-31
    distanciaplacas = 0.02
    distanciax = 0.1

    velocidadx = (((2 * carga * va) / masa) ** (1/2))
    tiempo = distanciax / velocidadx
    acelaraciony = (carga * vy) / (masa * distanciaplacas)
    distanciay = (acelaraciony / 2)*(tiempo ** 2)
    angulo = math.degrees(math.atan(distanciay / distanciax))
    angulo2 = math.degrees(math.atan(distanciay / distanciax))

    opuesto1 = 0.02 * (math.degrees(math.atan(angulo)))
    opuesto2 = 0.02 * (math.degrees(math.atan(angulo2)))


    fig, ax = plt.subplots()
    x = opuesto1
    y = opuesto2
    datos, = plt.plot([], [], 'ro')

    def init():
        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        return datos,

    def update(frame):
        datos.set_data(x, y)
        return datos,

    ani = FuncAnimation(fig, update, frames=np.linspace(2, 20, 100), init_func=init, blit=True)
    #plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str("HOLA"), fontsize=10, color='green')
    plt.show()
    plt.clf()
    #fig = plt.figure()
    #plt.figure().clear()



def menu():
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
            verificar_salida = False


        




menu()
#lissajous(1, 3, (1/2))
#estatico(10, 100, 1)