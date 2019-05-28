#!/usr/bin/env python
# -*- coding: utf-8 -*-


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

