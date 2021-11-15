'''
1. Mostrar el tablero
2. Pedir la primer posicion a descubrir
3. Dar vuelta la ficha de la posicion ingresada
4. Pedir la segunda posicion a descubrir
5. Dar vuelta la ficha de la posicion ingresada
6. Validar si las fichas tienen el mismo valor
	Si las fichas son iguales desaparecen del tablero
	Si son distintas que empiece el juego de nuevo
'''

import time, random
from ingreso_jugadores import obtener_jugadores

def obtener_fichas():
    fichas = {1:'D', 2:'D', 3:'S', 4:'S',
              5:'A', 6:'A', 7:'W', 8:'W',
              9:'X', 10:'X', 11:'Z', 12:'Z',
              13:'Y', 14:'Y', 15:'M', 16:'M'}
    return fichas

def mezclar_fichas(fichas):
    fichas_mezcladas = {}
    keys = list(fichas.keys())
    values = list(fichas.values())
    random.shuffle(values)
    for i in range(len(keys)):
        fichas_mezcladas[keys[i]] = values[i]
    return fichas_mezcladas

def voltear_ficha(ficha, posiciones):
    ficha_ingresada = False
    if ficha in posiciones: ficha_ingresada = True
    return ficha_ingresada

def mostrar_tablero(posiciones, fichas):
    print("Fichas y Posiciones:", end="\n")
    for ficha in fichas:
        if voltear_ficha(ficha, posiciones):
            print(f"[{fichas[ficha]}]", end=" ")
        else:
            print(f"[{ficha}]", end=" ")
        if ficha % 4 == 0: print("")

def validar_acierto(posiciones, fichas):
    if len(posiciones) % 2 == 0:
        for i in range(0, len(posiciones), 2):
            if not fichas[posiciones[i]] == fichas[posiciones[i+1]]:
                mostrar_tablero(posiciones, fichas)
                print("Las fichas no coinciden")
                posiciones.clear()
    return posiciones

def validar_posicion(posicion, posiciones, fichas):
    posicion_valida = False
    if not posicion.isdigit():
        print("Debe ingresar un caracter numerico")
    elif not int(posicion) in fichas.keys():
        print("Debe ingresar una posicion existente")
    elif int(posicion) in posiciones:
        print("Debe ingresar una posicion que no este descubierta")
    else:
        posicion_valida = True
    return posicion_valida

def pedir_posicion(posiciones, fichas):
    posicion = None
    if len(posiciones) % 2 == 0:
        posicion = input("1er posición: ")
    else:
        posicion = input("2da posición: ")
    if validar_posicion(posicion, posiciones, fichas):
        posiciones.append(int(posicion))
        posiciones = validar_acierto(posiciones, fichas)
    return posiciones

def terminar_juego(en_ejecucion, posiciones, intentos, tiempo_inicial, fichas):
    if len(posiciones) == len(fichas):
        en_ejecucion = False
        mostrar_tablero(posiciones, fichas)
        print(f"¡Felicidades, ganaste! Intentos: {intentos}. Duracion: {round(time.time() - tiempo_inicial, 1)}s")
    return en_ejecucion

#----FUNCION MAIN----
def ejecutar_memotest():
    en_ejecucion = True
    t_inicial = time.time()
    posiciones = []
    fichas = mezclar_fichas(obtener_fichas())
    jugadores = obtener_jugadores()
    print(jugadores)
    intentos = 0
    while en_ejecucion:
        intentos += 1
        mostrar_tablero(posiciones, fichas)
        posiciones = pedir_posicion(posiciones, fichas)
        en_ejecucion = terminar_juego(en_ejecucion, posiciones, intentos, t_inicial, fichas)

ejecutar_memotest()