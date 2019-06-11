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
#                  DEFINIENDO FUNCIONES: Entrada
#-------------------------------------------------------------------


# Deficiones Dimensiones a trabajar
def Dimension(DimensionesTablero): 
    while True: 
        try:
            # Entrada. Dimension o tamano de los tableros a jugar.    
            DimensionesTablero = int(input("\nIndique las dimesiones del tablero a jugar = "))
            # Aseguramos que la entrada sea un entero estrictamente .is_integer()
            assert(float(DimensionesTablero).is_integer())  
            assert ( DimensionesTablero >= 2)
            break                                           
        except:
            print ("Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2.")
            print ("Intente nuevamente.")
        finally:
            if DimensionesTablero >= 2:
                return DimensionesTablero
            else:
                pass

# Funcion de Entrada Identificacion de los usuarios
def Identificacion(Jugador1,Jugador2):
    while True: # Identificacion
        try:    
            #ENTRADA.
            J1 = str(raw_input("\nIngrese el nombre del Jugador 1: ")).upper()
            J2 = str(raw_input("Ingrese el nombre del Jugador 2: ")).upper()

            assert(len(J1) > 0)
            assert(len(J2) > 0)
            break

        except:
            print ("\nLa identificacion de los jugadores es esencial.")
            print ("Por favor ingrese una identificacion valida.")

        finally:
            # Se ejecuta si las aserciones se cumplen.
            if len(J1) > 0 and len(J2) > 0:
                # SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
                return J1, J2
            else:
                pass

# Definiendo las fichas a emplear en los tableros. 
def QueQuiereSer(Jugador1, Jugador2): #El jugador decide si quiere ser X y/o O
    while True:
        try: 
            letra = str(raw_input("\n%s, Quieres ser la ficha X o la ficha O?: " %Jugador1)).upper() 
            # letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan
            assert(letra == "X" or letra == "O")
            break
        except:
            print ("Intente nuevamente.")
        finally:
            #Asignando las fichas a los jugadores
            if letra == "X" or letra == "O":
                if letra == "X":
                    Asig_1 = "X" #Jugador1
                    Asig_2 = "O" #Jugador2
                    
                else:
                    Asig_1 = "O" #Jugador1
                    Asig_2 = "X" #Jugador2
                # Salida de la Funcion.
                return Asig_1 , Asig_2

# Decidiendo quien comienza la partida primero
def QuienIniciaPartida(Jugador1, Jugador2, ficha1, ficha2):
    # Inicializacion. Estos hacen el papel de sustitutos si es necesario hacer un cambio.
    CambioJugador = 0
    CambioFicha = 0

    # Inicializando el valor de entrada 
    Escoge = -1

    # Salida
    print ("\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1))
    print ("Jugador2 = %s con la ficha %s" %(Jugador2,ficha2))

    while True:
        try:
            # Entrada
            Escoge = int(input("\nQuieres que ese sea el orden de turnos? Primero %s y luego %s; \
1 (Si), 0 (No): " %(ficha1,ficha2)))
            # Si escoge 1 se toma como True, sino se lee 0 y este es False
            assert(float(Escoge).is_integer())
            assert((Escoge == 1 or Escoge == 0) and Escoge >= 0)
            break
        except:
            print ("\nIntente nuevamente.")
        finally:
        
            if Escoge == 1 or Escoge == 0:
                if Escoge:    
                    pass
                else:
                    # Realizando un intercambio del orden de los jugadores con sus respectivas fichas por decision del usuario.
                    CambioJugador = Jugador1
                    Jugador1 = Jugador2
                    Jugador2 = CambioJugador

                    CambioFicha = ficha1
                    ficha1 = ficha2
                    ficha2 = CambioFicha

                    print ("\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1))
                    print ("Jugador2 = %s con la ficha %s" %(Jugador2,ficha2))
                # Salida de la Funcion.
                return Jugador1, Jugador2, ficha1, ficha2
            else: # este se lee en caso de que la entrada sea un string
                pass


# Funcion que pide de entrada la eleccion de un Tablero; este verifica si la refencia es valida.
def ChooseTablero(Jugador,TablerosDisponible):
    # Inicializando valor de entrada.
    ReferenciaTablero = -1  

    while True:
        try:     
            # Seleccionar tablero a preferencia por el jugador
            ReferenciaTablero = int(input('\n%s, elije el tablero a jugar. Recuerde que puede elergir un tablero entre: %s tablero(s) \
contando el tablero 0: '%(Jugador, TablerosDisponible)))
            assert(float(ReferenciaTablero).is_integer())
            # COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO    
            assert((ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible))     
            break
        
        except:
            print ("\nUsted ha elegido un tablero inexistente en la Dimension.")
            print ("Intente nuevamente.")
        
        finally:
            if (ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible):
                # Salida. Retornando la referencia valida.
                return ReferenciaTablero
            else:
                pass
