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




