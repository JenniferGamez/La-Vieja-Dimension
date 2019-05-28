# #!/usr/bin/env python
#La vieja  cool
#No desistas. Echale.

import random
import string 

Jugador1 = str(raw_input("Ingrese el nombre del Jugador 1: "))
Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2: "))

print "\nJugador1 = %s" %Jugador1
print "Jugador2 = %s" %Jugador2

def QueQuiereSer(Jugador1, Jugador2): #El jugador decide si quiere ser X y O
	while True:
		try: 
			letra = str(raw_input("%s Quiere ser la letra X o la letra O?: " %Jugador1)).upper() 
			# letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan
			assert(letra == "X" or letra == "O")
		except:
			print "Intente nuevamente."
		finally:
			if letra == 'X':
				Asig_1 = "X" #Jugador1
				Asig_2 = "O" #Jugador2
				return Asig_1 , Asig_2
			elif letra == 'O':
				Asig_1 = "O" #Jugador1
				Asig_2 = "X" #Jugador2
				return Asig_1 , Asig_2 #estos me arrojan estas variables que deben volverse locales
			
#Variables locales de la asignacion de X y O

jug1, jug2 = QueQuiereSer(Jugador1,Jugador2)
	
