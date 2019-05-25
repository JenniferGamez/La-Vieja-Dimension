#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definiendo el tablero
import sys
import os

def MostrarTab(N): # -> Procedimiento Tablero
	def Tablero(N):
		tab= []
		for i in range(0,N):
			tab.append([0]*N)
		return tab

	tablero = Tablero(N)
	for i in range(0,N):
		print tablero[i]	
						
###NOTA: por ser procedimiento solo se llama sin el print
