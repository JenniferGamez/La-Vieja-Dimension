#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os

#ENTRADA IDENTIFICACION
while True:
	try: 
		#ENTRADA IDENTIFICACION
		print "Bienvenidos a HIMALAYA"
		print "Identificacion de Jugadores"
		Jugador1 = str(raw_input("Ingrese el nombre del Jugador 1:"))
		Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2:"))

		# CREO QUE FALTA RESOLVER ESTO PARA QUE LA ENTRADA NO TENGA EL ERROR DE SER VACIO EN LOS NOMBRES
		print "Jugador1 = %s" , Jugador1
		print "Jugador2 = %s" , Jugador2

		#ENTRADA DIMENSIONES DEL JUEGO
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		assert (DimensionesTab >= 2)
		assert(float(DimensionesTab).is_integer())		#entra estrictamente entero positivo
		break
	
	except:
		print "\n**Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2.**"
		print "Intente nuevamente."
	
	finally:
		# print "Tablero %s x %s en %s dimesiones.\n" %(DimensionesTab,DimensionesTab,DimensionesTab)
		print "\nAqui podria ir la parte si esta seguro de las dimesiones del juego.\n"
		# MostrarTab(DimensionesTab)
		MostrarTab(DimensionesTab)
