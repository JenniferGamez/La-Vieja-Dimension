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
    for i in range(0,Tamano):
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
  # Llamada si hay Linea Horizontal
  return HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha), HayAlineaVertical(Tablero,Fila,Tamano,Ficha),\
HayAlineaDiagonal(Tablero,Tamano,Ficha), HayAlineaTableros(SuperTablero,Fila,Columna,Tamano, Ficha)
  

SuperTablero = [\
\
[["X",0,"X"],\
[0,"X",0],\
["X","X","X"]]
,\
[[0,0,0],\
[0,"X",0],\
[0,0,0]]
,\
[["X","X","X"],\
["X","X","X"],\
["X","X","X"]]\
,]

Ficha = "X"
Fila = 1
Columna = 2
Tamano = 3

#tablero de pruebas
Tablero1 = \
[["X",0,"X"],\
[0,"X",0],\
["X","X","X"]]

Tablero2 = \
[[0,0,0],\
[0,"X",0],\
[0,0,0]]

Tablero3 = \
[["X","X","X"],\
["X","X","X"],\
["X","X","X"]]

LineaHorizontal, LineaVertical,LineaDiag,LineaTableros = HayAlinea(SuperTablero,Tablero1,Tamano, Fila, Columna,Ficha)

# Orden de Salida   
print LineaHorizontal

print LineaVertical

print LineaDiag

print LineaTableros 

