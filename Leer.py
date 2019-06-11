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
#                  DEFINIENDO FUNCIONES: Leen
#-------------------------------------------------------------------


# Mostrar en la consola el tablero por filas (Da la impresion de un tablero) 
def MostrarTablero(Tab): # Mostrar filas al imprimir
# Aqui definimos un tablero por cada llamada fila en el rango de Tab
    # Cota : DimensionesTab -1
    # DimensionesTab es la parte entera (numero) de Tab.
    for fila in Tab:
        print (fila) 

# Funcion. Determina si una jugada esta dentro de los parametros del tablero y no esta ocupada. 
def Jugada_Valida(fila,columna, tablero):
  while True:
    try:
        Valido = True
        # Verificando que la casilla este vacia.
        assert(tablero[fila][columna] == 0)
        assert(fila >= 0 and columna >= 0)
        break
    except:
        # En caso de estar ocupada o fuera de los parametros  
        Valido = False
    finally:
        # Salida de la Funcion.
        return Valido

# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero(fila,columna,tablero,ReferenciaTablero,tamano,ficha):
    # Disponibilidad en la dimension a escoger
    n = tamano - 1

    # fail; cuenta si se presenta un error por Casilla ocupada o inexistente
    fail = 0    
    while True:
        try:
            # Entrada.
            fila = int(input("\nFila a trabajar (E: %s filas): " %n))
            columna = int(input("Columna a trabajar (E: %s columnas): " %n))
            assert (fila >= 0 and columna >= 0)
            assert(float(fila).is_integer())
            assert(float(columna).is_integer())
        except:
            print ("Intente nuevamente.")
        finally:  
            if fila >= 0 and columna >= 0:
            # Llamada de Jugada_Valida evalua si la casilla esta ocupada o no exite.
                if Jugada_Valida(fila,columna, tablero) == True: 
                    tablero[fila][columna] =  ficha 
                    print ("\nTablero %s" %ReferenciaTablero)
                    # Salida. Llama la funcion y muestra el tablero por filas..
                    MostrarTablero(tablero)

                elif (Jugada_Valida(fila,columna, tablero) == False) or (Jugada_Valida(fila,columna, tablero) == None):
                    fail = 1
                    print ("\nIntente nuevamente. Casilla ocupada o inexistente.")
                    print ("\nTablero %s" %ReferenciaTablero)
                    # Salida. Llama la funcion y muestra el tablero por filas.
                    MostrarTablero(tablero)

                # Salida de la Funcion y los datos proporcionados de fila y/o columna.
                return fail,fila,columna
            else:
                pass

# Comprobar / Reafirmar que el tablero seleccionado es el deseado por el usuario.
def OKTablero():
    OK = -1
    while  True:
        try:
            #Condicional de confirmacion de tablero deseado.
            OK = int(input("\nDesea continuar con este tablero?; 1 (Si), 0 (No): "))
            assert(float(OK).is_integer())
            assert( OK == 1 or OK == 0)
            break
        except:
            print ("\nIntente nuevamente. Lea bien la instruccion.")
        finally:
            if OK == 1 or OK == 0:
                if OK:
                    return "OK"
                else:
                    return "NOT OK"


# Funcion que determina la existencia de linea entre tablero y en el tablero
def HayAlinea(SuperTablero, Tablero, Tamano, Fila, Columna, Ficha):
  #SuperTablero: contiene los tableros de todas las dimensiones
  #Tablero: el tablero que selecciona el usuario a realizar su jugada

  def HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha):
    # Valor booleano
    HaylineaHorizontal = 0
    # Tablero
    tab = Tablero[Fila]
    # Evaluando entre tablero si se cumple la condicion
    if all(tab[i] == Ficha for i in range(Tamano) if Tablero[i] != 0 ):
      HaylineaHorizontal = 1
    elif all(tab[i] != Ficha or tab[i] == 0 for i in range(Tamano) if Tablero[i] != 0 ):
      pass
    # Retornando la existencia de Linea Horizontal
    return HaylineaHorizontal

  def HayAlineaVertical(Tablero,Columna,Tamano, Ficha):
    # Valor booleano
    HaylineaVertical = 0
    # Inicializando contador
    cont_vertical = 0
    # Evaluando entre tablero si se cumple la condicion
    # Cota : Tamano -1
    for i in range(Tamano):
      if Tablero[i][Columna] == Ficha and Tablero[i][Columna] != 0: 
        cont_vertical = cont_vertical + 1
      elif Tablero[i][Columna] != Ficha or Tablero[i][Columna] == 0:
        pass
    # Evaluando existencia
    if cont_vertical == Tamano:
      HaylineaVertical = 1
    else:
      pass
    # Retornando la existencia de Linea Vertical
    return HaylineaVertical

  def HayAlineaDiagonal(Tablero,Tamano,Ficha):
    # Valor booleano
    HayAlineaDiagonal= 0
    # Inicializando contador
    cont_diagonal = 0
    # Evaluando entre tablero si se cumple la condicion
    # Cota : Tamano -1
    for i in range(0,Tamano):
      # Cota : Tamano -1
      for j in range (0,Tamano):  
        if Tablero[i][j] == Ficha and i == j: 
          cont_diagonal = cont_diagonal + 1
        else: 
          pass
    # Evaluando existencia      
    if cont_diagonal == Tamano:
      HayAlineaDiagonal = 1
    elif cont_diagonal != Tamano:
      pass
    # Retornando la existencia de Linea Diagonal
    return HayAlineaDiagonal
  
  def HayAlineaTableros(SuperTablero,Fila,Columna,Tamano, Ficha):
    # Posicion del primero tablero a escoger. Valor fijo. Ctte.
    k = 0  
    # Tablero ctte, nuestro tablero a comparar sera el fijo
    TableroFijo = SuperTablero[k] 
    # Valor de existencia.
    HayAlineaTablero = 0
    # Contador 
    contador_lineaTablero = 0

    # Evaluando entre tablero si se cumple la condicion
    # Cota : DimensionesTab -1  
    # DimensionesTab es el entero (numero) de SuperTablero
    for Tablero in SuperTablero:
      if (TableroFijo[Fila][Columna] == Tablero[Fila][Columna] == Ficha):
        contador_lineaTablero = contador_lineaTablero + 1
      else:
        pass
    # Evaluando existencia
    if contador_lineaTablero == Tamano:
       HayAlineaTablero = 1
    else:
      pass
    # Retornando existencia
    return HayAlineaTablero  

  ###LLAMADA DE LAS FUNCIONES INTERNAS###
  return HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha), HayAlineaVertical(Tablero,Columna,Tamano,Ficha),\
HayAlineaDiagonal(Tablero,Tamano,Ficha), HayAlineaTableros(SuperTablero,Fila,Columna,Tamano, Ficha)