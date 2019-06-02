#!/usr/bin/env python

# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero():
    # PartidaTablero; indica la cantidad de casillas a rellenar equivalente a las partidas a jugar
    PartidaTablero = DimensionesTab **2
    # fail; cuenta lo errores obtenidos por Casilla ocupada o inexistente
    fail = 0    

    for i in range(PartidaTablero):
        fila = int(input("\nFila a trabajar (E: %s filas): " %n))
        columna = int(input("Columna a trabajar (E: %s columnas): " %n))

        if Jugada_Valida(fila,columna, tab) == True:
            tab[fila][columna] = "x" ###AQUI FALTA DEFINIR LA FICHA DE DICHO TURNO
            print "\nTablero %s" %refe
            # MOSTRANDO EL TABLERO POR FILAS
            MostrarTablero(tab)

        elif Jugada_Valida(fila,columna, tab) == False:
            fail = fail + 1
            print "\nIntente nuevamente. Casilla ocupada o inexistente."
             
        i = i + 1

    return fail

# Este condicional hace la llamada del procedimiento JugadaTablero y evalua si es necesario seguir rellando el tablero o no.
if JugadaTablero() != 0 and not (all([n for z in range(  DimensionesTab)] for y in range(DimensionesTab))):
    JugadaTablero()
else:
    pass
