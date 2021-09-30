import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from time import time

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

distancia = 0.03
carga = 1.602e-17
masa = 1.67e-27
velocidad = 5e+5
voltaje = 1

fig, ax = plt.subplots()
datosx, datosy = [], []
datos, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 0.4)
    ax.set_ylim(-0.1, 0.1)
    return datos,

def update(frame):
    datosx.append(frame)
    datosy.append(((carga * voltaje)/(2 * masa * distancia)) * (( frame /velocidad) ** 2))
    datos.set_data(datosx, datosy)
    return datos,

def funcioncontador():
    #Ciclo para tomar el tiempo
    lista = {}
    contador = 0.001
    for i in range(300):
        ejey = ((carga * voltaje)/(2 * masa * distancia)) * (( contador /velocidad) ** 2)
        lista[contador] = ejey
        contador =+ 0.001

tiempoinicio = time()
funcioncontador()
tiempo = time() - tiempoinicio

ani = FuncAnimation(fig, update, frames=np.linspace(0.001, 0.3, 20), init_func=init, blit=True)
plt.text(0.08, 0.08, "Tiempo de ejecucion: " + str(tiempo), fontsize=10, color='green')
plt.show()