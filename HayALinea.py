def HayAlinea(Tablero, Tamano,Fila,Columna, Ficha):
  def HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha):
    # Valor booleano
    HaylineaHorizontal = 0
    # Tablero
    tab = Tablero[Fila]

    if all(tab[i] == Ficha for i in range(Tamano) if Tablero[i] != 0 ):
      HaylineaHorizontal = 1
    elif all(tab[i] != Ficha for i in range(Tamano) if Tablero[i] != 0 ):
      pass
    else:
      pass
    # Retornando la existencia de Linea Horizontal
    return HaylineaHorizontal

  def HayAlineaVertical(Tablero,Columna,Tamano, Ficha):
    # Valor booleano
    HaylineaVertical = 0
    # Inicializando contador
    cont_vertical = 0

    for i in range(Tamano):
      if Tablero[i][Columna] == Ficha and Tablero[i][Columna] != 0: 
        cont_vertical = cont_vertical + 1
      elif Tablero[i][Columna] != Ficha or Tablero[i][Columna] != 0:
        pass
      elif Tablero[i][Columna] == 0:
        pass

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

    for i in range(0,Tamano):
      for j in range (0,Tamano):  
        if Tablero[i][j] == Ficha and i == j: 
          cont_diagonal = cont_diagonal + 1
        else: 
          pass

    if cont_diagonal == Tamano:
      HayAlineaDiagonal = 1
    elif cont_diagonal != Tamano:
      pass
    # Retornando la existencia de Linea Diagonal
    return HayAlineaDiagonal

  ###LLAMADA DE LAS FUNCIONES INTERNAS###
  # Llamada si hay Linea Horizontal
  return HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha)
  # Llamada si hay Linea Horizontal
  return HayAlineaVertical(Tablero,Fila,Tamano,Ficha)
  # Llamada si hay Linea Diagonal
  return HayAlineaDiagonal(Tablero,Tamano,Ficha)


#tablero de pruebas
Tablero1 = \
[["X",0,"X"],\
[0,"X",0],\
["X","X","X"]]

Tablero2 = \
[[0,0,0],\
[0,0,0],\
[0,0,0]]

Tablero3 = \
[["X","X","X"],\
["X","X","X"],\
["X","X","X"]]

# dimension de referencia
tam = 3 


Ficha = "X"
Fila = 0
Columna = 0


HaylineaVertical = 0
Tamano = 3

print HayAlinea(Tablero1,tam, 0, 0,Ficha)
print HayAlinea(Tablero3,tam,1,1,Ficha) 
print HayAlinea(Tablero1,0,0,Tamano,Ficha)
