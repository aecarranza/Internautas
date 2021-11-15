from tkinter import *

def iniciar_ventana():
    X_LABEL, X_ENTRYBOX, Y_USUARIO = 12, 80, 11
    COLOR_VENTANA, COLOR_FRAME, COLOR_FUENTE = "#574236", "#C3581B", "white"
    jugadores = []
    #ventana
    ventana=Tk()
    ventana.title("Ingreso Memotest")
    ventana.geometry("300x130")
    ventana.resizable(0,0)
    ventana.iconbitmap("memotest.ico")
    ventana.config(bg=COLOR_VENTANA)
    #frame
    miframe=Frame(ventana,width=240,height=70)
    miframe.config(bg=COLOR_FRAME)
    miframe.pack()
    miframe.place(x=30,y=30)
    #entrada de datos
    jugador1=Label(miframe,text="Jugador",fg=COLOR_FUENTE)
    jugador1.config(bg=COLOR_FRAME)
    jugador1.place(x=X_LABEL, y=Y_USUARIO)
    #
    entrada_jugador= StringVar()
    texto_jugador=Entry(miframe,textvariable=entrada_jugador)
    texto_jugador.place(x=X_ENTRYBOX,y=Y_USUARIO)
    #botones
    boton_entrada = Button(miframe, text="Ingresar jugador", command=lambda:[jugadores.append(entrada_jugador.get()), texto_jugador.delete(0, END)])
    boton_entrada.pack()
    boton_entrada.place(x=60,y=40)
    #
    boton=Button(ventana, text="Empezar a jugar", command=ventana.destroy)
    boton.pack()
    boton.place(x=110,y=101.5)
    #
    ventana.mainloop()
    return jugadores

def obtener_jugadores():
    diccionario={}
    registro_jugadores = iniciar_ventana()
    for jugador in registro_jugadores:
        if not jugador == '': diccionario[jugador] = 0
    return diccionario

'''
def main():
    entrada_jugadores = iniciar_ventana()
    print(registro_jugadores(entrada_jugadores))

main()
'''