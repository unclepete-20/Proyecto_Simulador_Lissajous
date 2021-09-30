import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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

a = 1
b = 2
delta = 3.14/2

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