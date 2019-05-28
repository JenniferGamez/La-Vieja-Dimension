#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definiendo el tablero
import sys
import time
import os
from random import randint

# Tablero, Array de un Array, Matriz
DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
tab = []  # Inicializacion del tablero en un array

for x in range(0, DimensionesTab):
  tab.append(["O"] * DimensionesTab) # Introduciendo las filas en Arrays vacios

def MostrarTablero(tab): # Mostrar elementos sin "" ni los [], y organizado por filas al imprimir
# Aqui definimos un tablero
  for fila in tab:
    print " ".join(fila) # Join une los elementos del array 

MostrarTablero(tab)		 # Muestra el tablero en la shell 

