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



                ###### ESTOS ADJUNTADOS SON LOS EMPLEADOS
  
  # Definicion que crea los tableros N x N
def Tablero_NxN(tamano_Tablero, n):
	# entrada de la matriz (elementos a rellenar)
	tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
	return tablero

# Super Tablero este contiene las dimensiones (conjunto de tablero)
def Super_tablero(tamano):
	dimensiones = [ z for z in range(tamano)] #Array que contedra los demas tableros
	for i in dimensiones:
		dimensiones[i] = Tablero_NxN(tamano, 0)
		# Asigna n == 0, porque inicialmente la matriz esta vacia
	return dimensiones+

#IMPRIMIR EL TABLERO. PROCEDIMIENTO 
def MostrarTablero(tab): # Mostrar elementos sin "" ni los [], y organizado por filas al imprimir
# Aqui definimos un tablero
	for fila in tab:
		print fila # Join une los elementos del array

