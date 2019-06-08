from tkinter import *
from tkinter import messagebox #para enviar mensajes en caja de texto
from tkinter import simpledialog #con esto pedimos datos como los nombres
a = 0
def nuevaventana():
	global a #Se utiliza para poder trabajar con ella en toda la funcion
	a = a+1
	if a==1:  #Crearemosuna ventananueva
		Ventana = Tk()
	   #Creamo la variable Ventana
		Ventana.title("La vieja cool") #como colocarle titulo a la ventana
		Ventana.geometry("500x500") #tamano de la ventana
		Ventana.iconbitmap("Lavieja.ico") #Imagen de la esquina superior izquierda
		Ventana.configure(background="Pink") #configuracion de color. Bockground o bg es el fondo
		Jug1  = str(nombre1.get()).upper()
		Jug2 = str(nombre2.get()).upper()
		Jugador1 = Label(Ventana, text=("Jugador1:", Jug1),bg="white",fg="black").place(x=10, y=30)
		Jugador2 = Label(Ventana, text= ("jugador2:",Jug2),bg="white",fg="black").place(x=10, y=60)


def error():    #Cree esta funcion que verifique si habra error en los datos, aunque habia probbado el del len de los nombres y no los lee.
	NuevaVentana = nuevaventana()

	DimensionesTab = int(nombreDimension.get())
	ElJugador1 = str(nombre1.get())
	ElJugador2 = str(nombre2.get())
	if  DimensionesTab< 2  :
		alerta = messagebox.showwarning("ACEPTAR",""" ¡Intente nuevamente!   
							Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2""") #este es el msj de alerta cuando encuentra error
		return alerta 
	elif DimensionesTab >= 2: 
		NuevaVentana   #nuevaventana me dara la ventana donde se realizara el juego como tal. La hago cuando me levante

	



Ventana = Tk()   #Creamo la variable Ventana
Ventana.title("La vieja cool") #como colocarle titulo a la ventana
Ventana.geometry("400x150") #tamano de la ventana
Ventana.iconbitmap("Lavieja.ico") #Imagen de la ezquina superior izquierda
Ventana.configure(background="dark turquoise")
nombre1 = StringVar()  #Asi se crean las variables
nombre2 = StringVar()
nombreDimension = StringVar() #Las variables string, luego se vuelven int como en el ejemplo de DimensionTab

EtiquetaJugador1 = Label(Ventana, text= "Jugador1:",bg="white",fg="black").place(x=10, y=30) #places es posicion
#Las estiquetas es el nombre pero sin ninguna funcion
nombreCaja1 = Entry(Ventana,textvariable = nombre1).place(x=70,y=30) #ENTRY ES COMO EL INPUT en la vida normal
#el entry te crea una caja de texto donde el usuario coloca sus datos
EtiquetaJugador2 = Label(Ventana, text= "Jugador2:").place(x=200, y=30)
nombreCaja2 = Entry(Ventana, textvariable = nombre2).place(x=260,y=30)
EtiquetaDimension = Label(Ventana, text= "Las dimensiones del tablero:").place(x=10, y=70)
nombreCaja3 = Entry(Ventana, textvariable = nombreDimension).place(x=170,y=70)
	
botonEnvio=Button(Ventana, text = "Continuar",bg="white",fg="black",command=error).pack(side=RIGHT) 
#Este boton toma como comando la funcion error que te permite pasar a la otra ventana, si los datos triunfan 
Ventana.mainloop() #mainloop() siempre se coloca de ultimo para que se mantenga abierta la Ventana


