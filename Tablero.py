#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definiendo el tablero
import sys
import time
import os
# Matriz Inicial
def MostrarTab(N): # -> Procedimiento Tablero
	# N es la dimension del Tablero N x N
	def Tablero(N):
		tab= [] 				# Creamos un arreglo vacio, donde tendra como elementos otros arreglos
		for i in range(0,N):
			tab.append([0]*N) 	# introdujendo arreglos vacios al arreglo creado
		return tab

	tablero = Tablero(N)
	for i in range(0,N):
		print tablero[i]	
							
###NOTA: por ser procedimiento solo se llama sin el print
							##################################

MostrarTab(DimensionesTab)
