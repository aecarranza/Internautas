import time, random
from ingresar_jugadores import obtener_jugadores, leer_archivo, escribir_archivo

#----Constantes----
INDICE_INTENTOS, INDICE_ACIERTOS, INDICE_PROMEDIO, INDICE_INTENTOS_TOTALES, INDICE_ACIERTOS_TOTALES, INDICE_GANO, INDICE_PARTIDAS_GANADAS= 0, 1, 2, 3, 4, 5, 6
INDICE_VALOR_DICCIONARIO = 1

def mostrar_parametro(campo, valor, por_ar_config):
    '''
    Autor: Ezequiel Carranza
    Muestra los parametros de configuracion al principio del juego
    '''
    print(f"{campo}: {valor}. El valor fue dado por {'configuracion' if por_ar_config else 'omision'}.")

def asignar_parametros_configuracion(cantidad_fichas, maximo_jugadores, maximo_partidas, reiniciar_archivo_partidas):
    '''
    Autor: Ezequiel Carranza
    Asigna los valores del archivo de configuracion a las constantes que se usaran en el juego
    '''
    parametros = open("configuracion.csv")
    campo, valor = leer_archivo(parametros, ',')
    while campo:
        por_ar_config = False
        if campo == "CANTIDAD_FICHAS" and int(valor) % 2 == 0:
            cantidad_fichas = int(valor)
            por_ar_config = True
        elif campo == "MAXIMO_JUGADORES" and int(valor) > 0:
            maximo_jugadores = int(valor)
            por_ar_config = True
        elif campo == "MAXIMO_PARTIDAS" and int(valor) > 0:
            maximo_partidas = int(valor)
            por_ar_config = True
        elif campo == "REINICIAR_ARCHIV0_PARTIDAS" and valor:
            reiniciar_archivo_partidas = True if valor == 'True' else False
            por_ar_config = True
        mostrar_parametro(campo, valor, por_ar_config)
        campo, valor = leer_archivo(parametros, ',')
    parametros.close()
    return cantidad_fichas, maximo_jugadores, maximo_partidas, reiniciar_archivo_partidas

def obtener_fichas(cantidad_fichas):
    '''
    Autor: Rocio Donadel, Ezequiel Carranza
    Crea y devuelve un diccionario con las fichas que se usaran en el juego.
    '''
    fichas = {1:'D', 2:'D', 3:'R', 4:'R',
              5:'A', 6:'A', 7:'W', 8:'W',
              9:'X', 10:'X', 11:'Z', 12:'Z',
              13:'Y', 14:'Y', 15:'M', 16:'M'}
    return {ficha: fichas[ficha] for ficha in range(1, cantidad_fichas+1)}

def mezclar_diccionario(diccionario, por_clave=False):
    '''
    Autor: Ezequiel Carranza
    Mezcla los valores de un diccionario y los asigna a las claves. El parametro por_clave indica lo mismo pero con las claves.
    '''
    fichas_mezcladas = {}
    claves = list(diccionario.keys())
    valores = list(diccionario.values())
    if por_clave: random.shuffle(claves)
    else: random.shuffle(valores)
    for i in range(len(claves)):
        fichas_mezcladas[claves[i]] = valores[i]
    return fichas_mezcladas

def voltear_ficha(ficha, posiciones):
    '''
    Autor: Ezequiel Carranza
    Verifica si una ficha fue ingresada por el usuario y valida que esta muestre su valor en el tablero.
    '''
    voltear = False
    if ficha in posiciones: voltear = True
    return voltear

def mostrar_tablero(posiciones, fichas, cantidad_fichas):
    '''
    Autor: Ezequiel Carranza
    Inprime el tablero con todas las fichas en consola.
    '''
    print("Fichas y Posiciones:", end="\n")
    for ficha in fichas:
        if voltear_ficha(ficha, posiciones):
            print(f"[{fichas[ficha]}]", end=" ")
        else:
            print(f"[{ficha}]", end=" ")
        if ficha % 4 == 0 or ficha == cantidad_fichas: print("")

def se_acerto(posiciones, fichas):
    '''
    Autor: Ezequiel Carranza
    Verifica si un par de fichas ingresadas coinciden en su valor.
    '''
    acierto = True
    for i in range(0, len(posiciones), 2):
        if not fichas[posiciones[i]] == fichas[posiciones[i+1]]: acierto = False
    return acierto

def validar_posicion(posicion, posiciones, fichas):
    '''
    Autor: Rocio Donadel
    Valida que el ingreso del usuario sea un valor numérico dentro del rango de fichas utilizadas en el juego.
    '''
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

def pedir_posicion(posiciones, fichas, ):
    '''
    Autor: Rocio Donadel
    Pide al usuario ingresar la primer y segunda posición que quiere descubrir. 
    '''
    posicion = None
    if len(posiciones) % 2 == 0:
        posicion = input("1er posición: ")
    else:
        posicion = input("2da posición: ")
    if validar_posicion(posicion, posiciones, fichas):
        posiciones.append(int(posicion))
    return posiciones

def manejar_posiciones(posiciones, fichas, cantidad_fichas):
    '''
    Autor: Rocio Donadel
    Maneja las fichas en caso de que no haya acierto y modifica la lista posiciones.
    '''
    if len(posiciones) % 2 == 0 and not se_acerto(posiciones, fichas):
        mostrar_tablero(posiciones, fichas, cantidad_fichas)
        print("Las fichas no coinciden")
        del posiciones[-2:]
    return posiciones

def informar_turnos(jugadores):
    '''
    Autor: Ezequiel Carranza
    Informa el orden en el que los jugadores recibiran su turno.
    '''
    turnos = f"\nEl orden de los jugadores: "
    for jugador in jugadores:
        turnos += jugador + ", "
    return turnos[:-2]
 
def informar_ganador(jugadores):
    '''
    Autor: Rocio Donadel
    Informa qué jugador ganó el juego priorizando al con mayor acertadas, en caso de empate se tomarán en cuenta los mínimos intentos.
    '''
    nombres= list(jugadores.keys())
    intentos=[]
    acertadas=[]
    for jugador in jugadores:
        intentos.append(jugadores[jugador][INDICE_INTENTOS])
        acertadas.append(jugadores[jugador][INDICE_ACIERTOS])
    puntos_ganador= max (acertadas)
    posicion= acertadas.index(puntos_ganador)
    if acertadas.count(puntos_ganador) > 1:
        puntos_ganador= min(intentos)
        posicion= intentos.index(puntos_ganador)
    ganador= nombres[posicion]
    return ganador

def terminar_partida(en_partida, posiciones, tiempo_inicial, fichas, cantidad_fichas, jugadores, partidas_jugadas):
    '''
    Se encarga de finalizar el juego e imprimir la pantalla final.
    Autor: Rocio Donadel
    '''
    if len(posiciones) == len(fichas):
        en_partida = False
        mostrar_tablero(posiciones, fichas, cantidad_fichas)
        ganador = informar_ganador(jugadores)
        print(f"¡Felicidades, partida ganada {ganador}! Intentos: {jugadores[ganador][INDICE_INTENTOS]}. Duracion: {informar_duracion(tiempo_inicial, time.time())}")
        posiciones.clear()
        fichas = mezclar_diccionario(fichas)
        partidas_jugadas += 1
    return en_partida, posiciones, partidas_jugadas, fichas

def informar_duracion(tiempo_inicial, tiempo_final):
    '''
    Autor: Ezequiel Carranza
    Recibe un tiempo inicial y uno final en segundos. Devuelve la diferencia en un formato que muestra minutos y segundos
    '''
    duracion = ""
    MIN_EN_SEG = 60
    delta_tiempo = tiempo_final - tiempo_inicial
    resto = 0
    if delta_tiempo / MIN_EN_SEG >= 1:
        duracion += f'{int(delta_tiempo // MIN_EN_SEG)}m'
        resto = delta_tiempo % MIN_EN_SEG
    if resto > 0:
        duracion += f'{int(resto)}s'
    elif delta_tiempo / MIN_EN_SEG < 1:
        duracion += f'{int(delta_tiempo)}s'
    return duracion

def reiniciar_stats(jugadores):
    '''
    Autor: Rocio Donadel
    Reinicia las stats de los jugadores
    '''
    for jugador in jugadores:
        jugadores[jugador][INDICE_INTENTOS] = 0
        jugadores[jugador][INDICE_ACIERTOS] = 0
        jugadores[jugador][INDICE_GANO] = ""
    return jugadores

def guardar_partida(ar_partidas, jugadores):
    '''
    Autor: Ezequiel Carranza
    Guarda la partida en el archivo de partidas
    '''
    tupla_jugadores = sorted(jugadores.items(), key=lambda jugadores: jugadores[INDICE_VALOR_DICCIONARIO][INDICE_ACIERTOS])
    jugadores_ordenado = {clave: valor for clave, valor in tupla_jugadores}
    for jugador in jugadores_ordenado:
        escribir_archivo(ar_partidas, "{},{},{},{},{}".format(time.strftime("%x"), time.strftime("%X"), jugador, jugadores_ordenado[jugador][INDICE_ACIERTOS], jugadores_ordenado[jugador][INDICE_INTENTOS]))

#----Interfaz Ranking----
from tkinter import *

def ranking(jugadores):
    '''
    Autor: Rocio Donadel
    Ordena los jugadores por aciertos en forma descendente
    '''
    devolver = []
    INDICE_ESTRELLA = 6
    INDICE_GANADAS = 7
    ordenado= sorted(jugadores.items(), key= lambda jugadores: jugadores[INDICE_VALOR_DICCIONARIO][INDICE_ACIERTOS], reverse=True)
    ordenado_dicc= {clave: valor for clave,valor in ordenado}
    for jugador in ordenado_dicc:
        if not ordenado_dicc[jugador][INDICE_INTENTOS_TOTALES] == 0:
            ordenado_dicc[jugador][INDICE_PROMEDIO]= int((ordenado_dicc[jugador][INDICE_ACIERTOS_TOTALES]*100)/ordenado_dicc[jugador][INDICE_INTENTOS_TOTALES])
        devolver += [jugador,ordenado_dicc[jugador][INDICE_INTENTOS], ordenado_dicc[jugador][INDICE_ACIERTOS], ordenado_dicc[jugador][INDICE_PROMEDIO], 
                    ordenado_dicc[jugador][INDICE_INTENTOS_TOTALES], ordenado_dicc[jugador][INDICE_ACIERTOS_TOTALES], ordenado_dicc[jugador][INDICE_GANO], 
                    ordenado_dicc[jugador][INDICE_PARTIDAS_GANADAS]]
    jugador = devolver[0]
    jugadores[jugador][INDICE_PARTIDAS_GANADAS] += 1
    devolver[INDICE_GANADAS] += 1
    devolver[INDICE_ESTRELLA] = ("★" * (int(jugadores[jugador][INDICE_PARTIDAS_GANADAS]))) 
    return devolver

def ranking_interfaz(en_ejecucion, en_partida, partidas_jugadas, maximo_partidas, pjugadores):
    '''
    Autor: Rocio Donadel
    Inicia la interfaz del ranking de los jugadores en las partidas
    '''
    l_ejecucion, l_partida = [en_ejecucion], [en_partida]
    nombres=[]
    jugadores= ranking(pjugadores)
    y_rank, y_nombre, y_numero, x_numero= 30, 30, 30, 80
    COLOR_VENTANA, COLOR_FRAME, COLOR_FUENTE = "#574236", "#C3581B", "white"
    #ventana
    ventana=Tk()
    ventana.title("Ranking Memotest")
    ventana.geometry("600x320")
    ventana.resizable(0,0)
    ventana.iconbitmap("memotest.ico")
    ventana.config(bg=COLOR_VENTANA)
    #frame
    miframe=Frame(ventana,width=550,height=250)
    miframe.config(bg=COLOR_FRAME)
    miframe.pack()
    miframe.place(x=25,y=30)
    #
    mensaje=Label(miframe,text="""Jugadores    Aciertos   Intentos   Promedio A   Total I   Total A""",fg=COLOR_FUENTE)
    mensaje.config(bg=COLOR_FRAME)
    mensaje.place(x= 0, y= 0)
    #
    ganador=Label(miframe,text="GANADOR:",fg=COLOR_FUENTE)
    ganador.config(bg=COLOR_FRAME)
    ganador.place(x=450, y= 0)
    for dato in jugadores:
        dato=str(dato)
        if dato.isalpha():
            nombres.append(dato)
    for i in range(1,len(nombres)+1):
        jugador=Label(miframe,text=i,fg=COLOR_FUENTE)
        jugador.config(bg=COLOR_FRAME)
        jugador.place(x=0, y= y_rank)
        y_rank+= 20
        #x_frame= +50
    for i in range(0,len(jugadores),8):
        x_numero= 60
        jugadores[i]= str(jugadores[i])
        ganador=Label(miframe,text="GANADOR:",fg=COLOR_FUENTE)
        ganador.config(bg=COLOR_FRAME)
        ganador.place(x=450, y= 0)
        ganador_nombre=Label(miframe,text=jugadores[0],fg=COLOR_FUENTE)
        ganador_nombre.config(bg=COLOR_FRAME)
        ganador_nombre.place(x=460, y= 20)
        x_numero= 85
        jugadores[i]= str(jugadores[i])
        rank=Label(miframe,text=jugadores[i],fg=COLOR_FUENTE)
        rank.config(bg=COLOR_FRAME)
        rank.place(x=20, y= y_nombre)
        y_nombre+= 20
        aciertos=Label(miframe,text=jugadores[i+2],fg=COLOR_FUENTE)
        aciertos.config(bg=COLOR_FRAME)
        aciertos.place(x= x_numero , y= y_numero)
        x_numero+= 50
        intentos=Label(miframe,text=jugadores[i+1],fg=COLOR_FUENTE)
        intentos.config(bg=COLOR_FRAME)
        intentos.place(x= x_numero , y= y_numero)
        x_numero+= 55
        promedio_intentos=Label(miframe,text=jugadores[i+3],fg=COLOR_FUENTE)
        promedio_intentos.config(bg=COLOR_FRAME)
        promedio_intentos.place(x= x_numero , y= y_numero)
        x_numero+= 60
        intentos_totales=Label(miframe,text=jugadores[i+4],fg=COLOR_FUENTE)
        intentos_totales.config(bg=COLOR_FRAME)
        intentos_totales.place(x= x_numero , y= y_numero)
        x_numero+=45
        aciertos_totales=Label(miframe,text=jugadores[i+5],fg=COLOR_FUENTE)
        aciertos_totales.config(bg=COLOR_FRAME)
        aciertos_totales.place(x= x_numero , y= y_numero)
        x_numero+=40
        estrella=Label(miframe,text=jugadores[i+6],fg=COLOR_FUENTE)
        estrella.config(bg=COLOR_FRAME)
        estrella.place(x= x_numero , y= y_numero)
        y_numero+= 20
    #botones
    boton_jugar = Button(ventana, text="Jugar otra vez", command=lambda:[l_partida.clear(), l_partida.append(True), ventana.destroy()])
    boton_jugar.pack()
    boton_jugar.place(x=460,y=80)
    if partidas_jugadas == maximo_partidas: 
        boton_jugar.pack_forget()
        boton_jugar.place_forget()
    #
    boton_terminar = Button(ventana, text="Terminar Juego", command=lambda:[l_ejecucion.clear(), l_ejecucion.append(False), ventana.destroy()])
    boton_terminar.pack()
    boton_terminar.place(x=465,y=110)
    ventana.mainloop()
    return l_ejecucion[0], l_partida[0]
#----Fin Interfaz Grafica----


#----FUNCION MAIN----

def ejecutar_memotest():
    '''
    Autor: Rocio Donadel, Ezequiel Carranza
    Funcion que dirige la ejecucion del programa.
    '''
    #----Parametros de configuracion----
    CANTIDAD_FICHAS, MAXIMO_JUGADORES, MAXIMO_PARTIDAS, REINICIAR_ARCHIV0_PARTIDAS = 16, 2, 3, False
    #-----------------------------------
    en_ejecucion, en_partida = True, True
    CANTIDAD_FICHAS, MAXIMO_JUGADORES, MAXIMO_PARTIDAS, REINICIAR_ARCHIV0_PARTIDAS = asignar_parametros_configuracion(CANTIDAD_FICHAS, MAXIMO_JUGADORES, MAXIMO_PARTIDAS, REINICIAR_ARCHIV0_PARTIDAS)
    fichas = mezclar_diccionario(obtener_fichas(CANTIDAD_FICHAS))
    jugadores = mezclar_diccionario(obtener_jugadores(MAXIMO_JUGADORES), True)
    posiciones = []
    partidas_jugadas = 0
    if REINICIAR_ARCHIV0_PARTIDAS: archivo_partidas = open("partidas.csv", "w")
    else: archivo_partidas = open("partidas.csv", "a")
    while en_ejecucion == True:
        print(informar_turnos(jugadores))
        t_inicial = time.time()
        while en_partida and partidas_jugadas <= MAXIMO_PARTIDAS:
            for jugador in jugadores:
                terminar_turno = False
                if en_partida: print(f"Turno de: {jugador}")
                while en_partida and not terminar_turno:
                    mostrar_tablero(posiciones, fichas, CANTIDAD_FICHAS)
                    posiciones = pedir_posicion(posiciones, fichas)
                    if len(posiciones) % 2 == 0:
                        if se_acerto(posiciones, fichas):
                            jugadores[jugador][INDICE_ACIERTOS] += 1
                            jugadores[jugador][INDICE_ACIERTOS_TOTALES] += 1
                        else: terminar_turno = True
                    posiciones = manejar_posiciones(posiciones, fichas, CANTIDAD_FICHAS)
                    if len(posiciones) % 2 == 0:
                        jugadores[jugador][INDICE_INTENTOS] += 1
                        jugadores[jugador][INDICE_INTENTOS_TOTALES] += 1
                    en_partida, posiciones, partidas_jugadas, fichas = terminar_partida(en_partida, posiciones, t_inicial, fichas, CANTIDAD_FICHAS, jugadores, partidas_jugadas)
        en_ejecucion, en_partida = ranking_interfaz(en_ejecucion, en_partida, partidas_jugadas, MAXIMO_PARTIDAS, jugadores)
        guardar_partida(archivo_partidas, jugadores)
        jugadores = reiniciar_stats(jugadores)
        jugadores = mezclar_diccionario(jugadores, True)
    archivo_partidas.close()
    
ejecutar_memotest()