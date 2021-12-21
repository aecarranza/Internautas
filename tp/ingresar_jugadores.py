from tkinter import *


def leer_archivo(archivo, devolver):
    '''
    Autor: Ezequiel Carranza
    Lee un archivo y devuelve sus campos
    '''
    linea = archivo.readline()
    if linea:
        retorna = linea.rstrip('\n').split(',')
    else:
        retorna = devolver.split(',')
    return retorna

def escribir_archivo(archivo, linea_a_escribir):
    '''
    Autor: Ezequiel Carranza
    Escribe un archivo csv
    '''
    archivo.write(linea_a_escribir + '\n')

#----INICIO DE SESION----
def validar_ingreso(pusuario, pclave):
    '''
    Autor: Ezequiel Carranza
    Valida que exista el login iniciado
    '''
    ingreso_valido = False
    usuarios = open("usuarios.csv")
    usuario, clave = leer_archivo(usuarios, ',')
    while usuario and not ingreso_valido:
        if usuario == pusuario and clave == pclave: ingreso_valido = True
        usuario, clave = leer_archivo(usuarios, ',')
    usuarios.close()
    return ingreso_valido

def popup_login_incorrecto(vent_iniciar_sesion):
    '''
    Autor: Rocio Donadel
    Avisa en una nueva ventana cuando el login es incorrecto
    '''
    login_incorrecto = Toplevel(vent_iniciar_sesion)
    login_incorrecto.title("Login: Incorrecto")
    login_incorrecto.geometry("300x50")
    login_incorrecto.resizable(0,0)
    login_incorrecto.iconbitmap("memotest.ico")
    login_incorrecto.config(bg="black")
    incorrecto = Label(login_incorrecto,text="""Ingreso incorrecto, verifique que el usuario esté
registrado o la contraseña sea correcta""")
    incorrecto.place(x=20, y=5)

def ingresar_jugador_ventana(vent_iniciar_sesion, jugadores):
    '''
    Autor: Ezequiel Carranza
    Escribe los jugadores logueados en la interfaz de inicio de sesion
    '''
    for i in range(len(jugadores)):
        jugador = Label(vent_iniciar_sesion,text=jugadores[i])
        jugador.place(x=275,y=35+i*20)

def manejar_jugadores(vent_iniciar_sesion, boton_iniciar_sesion, jugadores, maximo_jugadores):
    '''
    Autor: Rocio Donadel
    Avisa el ingreso maximo de jugadores e inicia la partida
    '''
    ingresar_jugador_ventana(vent_iniciar_sesion, jugadores)
    if len(jugadores) >= maximo_jugadores:
        max_jugadores = Toplevel(vent_iniciar_sesion)
        max_jugadores.title("Aviso")
        max_jugadores.geometry("300x85")
        max_jugadores.resizable(0,0)
        max_jugadores.iconbitmap("memotest.ico")
        max_jugadores.config(bg="black")
        #label
        label_max_jugadores = Label(max_jugadores,text="""Se ha ingresado el maximo de jugadores. 
Se inicia la partida.""")
        label_max_jugadores.place(x=20, y=5)
        #boton iniciar partida
        boton_empezar = Button(max_jugadores, text="Empezar a jugar", command=vent_iniciar_sesion.destroy)
        boton_empezar.pack()
        boton_empezar.place(x=90,y=50)

def iniciar_ventana(maximo_jugadores):
    '''
    Autor: Rocio Donadel, Ezequiel Carranza
    Inicia la interfaz grafica que permite ingresar los juagdores que participaran del juego.
    '''
    X_LABEL, X_ENTRYBOX, Y_USUARIO = 12, 68, 11
    COLOR_VENTANA, COLOR_FRAME, COLOR_FUENTE = "#574236", "#C3581B", "white"
    jugadores = []
    #ventana
    ventana=Tk()
    ventana.title("Ingreso Memotest")
    ventana.geometry("400x200")
    ventana.resizable(0,0)
    ventana.iconbitmap("memotest.ico")
    ventana.config(bg=COLOR_VENTANA)
    #frame
    miframe=Frame(ventana,width=230,height=140)
    miframe.config(bg=COLOR_FRAME)
    miframe.pack()
    miframe.place(x=30,y=30)
    #
    miframe2=Frame(ventana,width=120,height=140)
    miframe2.config(bg="white")
    miframe2.pack()
    miframe2.place(x=270,y=30)
    #
    ingresados=Label(ventana,text="Ingresados",fg=COLOR_FUENTE)
    ingresados.config(bg=COLOR_FRAME)
    ingresados.place(x=300, y=5)
    #entrada de datos
    jugador=Label(miframe,text="Jugador",fg=COLOR_FUENTE)
    jugador.config(bg=COLOR_FRAME)
    jugador.place(x=X_LABEL, y=Y_USUARIO)
    #
    clave=Label(miframe,text="Clave",fg=COLOR_FUENTE)
    clave.config(bg=COLOR_FRAME)
    clave.place(x=X_LABEL, y=50)
    #requisitos
    entrada_jugador = StringVar()
    texto_jugador = Entry(miframe, textvariable=entrada_jugador)
    texto_jugador.place(x=X_ENTRYBOX,y=Y_USUARIO)
    #
    entrada_clave = StringVar()
    texto_clave = Entry(miframe, textvariable=entrada_clave)
    texto_clave.config(show="*")
    texto_clave.place(x=X_ENTRYBOX,y=50)
    #botones
    boton_entrada = Button(miframe, text="Iniciar sesion", command=lambda:[
                                                                            jugadores.append(entrada_jugador.get()) if validar_ingreso(texto_jugador.get(), texto_clave.get()) else popup_login_incorrecto(ventana),
                                                                            texto_jugador.delete(0, END), 
                                                                            texto_clave.delete(0, END),
                                                                            manejar_jugadores(ventana, boton_entrada, jugadores, maximo_jugadores),
                                                                            ])
    boton_entrada.pack()
    boton_entrada.place(x=X_LABEL,y=85)
    #
    boton_registrar=Button(miframe, text="Registrar jugador", command=lambda: registro(ventana))
    boton_registrar.pack()
    boton_registrar.place(x=115,y=85)
    #
    boton_empezar=Button(ventana, text="Empezar a jugar", command=ventana.destroy)
    boton_empezar.pack()
    boton_empezar.place(x=90,y=145)
    #
    ventana.mainloop()
    return jugadores

#----FIN INICIO DE SESION----


#----REGISTRO DE USUARIOS----
def registrar(vent_iniciar_sesion, pusuario, pclave, pconfirmacion):
    '''
    Autor: Ezequiel Carranza
    Registra el usuario
    '''
    se_registro = False
    usuarios = open("usuarios.csv", "r+")
    if not usuario_registrado(usuarios, pusuario):
        if pusuario and len(pclave) > 0 and pclave == pconfirmacion and validar_registro(usuarios, pusuario, pclave): se_registro = True
        if not se_registro: popup_registro_incorrecto(vent_iniciar_sesion)
    else:
        popup_usuario_registrado(vent_iniciar_sesion)
    usuarios.close()

def usuario_registrado(ar_usuarios, pusuario):
    '''
    Autor: Ezequiel Carranza
    Verifica que el usuario no se haya registrado anteriormente
    '''
    registrado = False
    usuario, clave = leer_archivo(ar_usuarios, ',')
    while usuario and not registrado:
        if usuario == pusuario: registrado = True
        usuario, clave = leer_archivo(ar_usuarios, ',')
    return registrado

def validar_registro(ar_usuarios, usuario, clave):
    '''
    Autor: Rocio Donadel
    Valida que el registro cumpla con los requisitos
    '''
    registro_valido = False
    if validar_usuario(usuario) and validar_clave(clave): 
        escribir_archivo(ar_usuarios, "{},{}".format(usuario, clave))
        registro_valido = True
    return registro_valido

def validar_usuario(usuario):
    '''
    Autor: Rocio Donadel
    Valida que el usuario ingresado cumpla con los requisitos
    '''
    usuario_valido = False
    if len(usuario) >= 4 and len(usuario) <= 15:
        usuario_valido = True
        for letra in usuario:
            if not letra.isalnum() and not letra == '_': usuario_valido = False
    return usuario_valido

def validar_clave(clave):
    '''
    Autor: Rocio Donadel
    Valida que la contrasena ingresada cumpla con los requisitos
    '''
    clave_valida = False
    mayuscula, minuscula, numero, guion = 0, 0, 0, 0
    caracter_especial = False
    CARACTERES_GUION, CARACTERES_TILDE = "_-", "áéíóúÁÉÍÓÚ"
    i=0
    if len(clave) >= 8 and len(clave) <= 12:
        while i < len(clave) and not caracter_especial:
            if clave[i].isupper():
                mayuscula += 1
            elif clave[i].islower():
                minuscula += 1
            elif clave[i].isdigit():
                numero += 1
            elif clave[i] in CARACTERES_GUION:
                guion += 1
            elif clave[i] not in CARACTERES_TILDE:
                caracter_especial = True
            i+=1
        if not caracter_especial and mayuscula > 0 and minuscula > 0 and numero > 0 and guion > 0: clave_valida = True
    return clave_valida

def popup_registro_incorrecto(vent_iniciar_sesion):
    '''
    Autor: Rocio Donadel
    Avisa cuando se produce un error durante el registro
    '''
    registro_incorrecto = Toplevel(vent_iniciar_sesion)
    registro_incorrecto.title("Registro: Incorrecto")
    registro_incorrecto.geometry("300x50")
    registro_incorrecto.resizable(0,0)
    registro_incorrecto.iconbitmap("memotest.ico")
    registro_incorrecto.config(bg="black")
    incorrecto=Label(registro_incorrecto,text="""Registro incorrecto, verifique que ambas contraseñas
coincidan y que sus datos cumplan con los requisitos""")
    incorrecto.place(x=10, y=5)

def popup_usuario_registrado(vent_iniciar_sesion):
    '''
    Autor: Ezequiel Carranza
    Avisa cuando se quiere registrar a un jugador que ya lo esta
    '''
    registro_incorrecto = Toplevel(vent_iniciar_sesion)
    registro_incorrecto.title("Registro: Incorrecto")
    registro_incorrecto.geometry("300x50")
    registro_incorrecto.resizable(0,0)
    registro_incorrecto.iconbitmap("memotest.ico")
    registro_incorrecto.config(bg="black")
    incorrecto=Label(registro_incorrecto,text="El usuario ya se encuentra registrado.")
    incorrecto.place(x=10, y=5)

def registro(vent_iniciar_sesion):
    '''
    Autor: Rocio Donadel
    Inicia la ventana de registro de jugadores
    '''
    X_LABEL, X_ENTRYBOX, Y_USUARIO = 12, 108, 11
    COLOR_VENTANA, COLOR_FRAME, COLOR_FUENTE = "#574236", "#C3581B", "white"
    #ventana
    ventana_registro = Toplevel(vent_iniciar_sesion)
    ventana_registro.title("Registro Memotest")
    ventana_registro.geometry("450x150")
    ventana_registro.resizable(0,0)
    ventana_registro.iconbitmap("memotest.ico")
    ventana_registro.config(bg=COLOR_VENTANA)
    #frame
    miframe=Frame(ventana_registro,width=240,height=105)
    miframe.config(bg=COLOR_FRAME)
    miframe.pack()
    miframe.place(x=30,y=10)
    #
    requisitos=Label(ventana_registro,text="""El usuario debe contener entre
4 y 15 dígitos y estar formado
solo por letras, números y guión
bajo. La contraseña debe tener
entre 8 y 12 dígitos, una
mayúscula, una minúcula, un
número y alguno de los
siguientes caracteres: '_', '-'""",fg=COLOR_FUENTE)
    requisitos.config(bg=COLOR_FRAME)
    requisitos.place(x=272, y=Y_USUARIO)
    #entrada de datos
    jugador = Label(miframe,text="Nombre usuario",fg=COLOR_FUENTE)
    jugador.config(bg=COLOR_FRAME)
    jugador.place(x=X_LABEL, y=Y_USUARIO)
    #
    clave = Label(miframe,text="Clave",fg=COLOR_FUENTE)
    clave.config(bg=COLOR_FRAME)
    clave.place(x=X_LABEL, y=36)
    #
    confirmar_clave = Label(miframe,text="Confirmar Clave",fg=COLOR_FUENTE)
    confirmar_clave.config(bg=COLOR_FRAME)
    confirmar_clave.place(x=X_LABEL, y=62)
    #
    entrada_usuario = StringVar()
    texto_jugador = Entry(miframe,textvariable=entrada_usuario)
    texto_jugador.place(x=X_ENTRYBOX,y=Y_USUARIO)
    #
    entrada_clave = StringVar()
    texto_clave = Entry(miframe,textvariable=entrada_clave)
    texto_clave.config(show="*")
    texto_clave.place(x=X_ENTRYBOX,y=36)
    #
    entrada_confirmar_clave = StringVar()
    texto_confirmar_clave = Entry(miframe,textvariable=entrada_confirmar_clave)
    texto_confirmar_clave.config(show="*")
    texto_confirmar_clave.place(x=X_ENTRYBOX,y=62)
    #botones
    boton_registro = Button(ventana_registro, text="Registrar jugador", command=lambda:[
                                                                                        registrar(vent_iniciar_sesion, texto_jugador.get(), texto_clave.get(), texto_confirmar_clave.get()),
                                                                                        texto_jugador.delete(0, END), 
                                                                                        texto_clave.delete(0, END),
                                                                                        texto_confirmar_clave.delete(0, END)
                                                                                        ])
    boton_registro.pack()
    boton_registro.place(x=55,y=120)
    #
    boton_destroy = Button(ventana_registro, text="Volver", command=ventana_registro.destroy)
    boton_destroy.pack()
    boton_destroy.place(x=188,y=120)
#----FIN REGISTRO DE USUARIOS----


def obtener_jugadores(maximo_jugadores):
    '''
    Autor: Rocio Donadel
    Registra los jugadores ingresados a través de interfaz en un diccionario.
    '''
    diccionario={}
    registro_jugadores = iniciar_ventana(maximo_jugadores)
    for jugador in registro_jugadores:
        #Orden variables: intentos, aciertos, promedio, intentos_totales, aciertos_totales, gano, partidas ganadas
        if not jugador == '': diccionario[jugador] = [0, 0, 0, 0, 0, '', 0]
    return diccionario