# #!/usr/bin/env python

import sys
import time
import os

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
        print fila 

#Funcion. Determina si una jugada esta dentro de los parametros del tablero o no esta ocupada. 
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
            if letra == "X":
                Asig_1 = "X" #Jugador1
                Asig_2 = "O" #Jugador2
                return Asig_1 , Asig_2
            elif letra == "O":
                Asig_1 = "O" #Jugador1
                Asig_2 = "X" #Jugador2
                return Asig_1 , Asig_2

# Decidiendo quien comienza la partida primero
def QuienIniciaPartida(Jugador1, Jugador2, ficha1, ficha2):
    # Inicializacion 
    CambioJugador = 0
    CambioFicha = 0

    # Salida
    print "\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1)
    print "Jugador2 = %s con la ficha %s" %(Jugador2,ficha2)

    # Entrada
    Escoge= int(input("\nQuieres que ese sea el orden de turnos? Primero %s y luego %s 1 (Si), 0 (No): " %(ficha1,ficha2)))
    if Escoge:    # si escoge 1 entonces se toma como true y por lo tando no coloco escoge == 1 sino solo escoge para cuando es X
        pass
    else:
        # realizando un intercambio del orden de los jugadores con sus respectivas fichas
        CambioJugador = Jugador1
        Jugador1 = Jugador2
        Jugador2 = CambioJugador

        CambioFicha = ficha1
        ficha1 = ficha2
        ficha2 = CambioFicha

        print "\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1)
        print "Jugador2 = %s con la ficha %s" %(Jugador2,ficha2)
    return Jugador1, Jugador2, ficha1, ficha2

# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero(fila,columna,tablero,ReferenciaTablero,tamano,ficha):
    # Disponibilidad en la dimension a escoger
    n = tamano - 1

    # fail; cuenta si se presenta un error por Casilla ocupada o inexistente
    fail = 0    
 
    fila = int(input("\nFila a trabajar (E: %s filas): " %n))
    columna = int(input("Columna a trabajar (E: %s columnas): " %n))

    # Llamada de Jugada_Valida evalua si la casilla esta ocupada o no exite.
    if Jugada_Valida(fila,columna, tablero) == True: 
        tab[fila][columna] =  ficha 
        print "\nTablero %s" %ReferenciaTablero
        # MOSTRANDO EL TABLERO POR FILAS
        MostrarTablero(tablero)

    elif Jugada_Valida(fila,columna, tablero) == False:
        fail = fail + 1
        print "\nIntente nuevamente. Casilla ocupada o inexistente."
        print "\nTablero %s" %ReferenciaTablero
        # MOSTRANDO EL TABLERO POR FILAS
        MostrarTablero(tablero)
      
    return fail

# Escoger Tablero
def ChooseTablero(Jugador,TablerosDisponible):
    while True:
        try:     
            # Seleccionar tablero a preferencia por el jugador
            ReferenciaTablero = input('\n%s, elije el tablero a jugar. Recuerde que puede elergir un tablero entre: %s tablero(s) \
contando el tablero 0: '%(Jugador, TablerosDisponible))
            assert(float(ReferenciaTablero).is_integer())
            # COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO    
            assert((ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible))     
            break
        
        except:
            print "\nUsted ha elegido un tablero inexistente en la Dimension."
            print "Intente nuevamente."
        
        finally:
            if (ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible):
                return ReferenciaTablero   

# Comprobar / Reafirmar que el tablero seleccionado es el deseado por el usuario.
def OKTablero():
    while  True:
        try:
            #Condicional de confirmacion de tablero deseado:
            OK = int(input("\nDesea continuar con este tablero?; 1 (Si), 0 (No): "))
            assert(float(OK).is_integer())
            assert( OK == 1 or OK == 0)
        except:
            print "\nIntente nuevamente. Lea bien la instruccion."
        finally:
            if OK == 1 or OK == 0:
                if OK:
                    return "OK"
                else:
                    return "NOT OK"


