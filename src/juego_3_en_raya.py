fichas = ['o', 'x']

def generar_tablero(n, movimientos_jugadores):
    tablero = []
    for i in range(n):
        fila = ['_' for _ in range(n)]
        for k in range(len(movimientos_jugadores)):
            movimientos_jugador = movimientos_jugadores[k]
            if i in movimientos_jugador:
                for j in movimientos_jugador[i]:
                    fila[j] = fichas[k]
        tablero.append(fila)
    return tablero


import pytest

def test_generar_tablero():
    mov_jugador_1 = {}
    mov_jugador_2 = {}
    movimientos_jugadores = [mov_jugador_1, mov_jugador_2]
    n = 3

    t = generar_tablero(n, movimientos_jugadores)

    assert len(t) == n
    for fila in t:
        assert len(fila) == n

def movimiento_valido(x, y, movimientos_otro_jugador, n):
    if x >= n or y >= n:
        return False
    if x in movimientos_otro_jugador:
        if y in movimientos_otro_jugador[x]:
            return False
    return True


def test_movimiento_columna_fuera_tablero():
    movimientos_otro_jugador = {}
    n = 3
    x = 1
    y = n
    assert False == movimiento_valido(x, y, movimientos_otro_jugador, n)


def test_movimiento_fila_y_columna_fuera_tablero():
    movimientos_otro_jugador = {}
    n = 3
    x = n
    y = n
    assert False == movimiento_valido(x, y, movimientos_otro_jugador, n)


def test_movimiento_incorrecto():
    movimientos_otro_jugador = {2: [3]}
    n = 4
    x = 2
    y = 3
    assert False == movimiento_valido(x, y, movimientos_otro_jugador, n)


def jugada_ganadora(movimientos_jugador):
    """
    Método que permite determinar si los movimientos de un jugador le
    permite ganar una partida.
    Parámetros:
    * movimientos_jugador: dict con el conjunto de movimientos de un
      jugador
    """
    # Comprobamos si hay 3 fichas en una fila
    for fila in movimientos_jugador:
        movimientos_columna = movimientos_jugador[fila]
        if len(movimientos_columna) == 3:
            return True
    return False


def test_no_ganador():
    movimientos_jugador={2:[2,3]}
    assert False == jugada_ganadora(movimientos_jugador)

def test_ganador():
    movimientos_jugador={2:[1,2,3]}
    assert True == jugada_ganadora(movimientos_jugador)

def mostrar_tablero(tablero):
    """
    Método que muestra el estado actual del tablero

    Parámetros:
    * tablero: dict con el tablero a mostrar
    """
    for fila in tablero:
        for celda in fila:
            print(celda,end='')
        print('\n')

import os

if __name__ == "__main__":

    n = int(input("Introduce el tamaño del tablero cuadrado: "))
    casillas_libres = n * n
    jugador_activo = 0

    movimientos_jugador_1 = {}
    movimientos_jugador_2 = {}
    movimientos_jugadores = [movimientos_jugador_1, movimientos_jugador_2]

    tablero = generar_tablero(n, movimientos_jugadores)
    mostrar_tablero(tablero)

    while casillas_libres > 0:
        casilla_jugador = input(
            f"JUGADOR {jugador_activo+1}: Introduce movimiento (x,y): "
        ).strip()

        x = int(casilla_jugador.split(',')[0]) - 1
        y = int(casilla_jugador.split(',')[1]) - 1

        movimientos_jugador_activo = movimientos_jugadores[jugador_activo]
        movimientos_otro_jugador = movimientos_jugadores[(jugador_activo + 1) % 2]

        if movimiento_valido(x, y, movimientos_otro_jugador, n):
            mov_col = movimientos_jugador_activo.get(x, [])
            mov_col.append(y)
            movimientos_jugador_activo[x] = mov_col

            os.system('cls')
            tablero = generar_tablero(n, movimientos_jugadores)
            mostrar_tablero(tablero)

            if jugada_ganadora(movimientos_jugador_activo):
                print(f"ENHORABUENA EL JUGADOR {jugador_activo+1} HA GANADO")
                break

        else:
            print("Movimiento inválido")

        casillas_libres -= 1
        jugador_activo = (jugador_activo + 1) % 2





