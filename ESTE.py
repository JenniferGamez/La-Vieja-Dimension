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
			if (letra == "X" or letra == "O"):
				#Asignando las fichas a los jugadores
				if letra == 'X':
					Asig_1 = "X" #Jugador1
					Asig_2 = "O" #Jugador2
					return Asig_1 , Asig_2
				elif letra == 'O':
					Asig_1 = "O" #Jugador1
					Asig_2 = "X" #Jugador2
					return Asig_1 , Asig_2

# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero(fila,columna,tablero,turno,ReferenciaTablero,tamano):
    # Disponibilidad en la dimension
    n = tamano - 1

    # fail; cuenta lo errores obtenidos por Casilla ocupada o inexistente
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


									###PROGRAMA PRINCIPAL###

while True: #DIMENSIONES 
	try:	
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		# Aseguramos que la entrada sea un entero estrictamente .is_integer()
		assert(float(DimensionesTab).is_integer())	
		assert ( DimensionesTab > 0 and DimensionesTab >= 2)
		break 											
	except:
		print "Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2."
		print "Intente nuevamente."
	finally:
		# Se ejecuta si las aserciones se cumplen.
		if DimensionesTab > 0 and DimensionesTab >= 2: 
			print "\nHas elegido un tablero: %s x %s." %(DimensionesTab,DimensionesTab)
			print "Dimensiones a jugar: %s Dimensiones." %DimensionesTab

		while True:	#IDENTIFICACION
			try:	
				#ENTRADA.
				Jugador1 = str(raw_input("\nIngrese el nombre del Jugador 1: ")).upper()
				Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2: ")).upper()

				assert(len(Jugador1) > 0)
				assert(len(Jugador2) > 0)
				break

			except:
				print "\nLa identificacion de los jugadores es esencial."
				print "Por favor ingrese una identificacion valida."

			finally:
				# Se ejecuta si las aserciones se cumplen.
				if len(Jugador1) > 0 and len(Jugador2) > 0:
					# SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
					print "\nJugador1 = %s" %Jugador1
					print "Jugador2 = %s" %Jugador2

					# Asigando valores a variables locales
					ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

					# Monstrando los resultados
					print "\n%s sera las: %s y %s sera: %s." %(Jugador1,ficha_jug1,Jugador2,ficha_jug2)

					# CONSTRUYENDO LOS TABLEROS EN LA DIMENSION SELECCIONADA 
					Sup_Tab = Super_tablero(DimensionesTab)

					while True:# ELIGIENDO TABLERO.
						try: 
							n = DimensionesTab - 1
							refe = input('\nElija el tablero a jugar. Recuerde que puede elergir un tablero \
entre: %s tablero(s) contando el tablero 0: '%n)
							# COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO
							assert(float(refe).is_integer())	
							assert((refe >= 0) and (refe <= n)) 	
							break

						except:
							print "\nUsted ha elegido un tablero inexistente en la Dimension."
							print "Intente nuevamente."

						finally:
							if (refe >= 0) and (refe <= n):
								
								# LLAMADA DEL TABLERO SELECCIONADO
								tab = Sup_Tab[refe]		
								print "\nTablero %s" %refe

								#MOSTRANDO EL TABLERO POR FILAS
								MostrarTablero(tab)

								# Turnos por tablero
								PartidaTablero = DimensionesTab **2

								# Este condicional hace la llamada del procedimiento JugadaTablero y evalua si es necesario seguir rellando el tablero o no
								turno_fail = JugadaTablero(0,0,tab, PartidaTablero,refe,DimensionesTab) 
								if turno_fail > 0 and (not(all([z for z in range(DimensionesTab)] for y in range(DimensionesTab)) == 0)):
								    PartidaTablero = turno_fail
								    JugadaTablero(0,0,tab,PartidaTablero,refe,DimensionesTab)
								else:
								   pass
