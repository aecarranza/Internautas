from tkinter import *

X_LABEL, X_ENTRYBOX, Y_USUARIO, Y_CLAVE = 12, 110, 11, 41
COLOR_VENTANA, COLOR_FRAME, COLOR_FUENTE = "#574236", "#C3581B", "white"

def obtener_datos():
    datos = {"Richard":"1", "Francisco":"2", "Ezequiel":"3", "Rocio":"4", "Jaime":"5", "Nicolas":"6"}
    return datos

def levantar_validacion(mensaje):
    #popup
    ventana_validacion = Toplevel(ventana)
    ventana_validacion.title("Validación")
    ventana_validacion.geometry("257x28")
    ventana_validacion.config(bg=COLOR_VENTANA)
    ventana_validacion.resizable(0, 0)
    ventana_validacion.iconbitmap("internautas.ico")
    #label
    texto = Label(ventana_validacion, text=mensaje, fg=COLOR_FUENTE)
    texto.config(bg=COLOR_VENTANA)
    texto.place(x=5, y=2)

def validar_datos():
    usuario = texto_usuario.get()
    clave = texto_clave.get()
    if usuario and clave:
        datos = obtener_datos()
        usuarios = list(datos.keys())
        claves = list(datos.values())
        if usuario in usuarios:
            pos = usuarios.index(usuario)
            if clave == claves[pos]:
                levantar_validacion("Usuario y Clave Correctos")
            else:
                levantar_validacion("Algunos de los datos ingresados es Incorrecto")
        else:
            levantar_validacion("Algunos de los datos ingresados es Incorrecto")


#ventana    
ventana=Tk()
ventana.title("Login Internautas")
ventana.geometry("300x130")
ventana.resizable(0,0)
ventana.iconbitmap("internautas.ico")
ventana.config(bg=COLOR_VENTANA)

#frame
miframe=Frame(ventana,width=240,height=70)
miframe.config(bg=COLOR_FRAME)
miframe.pack()
miframe.place(x=30,y=30)

#entrada de datos
usuario=Label(miframe,text="Usuario Alumno",fg=COLOR_FUENTE)
usuario.config(bg=COLOR_FRAME)
usuario.place(x=X_LABEL,y=Y_USUARIO)

texto_usuario=Entry(miframe)
texto_usuario.place(x=X_ENTRYBOX,y=Y_USUARIO)

clave=Label(miframe,text="Clave",fg=COLOR_FUENTE)
clave.config(bg=COLOR_FRAME)
clave.place(x=X_LABEL,y=Y_CLAVE)

texto_clave=Entry(miframe)
texto_clave.place(x=X_ENTRYBOX,y=Y_CLAVE)
texto_clave.config(show="*")

validacion = Label(miframe)

#boton
boton=Button(ventana, text="Ingresar", command=validar_datos)
boton.pack()
boton.place(x=120,y=101.5)

ventana.mainloop()