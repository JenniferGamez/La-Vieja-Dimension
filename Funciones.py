# #!/usr/bin/env python

import sys
import time
import os

#Juagada Valida
def Jugada_Valida(fila,columna, tablero):
  while True:
    try:
      Valido = True
      # Verificando que la casilla este vacia.
      assert(tablero[fila][columna] == 0)
      assert(fila >= 0 and columna >= 0)
      break
    except:
      Valido = False
      return Valido
    finally:
        return Valido

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

# Jugada completa por tablero
# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero(fila,columna,tablero,turno,ReferenciaTablero,tamano):
    # Disponibilidad en la dimension
    n = tamano - 1

    # fail; cuenta lo errores obtenidos por Casilla ocupada o inexistente.
    fail = 0    

    for i in range(turno):
        fila = int(input("\nFila a trabajar (E: %s filas): " %n))
        columna = int(input("Columna a trabajar (E: %s columnas): " %n))

        if Jugada_Valida(fila,columna, tablero) == True:
            tab[fila][columna] = "x" ###AQUI FALTA DEFINIR LA FICHA DE DICHO TURNO
            print "\nTablero %s" %ReferenciaTablero
            # MOSTRANDO EL TABLERO POR FILAS
            MostrarTablero(tablero)

        elif Jugada_Valida(fila,columna, tablero) == False:
            fail = fail + 1
            print "\nIntente nuevamente. Casilla ocupada o inexistente."
            print "\nTablero %s" %ReferenciaTablero
            # MOSTRANDO EL TABLERO POR FILAS
            MostrarTablero(tablero)
      
        i = i + 1

    return fail
##################
