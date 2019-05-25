
#La vieja  cool
#No desistas. Echale.

import random
import string 

Jugador1 = str(raw_input("Ingrese el nombre del Jugador 1:"))
Jugador2 = str(raw_input("Ingrese el nombre del Jugador 2:"))

print("Jugador1 =" , Jugador1)
print("Jugador2 =" , Jugador2)

def QueQuiereSer(Jugador1): #El jugador decide si quiere ser X y O
	letra = ''
	if not(letra == 'X' or letra == 'O'): #si la letra no es X y O hara que se siga pidiendo al usuario una X o una O
		print(str(Jugador1) , 'Quiere ser la letra X o la letra O?')
		letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan

		if letra == 'X':
			print (str(Jugador1) ,'sera las X')
			print (str(Jugador2) ,'sera las O')
		else:
			print (str(Jugador1) ,'sera las O')
			print (str(Jugador2) ,'sera las X')

QueQuiereSer(Jugador1)

