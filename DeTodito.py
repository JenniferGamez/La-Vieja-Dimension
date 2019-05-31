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
	return dimensiones

# Mostrar Tablero como una Matriz de filas y columnas
def MostrarTablero(tab): # Mostrar elementos sin "" ni los [], y organizado por filas al imprimir
	for fila in tab:
		print fila # Join une los elementos del array


# Jugadores
def QueQuiereSer(Jugador1, Jugador2): #El jugador decide si quiere ser X y O
	while True:
		try: 
			letra = str(raw_input("\n%s, Quieres ser la letra X o la letra O?: " %Jugador1)).upper() 
			# letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan
			assert(letra == "X" or letra == "O")
		except:
			# Esto asegura que la unica entrada sea X y/o Y
			print "Intente nuevamente."
		finally:
			if letra == 'X':
				#Asignando la ficha a jugar en el programa
				Asig_1 = "X" #Jugador1 
				Asig_2 = "O" #Jugador2
				return Asig_1 , Asig_2
			elif letra == 'O':
				#Asignando la ficha a jugar en el programa
				Asig_1 = "O" #Jugador1
				Asig_2 = "X" #Jugador2
				return Asig_1 , Asig_2

#### INICIOOOO
import sys

while True:
	try: 
		DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
		assert (DimensionesTab >= 3)
		assert(float(DimensionesTab).is_integer())		#aseguramos que la entrada sea un entero estrictamente
		break 											#indica que si no se cumple para y pide que sea corregido el erorr
	except:
		print "Las dimesiones del tablero son estrictamente numericas y mayores iguales a 3."
		print "Intente nuevamente."


print "\nHas elegido un tablero %s x %s y profundidad %s." %(DimensionesTab,DimensionesTab,DimensionesTab) 
