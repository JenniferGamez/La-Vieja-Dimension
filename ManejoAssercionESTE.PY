#!/usr/bin/env python

#IMPORTANDO LIBRERIAS
import sys
import time
import os

								###DEFINIENDO PROCEDIMIENTOS Y FUNCIONES###

# Definicion que crea los tableros N x N
def Tablero_NxN(tamano_Tablero, n):
	# Entrada de la matriz (elementos a rellenar)
	tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
	return tablero

# Super Tablero: contiene las dimensiones (conjunto de tablero)
def Super_tablero(tamano):
	dimensiones = [ z for z in range(tamano)] #Array que contedra los demas tableros
	for i in dimensiones:
		dimensiones[i] = Tablero_NxN(tamano, 0)
		# Asigna n == 0, porque inicialmente la matriz esta vacia
	return dimensiones

#IMPRIMIR EL TABLERO. PROCEDIMIENTO 
def MostrarTablero(tab): # Mostrar filas al imprimir
# Aqui definimos un tablero
	for fila in tab:
		print fila # Join une los elementos del array

# LLENAR EL TABLERO CON LA FICHA DEL JUGADOR DE TURNO
def Jugada_Valida(fila,columna, dimensiones, Valido):
	while True:
		try:	
			# Verificando la casilla se encuentra dentro del tablero
			assert((0 <= fila < dimensiones) and (0 <= columna < dimensiones))
			break
		except:
			print "Usted ha seleccionando una casilla fuera de los limites del tablero."
		finally:
			try:
				# Verificando que la casilla este vacia.
				assert(tablero[fila][columna] == 0)
				break
			except:
				Valido = False
				return Valido
			finally:
				Valido = True
				return Valido

# DEFINIENDO LAS FICHAS 
def QueQuiereSer(Jugador1, Jugador2): #El jugador decide si quiere ser X y O
	while True:
		try: 
			letra = str(raw_input("\n%s, Quieres ser la ficha X o la letra O?: " %Jugador1)).upper() 
			# letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan
			assert(letra == "X" or letra == "O")
		except:
			print "Intente nuevamente."
		finally:
			#Asignando las fichas a los jugadores
			if letra == 'X':
				Asig_1 = "X" #Jugador1
				Asig_2 = "O" #Jugador2
				return Asig_1 , Asig_2
			elif letra == 'O':
				Asig_1 = "O" #Jugador1
				Asig_2 = "X" #Jugador2
				return Asig_1 , Asig_2


									###PROGRAMA PRINCIPAL###

while True: #DIMENSIONES 
	try:	
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		# Aseguramos que la entrada sea un entero estrictamente .is_integer()
		assert(float(DimensionesTab).is_integer())	
		assert ( DimensionesTab > 0 and DimensionesTab >= 2)
		break 											
	except:
		print "Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2."
		print "Intente nuevamente."
	finally:
		# Se ejecuta si las aserciones se cumplen.
		if DimensionesTab > 0 and DimensionesTab >= 2: 
			print "\nHas elegido un tablero: %s x %s." %(DimensionesTab,DimensionesTab)
			print "Dimensiones a jugar: %s Dimensiones." %DimensionesTab

		while True:	#IDENTIFICACION
			try:	
				#ENTRADA.
				Jugador1 = str(raw_input("\nIngrese el nombre del Jugador 1: ")).upper()
				Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2: ")).upper()

				assert(len(Jugador1) > 0)
				assert(len(Jugador2) > 0)
				break
			except:
				print "\nLa identificacion de los jugadores es esencial."
				print "Por favor ingrese una identificacion valida."
			finally:
				# Se ejecuta si las aserciones se cumplen.
				if len(Jugador1) > 0 and len(Jugador2) > 0:
					# SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
					print "\nJugador1 = %s" %Jugador1
					print "Jugador2 = %s" %Jugador2

					# Asigando valores a variables locales
					ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

					# Monstrando los resultados
					print "\n%s sera las: %s y %s sera: %s." %(Jugador1,ficha_jug1,Jugador2,ficha_jug2)

					# CONSTRUYENDO LOS TABLEROS EN LA DIMENSION SELECCIONADA 
					Sup_Tab = Super_tablero(DimensionesTab)

				while True:# ELIGIENDO TABLERO.
					try: 
						n = DimensionesTab - 1
						refe = input('\nElija el tablero a jugar. Recuerde que puede elergir un tablero \
entre: %s tablero(s) contando el tablero 0: '%n)
						# COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO
						assert ((refe >= 0) and (refe <= n)) 
						assert(float(refe).is_integer())		
						break
					except:
						print "\nUsted ha elegido un tablero inexistente en la Dimension."
						print "Intente nuevamente."
					finally:
						if (refe >= 0) and (refe <= n):
							# LLAMADA DEL TABLERO SELECCIONADO
							tab = Sup_Tab[refe]		
							print "\nTablero %s" %refe
