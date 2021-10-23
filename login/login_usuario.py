from tkinter import *

datos={}

def obtener_usuario_claves():
    global datos
    datos={"Richard":"Internautas", "Francisco":"Internautas", "Ezequiel":"Internautas", "Rocio":"Internautas", "Jaime":"Internautas", "Nicolas":"Internautas"}
    print(datos)

def levantar_validacion(mensaje):
    #popup
    ventana_validacion = Toplevel(ventana)
    ventana_validacion.title("Validación")
    ventana_validacion.geometry("257x28")
    ventana_validacion.config(bg="#574236")
    ventana_validacion.resizable(0,0)
    ventana_validacion.iconbitmap("internautas.ico")
    #label
    texto = Label(ventana_validacion,text=mensaje,fg="white")
    texto.config(bg="#574236")
    texto.place(x=5,y=2)
    '''
    validacion.config(text="")
    validacion.config(text=mensaje)
    validacion.place(x=6, y=3)
    '''

def validar_datos():
    usuario = texto_usuario.get()
    clave = texto_clave.get()
    if usuario and clave:
        usuario_valido = False
        for dato in datos:
            if dato == usuario and datos[dato] == clave:
                levantar_validacion("Usuario y Clave Correctos")
                usuario_valido = True
        if not usuario_valido:
            levantar_validacion("Algunos de los datos ingresados es Incorrecto")


obtener_usuario_claves()

#ventana    
ventana=Tk()
ventana.title("Login Internautas")
ventana.geometry("300x130")
ventana.resizable(0,0)
ventana.iconbitmap("internautas.ico")
ventana.config(bg="#574236")

#frame
miframe=Frame(ventana,width=240,height=70)
miframe.config(bg="#C3581B")
miframe.pack()
miframe.place(x=30,y=30)

#entrada de datos
usuario=Label(miframe,text="Usuario Alumno",fg="white")
usuario.config(bg="#C3581B")
usuario.place(x=12, y=11)

texto_usuario=Entry(miframe)
texto_usuario.place(x=110,y=11)

clave=Label(miframe,text="Clave",fg="white")
clave.config(bg="#C3581B")
clave.place(x=12, y=41)

texto_clave=Entry(miframe)
texto_clave.place(x=110,y=41)
texto_clave.config(show="*")

validacion = Label(miframe)

#boton
boton=Button(ventana, text="Ingresar", command=validar_datos)
boton.pack()
boton.place(x=120,y=101.5)

ventana.mainloop()