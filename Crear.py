#!/usr/bin/env python
#
#-------------------------------------------------------------------
#
#  Universidad Experimental Simon BOlivar
#  Laboratorio de Algoritmos y Estructuras I
#  Jennifer Gamez 16-10396
#  Amaranta Villegas 16-11
#
#-------------------------------------------------------------------
#
#IMPORTANDO LIBRERIA
import sys

#-------------------------------------------------------------------
#                  DEFINIENDO FUNCIONES: Crean
#-------------------------------------------------------------------

# Definicion que crea los tableros N x N
def Tablero_NxN(tamano_Tablero, n):
    # Entrada de la matriz (elementos a rellenar)
    tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
    # Salida del tablero 
    return tablero

# Super Tablero: contiene las dimensiones (conjunto de tableros).
def Super_tablero(tamano):
    #Dimensiones: array que conformado por un conjunto de tableros
    dimensiones = [ z for z in range(tamano)]
    # Cota : Dimensiones -1
    for i in dimensiones:
        dimensiones[i] = Tablero_NxN(tamano, 0)
        # Asigna n == 0, porque inicialmente la matriz esta vacia Tablero_NxN(tamano, n)
    # Salida. Retornando el Super Tablero
    return dimensiones

# Definicion Suma de Linea. Crea una puntuacion en caso de ser valido los datos leidos. 
def SumarLinea(LineaJugador, LineaHorizontal, LineaVertical,LineaDiag,LineaTableros):
  # Inicializa en cero LineaJugador.
  # Este condicional lee 1 como True y 0 False.
  if LineaHorizontal or LineaVertical or LineaDiag or LineaTableros: 
    LineaJugador =  LineaHorizontal + LineaVertical + LineaDiag + LineaTableros # actualiza el contador cuando retorna esto
  else:
    pass # No actualiza el contador si no cumple la condicion de existencia
  return LineaJugador
