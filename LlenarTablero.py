#!/usr/bin/env python
# -*- coding: utf-8 -*-

#EN PROCESOOOOOOO
import sys
import time
import os
from numpy import *
# Definiendo el tablero cuando se rellena una vez
# aclarado los jugadores y demas
def MostrarTab(N, f, c): # -> Procedimiento Tablero
	# Este construye la matriz, array de un array
	def Tablero(N):
		tab= [  ]
		for i in range(0,N):
			tab.append([  0 ]*N)
		return tab
	# Imprime por elemntos == array
	tablero = Tablero(N)

	for i in range(0,N):
		print tablero[i]
		tablero[f][c] = "X"
			

DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
f = int(input("Fila a trabajar= "))
c = int(input("Columnaa a trabajar= "))

MostrarTab(DimensionesTab, f, c)

### OTRA

def LlenarTablero(fila,columna,tablero, dimensiones, ficha):
	while True:
		try:	
			assert(0 <= fila < dimensiones and 0 <= columna < dimensiones)
		except:
			print "Usted esta seleccionando una casilla fuera de los limites del tablero."
		finally:
			tablero[fila][columna] = ficha #aqui depende del jugador

