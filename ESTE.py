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

def Jugada_Valida(fila,columna, tablero):
	while True:
		try:
			Valido = True
			# Verificando que la casilla este vacia.
			assert(tablero[fila][columna] == 0)
			break
		except:
			Valido = False
			return Valido
		finally:
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

while True:
	try:	#DIMENSIONES 
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		assert (DimensionesTab >= 2)
		# Aseguramos que la entrada sea un entero estrictamente .is_integer()
		assert(float(DimensionesTab).is_integer())		
		break 											
	except:
		print "Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2."
		print "Intente nuevamente."
	finally:
		print "\nHas elegido un tablero: %s x %s." %(DimensionesTab,DimensionesTab)
		print "Dimensiones a jugar: %s Dimensiones." %DimensionesTab
		
		try:	#IDENTIFICACION
			#ENTRADA.
			Jugador1 = str(raw_input("\nIngrese el nombre del Jugador 1: ")).upper()
			Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2: ")).upper()

			### AIUDA ARREGLAR NO ME LEE EL ASSERT
			print "NO LEE ESTE ASSERT LINE 95"
			assert(len(Jugador1) != 0)	#para indicar que es distinto de vacio
			assert(len(Jugador2) != 0)
			break
		except:
			print "\nLa identificacion de los jugadores es esencial."
			print "Por favor ingrese una identificacion valida."
		finally:
			# SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
			print "\nJugador1 = %s" %Jugador1
			print "Jugador2 = %s" %Jugador2

			# Asigando valores a variables locales (FICHAS)
			ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

			# Monstrando los resultados
			print "\n%s sera las: %s y %s sera: %s." %(Jugador1,ficha_jug1,Jugador2,ficha_jug2)

			# CONSTRUYENDO LOS TABLEROS EN LA DIMENSION SELECCIONADA 
			Sup_Tab = Super_tablero(DimensionesTab)

			try: # ELIGIENDO TABLERO.
				refe = input('\nElija el tablero a jugar. Recuerde que puede elergir entre %s \
tablero(s): '%DimensionesTab)
				# COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO 
				assert (refe >= 0 and refe < DimensionesTab) 
				assert(float(refe).is_integer())		
				break
			except:
				# NO LEE ESTE ASSERT NJDS TOY ARRECHA
				print "\nUsted ha elegido un tablero inexistente en la Dimension indicada."
				print "Intente nuevamente."
			finally:
				# LLAMADA DEL TABLERO SELECCIONADO
				tab = Sup_Tab[refe]		
				print "\nTablero %s" %refe

				#MOSTRANDO EL TABLERO POR FILAS
				MostrarTablero(tab)

				try:
					#ANTES DE ESTO SUPONGO DEBE HABER UN BOOCLE CUANDO SE CUENTA LAS FICHAS Y ESO

					#COMPROBANDO JUGADA 
					fila = int(input("\nFila a trabajar: "))
					columna = int(input("Columna a trabajar: "))
					# Verificando la casilla se encuentra dentro del tablero
					assert(float(fila.is_integer()) and float(columna.is_integer()) )
					assert((0 <= fila < dimensiones) and (0 <= columna < dimensiones))
					break
				except:
					print "\nUsted ha seleccionando una casilla fuera de los limites del tablero."
					print "Intente nuevamente. Casilla ocupada."
				finally:
					#### BUCLE CON LA FUNCION DE LAS FICHAS QUE SE HAN PUESTO YA
					if Jugada_Valida(fila,columna, tab) == True:
						tab[fila][columna] = ficha_jug1  ###AQUI FALTA DEFINIR LA FICHA DE DICHO TURNO
						print "\nTablero %s" %refe
						# MOSTRANDO EL TABLERO POR FILAS
						MostrarTablero(tab)

						if Jugada_Valida(fila,columna, tab) == True:
							tab[fila][columna] = ficha_jug1  ###AQUI FALTA DEFINIR LA FICHA DE DICHO TURNO
							print "\nTablero %s" %refe
							# MOSTRANDO EL TABLERO POR FILAS
							MostrarTablero(tab)

						elif Jugada_Valida(fila,columna, tab) == False:### NO LLEGA A ESTE SUBPROGRAMA
							print "\nIntente nuevamente. Casilla ocupada."
							fila = int(input("\nFila a trabajar: "))
							columna = int(input("Columna a trabajar: "))
							Jugada_Valida(fila,columna, tab)

					elif Jugada_Valida(fila,columna, tab) == False:### NO LLEGA A ESTE SUBPROGRAMA
						print "Intente nuevamente. Casilla ocupada."
						fila = int(input("\nFila a trabajar: "))
						columna = int(input("Columna a trabajar: "))
						Jugada_Valida(fila,columna, tab)
