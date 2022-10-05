import numpy as np
import funciones as fn

class tablero:
    def __init__(self, id_tablero):
        self.id_tablero = id_tablero
        self.forma = np.full((10,10), " ")
        self.barcos = 0

class navio:
    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.ubicacion = []