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

#Importando Modulos de entrada y lectura de Datos
import Entradas
from Entradas import *
import Leer
from Leer import *
import Crear
from Crear import *
 
#-------------------------------------------------------------------
#
#                  LA VIEJA COOL 
#                       
#-------------------------------------------------------------------

def OtraPartida():
                            
    # Llamada de la funcion Dimension
    DimensionesTab = Dimension(0)
    
    # Mensaje de las Dimensiones seleccionada por los usuario
    print ("\nHas elegido un tablero: %s x %s." %(DimensionesTab,DimensionesTab))
    print ("Dimensiones a jugar: %s Dimensiones." %DimensionesTab)
    
    # Identificacion de Jugadores
    Jugador1, Jugador2 = Identificacion(0,0)

    print ("\nJugador1 = %s" %Jugador1)
    print ("Jugador2 = %s" %Jugador2)

    # Asigando las fichas
    ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

    # Monstrando los resultados. Se llama la funcion para reafirmar la informacion proporcionada por los usuarios.
    Jugador1, Jugador2, ficha_jug1, ficha_jug2 = QuienIniciaPartida(Jugador1, Jugador2, ficha_jug1, ficha_jug2)

    # Construyendo los tableros en la dimension / tamano seleccionada.
    SuperTableros = Super_tablero(DimensionesTab)

    # Disponibilidad de tablero a escoger.
    n = DimensionesTab - 1 

    # Fichas entre todos los tableros
    Fichas = DimensionesTab * DimensionesTab * DimensionesTab 

    # Fichas entre el mismo tablero
    PartidaTablero = DimensionesTab * DimensionesTab 

    # Inicializando Contador de Lineas.
    LineaJugador1 = 0
    LineaJugador2 = 0 

    # JUGANDO EN LOS TABLEROS
    # Cota : Fichas -1
    for i in range (Fichas):

        if i % 2 == 0 : # Par: Jugador 1
            # Salida. Mensaje
            print ("\nJuegan las: %s, Jugador: %s." %(ficha_jug1,Jugador1))

            print ("Fichas disponible(s): %s" %Fichas)

            # Referencia del tablero a escoger.
            refe = ChooseTablero(Jugador1, n)

            # Tablero
            Tablero = SuperTableros[refe]    
            print ("\nTablero %s" %refe)
            MostrarTablero(Tablero)

            while True:
                try:
                    # Confirmacion de tablero deseado
                    OK = OKTablero()
                    assert(OK == "OK")
                    break
                except:
                    # Referencia del tablero a escoger.
                    refe = ChooseTablero(Jugador1, n)

                    # Tablero
                    Tablero = SuperTableros[refe]    
                    print ("\nTablero %s" %refe)
                    MostrarTablero(Tablero)

                finally:                              
                    if OK == "OK":
                        turno_fail,fila,columna = JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug1)
                        # Condicional por si la fila y/o columna seleccionada se salen de la dimension.
                        if turno_fail > 0: # Se sale de la dimension
                            JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug1)
                        elif turno_fail == 0: # Se mantiene en la dimension
                            # Verificando si hay Linea.
                            LineaHorizontal,LineaVertical,LineaDiag,LineaTableros= HayAlinea(SuperTableros,\
Tablero, DimensionesTab, fila, columna, ficha_jug1)

                            # Sumando si hay linea.
                            LineaJugador1 =  LineaJugador1 + SumarLinea(LineaJugador1, LineaHorizontal,\
LineaVertical,LineaDiag,LineaTableros)
                            # Salida de los resultados obtenidos con la jugada del jugador.
                            print ("\nLinea(s) Realizadas = %s" %LineaJugador1)
                    else:
                        pass
        elif i % 2 != 0: # Impar: Jugador 2
            # Jugador actual.
            print ("\nJuegan las: %s, Jugador: %s." %(ficha_jug2,Jugador2))

            print ("Fichas disponible(s): %s" %Fichas)

            # Referencia del tablero a escoger.
            refe = ChooseTablero(Jugador2, n)

            # Tablero
            Tablero = SuperTableros[refe]    
            print ("\nTablero %s" %refe)
            MostrarTablero(Tablero)

            while True:
                try:
                    # Confirmacion de tablero deseado
                    OK = OKTablero()
                    assert(OK == "OK")
                    break
                except:
                    # Referencia del tablero a escoger.
                    refe = ChooseTablero(Jugador2, n)

                    # Tablero
                    Tablero = SuperTableros[refe]    
                    print ("\nTablero %s" %refe)
                    MostrarTablero(Tablero)

                finally:                              
                    if (OK ==str("OK")):
                        turno_fail,fila,columna = JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug2) 
                        # Condicional por si la fila y/o columna seleccionada se salen de la dimension.
                        if turno_fail > 0: # Se sale de la dimension
                            JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug2)
                        elif turno_fail == 0: # Se mantiene en la dimension
                            # Verificando si hay Linea.
                            LineaHorizontal,LineaVertical,LineaDiag,LineaTableros= HayAlinea(SuperTableros,\
Tablero, DimensionesTab, fila, columna, ficha_jug2)

                            # Sumando si hay linea.
                            LineaJugador2 = LineaJugador2 +  SumarLinea(LineaJugador2, LineaHorizontal,\
LineaVertical,LineaDiag,LineaTableros)
                            # Salida de los resultados obtenidos con la jugada del jugador.
                            print ("\nLinea(s) Realizadas = %s" %LineaJugador2)
                    else:
                        pass                                                  
        # Cada vez que juega disminuye una ficha
        Fichas = Fichas - 1     

    # Al acabarse la partida.    
    # Quien es el ganador?                        
    if LineaJugador1 > LineaJugador2:
      print ("\nHAZ GANADO! %s" %(Jugador1))
    elif LineaJugador1 < LineaJugador2:
      print ("\nHAZ GANADO! %s" %(Jugador2)) 
    elif LineaJugador1 == LineaJugador2:
        print ("\nEMPATE!")
    # Resultados obtenidos de la partida
    print ("\nTotal resultados: %s= %s lineas. %s= %s lineas" %(Jugador1,LineaJugador1,Jugador2,LineaJugador2))

    # Y si queremos volver a dar otra jugada. Una revancha o mas nivel en el tablero.
    while True:
        try:
            Otra = int(input("\nDesean jugar otra partida?; 1 (Si), 0 (No):"))
            assert(float(Otra).is_integer())
            assert( Otra == 1 or Otra == 0)
            break
        except:
            print ("\nIntente nuevamente.")
        finally:
            if Otra == 1 or Otra == 0:
                if Otra:
                    # Otra partida.
                    OtraPartida()
                else:
                    # Se acabo.
                    print ("\nExcelente partida.")                            

# Llamando el procedimiento principal
OtraPartida()