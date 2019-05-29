
import sys
import time
import os

from random import randint

# Variable GLOBAL
tab = []

def tamanoTablero(tamano_Tablero, n):

	tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
	return tablero


def crearNtablero(ntablero, tamano):
	
	posicion = [ z for z in range(ntablero) ]

	for i in posicion:
		posicion[i] = tamanoTablero(tamano, 0)


	return posicion



if __name__ == '__main__': # inicializar la lectura del programa

	global tab

	numeros_tablero = input("Por favor ingrese los tableros que desea. ")
	tamano_tablero = input("Por favor ingrese el tamano del tablero.  ")

	if 1 <= numeros_tablero <= 5:
		
		tab = crearNtablero(numeros_tablero, tamano_tablero)

		print(tab)

	else:
		print('Error 4.')
		exit()

	refe = input('Elija el tablero a referenciar ')

	test = tab[refe]

	print(test)

