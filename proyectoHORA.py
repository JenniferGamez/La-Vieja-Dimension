#La vieja  cool
#No desistas. Echale.
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

#programa

DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))

# CONTRUYENDO LOS TABLEROS Y HACIENDO LA LLAMADA DEL TABLERO A TRABAJAR
if 1 <= DimensionesTab: #REALIZAR UN ASSERT ROBUSTO
	Sup_Tab = Super_tablero(DimensionesTab) # Formando los supertableros o Dimensiones
	print "Dimensiones a jugar: %s Dimensiones" %DimensionesTab

else:
	print('Error 4.')
	exit()

#ENTRADA. IDENTIFICACION
Jugador1 = str(raw_input("\nIngrese el nombre del Jugador 1: ")).upper() 
Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2: ")).upper() 

# SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
print "\nJugador1 = %s" %Jugador1
print "Jugador2 = %s" %Jugador2

# Asigando valores a variables locales
ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

# Monstrando los resultados
print "\n%s sera las: %s y %s sera: %s." %(Jugador1,ficha_jug1,Jugador2,ficha_jug2)

#definiendo de quien sera el primer turno REALIZAR DEFINICION BUCLE
### ESTO DEBERIA ESTAR EN UN BUCLE .... THINK
print "\nARREGLAR aqui falta algo"
print "\nTurno: %s" 	%1	# aquie deberia estar el turno que se esta jugando 
print "Jugador: %s "	%Jugador1	# nombre del jugador 

# ELIGIENDO TABLERO. BUCLE ESTO
refe = input('\nElija el tablero a jugar. Recuerde que puede elergir entre %s \
tablero(s): '%DimensionesTab)
tab = Sup_Tab[refe]		# Llamada del tablero a llenar y/o Dimension
print "\nTablero %s" %refe
MostrarTablero(tab)

# Cambiando valores del tablero seleccionado
fila = int(input("\nFila a trabajar: "))
columna = int(input("Columna a trabajar: "))

# Llenando el tablero con la ficha del jugador
jugada= LlenarTablero(fila,columna,tab,DimensionesTab,ficha_jug1) 
print "\nTablero %s" %refe
MostrarTablero(jugada)		# Impresion del talero

"""
## esto debe ser una definicion, que involucre la impresion del tablero
refe = input('\nElija el tablero a jugar. Recuerde que puede elergir entre %s \
tablero(s): '%DimensionesTab)

print "\nTablero %s" %refe

MostrarTablero(tab)

#esto debe ser una definicion
fila = int(input("\nFila a trabajar: "))
columna = int(input("Columna a trabajar: "))

jugada= LlenarTablero(fila,columna,tab,DimensionesTab, ficha_jug2)
MostrarTablero(jugada)
"""
