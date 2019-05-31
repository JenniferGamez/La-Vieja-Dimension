# #!/usr/bin/env python

import sys
import time
import os

# Definicion que crea los tableros N x N
def Tablero_NxN(tamano_Tablero, n):
	# entrada de la matriz (elementos a rellenar)
	tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
	return tablero

# Definicion de un arreglo con las matrices contruidas
# Super Tablero este contiene las dimensiones (conjunto de tablero)
def Super_tablero(tamano):
	dimensiones = [ z for z in range(tamano)] #Array que contedra los demas tableros
	for i in dimensiones:
		dimensiones[i] = Tablero_NxN(tamano, i)
	return dimensiones+

#IMPRIMIR EL TABLERO 
def MostrarTablero(tab): # Mostrar elementos sin "" ni los [], y organizado por filas al imprimir
# Aqui definimos un tablero
	for fila in tab:
		print fila # Join une los elementos del array

# LLENAR EL TABLERO CON LA FICHA DEL JUGADOR DE TURNO
def LlenarTablero(fila,columna,tablero, dimensiones, ficha):
	while True:
		try:	
			assert((0 <= fila < dimensiones) and (0 <= columna < dimensiones))
		except:
			print "Usted esta seleccionando una casilla fuera de los limites del tablero."
		finally:
			# Asignando la ficha, esta una variable esto depende del Jugador1 y Jugador2
			tablero[fila][columna] = ficha 
			return tablero

# Fichas
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
# Asigando valores a variables locales
ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

# Monstrando los resultados
print "\n%s sera las: %s y %s sera: %s." %(Jugador1,ficha_jug1,Jugador2,ficha_jug2)
			
#### INICIOOOO
import sys

while True:
	try: 
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		assert (DimensionesTab >= 3)
		assert(float(DimensionesTab).is_integer())		#aseguramos que la entrada sea un entero estrictamente
		break 											#indica que si no se cumple para y pide que sea corregido el erorr
	except:
		print "Las dimesiones del tablero son estrictamente numericas y mayores iguales a 3."
		print "Intente nuevamente."


print "\nHas elegido un tablero %s x %s y profundidad %s." %(DimensionesTab,DimensionesTab,DimensionesTab) 

##################
