import tkinter as tt
from tkinter import ttk
from tkinter import messagebox


def Inicio():
    global ventana
    ventana = tt.Tk()
    global usuario
    usuario = tt.StringVar()
    global clave
    clave = tt.StringVar()
    global rol
    rol = tt.StringVar()

    ventana.title("Sistema Registro de Secciones")
    ventana.geometry("400x400")
    

    tt.Label(ventana,text="Ingreso al Sistema",bg="Blue",width="100",font="Arial",foreground="white").pack()
    tt.Label(ventana).pack()
    tt.Label(ventana,text="Por favor digite sus datos").pack()
    tt.Label(ventana).pack()
    tt.Label(ventana,text="Digite su usuario").pack()
    tt.Entry(ventana,textvariable=usuario).pack()
    tt.Label(ventana,text="Digite su Calve").pack()
    tt.Entry(ventana,textvariable=clave,show="*").pack()
    tt.Label(ventana).pack()
    tt.Button(ventana,text="Login",command=FuncionVerificarUsuario).pack()
    tt.Label(ventana).pack()
    tt.Label(ventana).pack()
    tt.Label(ventana,text="Estos son los usuarios iniciales el registro está en las opciones de admin").pack()
    tt.Label(ventana,text="Usuario1: admin / clave:123").pack()
    tt.Label(ventana,text="Usuario2: ofici / clave 123").pack()

    ventana.mainloop()


listausuarios = {"admin":["123","Nivel Administrador"],"ofici":["123","Nivel oficinista"]}


def FuncionVerificarUsuario():

    
    encontrar = False

    for llave, valor in listausuarios.items():
        if usuario.get() == llave and clave.get() == valor[0]:  
            encontrar = True
            sesionrol= valor[1]
            break
        else: 
            encontrar = False

    if encontrar and sesionrol== "Nivel Administrador":
        messagebox.showinfo("","Usuario encontrado")
        ventana.destroy()
        global ventanaa
        ventanaa = tt.Tk()
        menu = tt.Menu()    
        ventanaa.title("Nivel Administrador")
        ventanaa.geometry("500x500")

# Se crean las opciones principales
        menu_ingresos = tt.Menu(menu, tearoff=0)
        menu_consultas = tt.Menu(menu, tearoff=0)
        menu_salir = tt.Menu(menu, tearoff=0)

# Agregar las opciones principales al menú
        menu.add_cascade(label="Ingresos", menu=menu_ingresos)
        menu.add_cascade(label="Consultas", menu=menu_consultas)
        menu.add_cascade(label="Salir", menu=menu_salir)

# Se crean las subopciones para "ingresos"
        menu_ingresos.add_command(label="Crear Sección",command=cargaseccion)
        menu_ingresos.add_command(label="Agregar Alumno",command=cargaalumnos)
        menu_ingresos.add_separator()
        menu_ingresos.add_command(label="Agregar Usuario",command=Registro)

# Se crean las subopciones para "consultas"
        menu_consultas.add_command(label="Consultar Sección",command=seccionesss)
        menu_consultas.add_command(label="Consultar Alumno",command=listaalumnoooss)

        menu_salir.add_command(label="Salir", command=ventanaa.quit)


        ventanaa.config(menu=menu)

        menu_secciones = tt.Menu(menu_consultas, tearoff=0)
        menu_secciones.add_command(label="Sección 1")
        menu_secciones.add_command(label="Sección 2")
        menu_secciones.add_command(label="Sección 3")

        menu_consultas.add_cascade(label="Secciones 1 2 3", menu=menu_secciones)

        menu_consultas = tt.Menu(menu, tearoff=1)

        menu_secciones = tt.Menu(menu_consultas, tearoff=1)

        ventanaa.mainloop()
            
########oficinista
    if encontrar and sesionrol== "Nivel oficinista":
        messagebox.showinfo("","Usuario encontrado")
        ventana.destroy()
        global ventanao
        ventanao = tt.Tk()
        menu = tt.Menu()    
        ventanao.title("Nivel Administrador")
        ventanao.geometry("500x500")

# Se crean las opciones principales
        menu_ingresos = tt.Menu(menu, tearoff=0)
        menu_consultas = tt.Menu(menu, tearoff=0)
        menu_salir = tt.Menu(menu, tearoff=0)

# Agregar las opciones principales al menú
        menu.add_cascade(label="Ingresos", menu=menu_ingresos)
        menu.add_cascade(label="Consultas", menu=menu_consultas)
        menu.add_cascade(label="Salir", menu=menu_salir)

# Se crean las subopciones para "ingresos"
       # menu_ingresos.add_command(label="Crear Sección",command=cargaseccion)
        menu_ingresos.add_command(label="Agregar Alumno",command=cargaalumnos)
       # menu_ingresos.add_separator()
       # menu_ingresos.add_command(label="Agregar Usuario",command=Registro)

# Se crean las subopciones para "consultas"
        menu_consultas.add_command(label="Consultar Sección",command=seccionesss)
        menu_consultas.add_command(label="Consultar Alumno",command=listaalumnoooss)

        menu_salir.add_command(label="Salir", command=ventanao.quit)


        ventanao.config(menu=menu)

        #menu_secciones = tt.Menu(menu_consultas, tearoff=0)
       # menu_secciones.add_command(label="Sección 1")
        #menu_secciones.add_command(label="Sección 2")
        #menu_secciones.add_command(label="Sección 3")

       # menu_consultas.add_cascade(label="Secciones 1 2 3", menu=menu_secciones)

        menu_consultas = tt.Menu(menu, tearoff=1)

       # menu_secciones = tt.Menu(menu_consultas, tearoff=1)

        ventanao.mainloop()

            




    else:
        messagebox.showerror("","Error")
        

####################### agregar user


valores = ["Nivel Administrador","Nivel oficinista"]
def Registro():
    ventana_Registro = tt.Toplevel(ventanaa)
    ventana_Registro.title("Ventana Registro")
    ventana_Registro.geometry("500x500")
    global usuarioRegistro
    global claveRegistro
    global rolRegistro
    usuarioRegistro = tt.StringVar()
    claveRegistro = tt.StringVar()
    rolRegistro = tt.StringVar()
    tt.Label(ventana_Registro,text="Por favor digite usuario").pack()
    entradausuarioRegistro = tt.Entry(ventana_Registro,textvariable=usuarioRegistro).pack()
    tt.Label(ventana_Registro,text="Por favor digite Contraseña").pack()
    entradaclaveRegistro = tt.Entry(ventana_Registro,textvariable=claveRegistro).pack()
    tt.Label(ventana_Registro,text="Por favor elija el rol").pack()
    comboboxRegistro = ttk.Combobox(ventana_Registro,textvariable=rolRegistro,values=valores,state="readonly")
    comboboxRegistro.pack()
    tt.Button(ventana_Registro,text="Guardar",command=GuardarRegistro).pack()


def GuardarRegistro():
    
    datos = []
    datos.append(claveRegistro.get())
    datos.append(rolRegistro.get())
    listausuarios[usuarioRegistro.get()] = datos
    messagebox.showinfo("Alerta","Usuario Guardado")
    listaaausers()
    
def listaaausers():
    aja1= tt.Tk()
    aja1.title("Lista usuarios")
    aja1.geometry("500x500")
    for x, y in listausuarios.items():
        tt.Label(aja1,text=(x," con clave ",y) ,bg="Blue",width="100",font="Arial",foreground="white").pack()
    
    aja1.mainloop()


############################# agregar alumno ###################

listasecciones = ["Sección 1","Sección 2","Sección 3"]
seccioness={}

def cargaalumnos():
    ventana_Realumn = tt.Toplevel(ventanaa)
    ventana_Realumn.title("Ventana Registro")
    ventana_Realumn.geometry("500x500")
    global nombreRegistro
    global apellidoRegistro
    global idRegistro
    global seccionregistro
    nombreRegistro = tt.StringVar()
    apellidoRegistro = tt.StringVar()
    idRegistro = tt.StringVar()
    seccionregistro=tt.StringVar()
    tt.Label(ventana_Realumn,text="Nombre del alumno").pack()
    entradanombreRegistro = tt.Entry(ventana_Realumn,textvariable=nombreRegistro).pack()
    tt.Label(ventana_Realumn,text="Igrese el apellido").pack()
    entradaapellidoRegistro = tt.Entry(ventana_Realumn,textvariable=apellidoRegistro).pack()
    tt.Label(ventana_Realumn,text="Cedula del alumno").pack()
    entradaidRegistro = tt.Entry(ventana_Realumn,textvariable=idRegistro).pack()
    tt.Label(ventana_Realumn,text="Por favor elija la sección").pack()
    comboboxRegistroalumno = ttk.Combobox(ventana_Realumn,textvariable=seccionregistro,values=listasecciones,state="readonly")
    comboboxRegistroalumno.pack()


    tt.Button(ventana_Realumn,text="Guardar",command=Guardaralumno).pack()


def Guardaralumno():
    
    datos1 = []
    datos1.append(nombreRegistro.get())
    datos1.append(apellidoRegistro.get())
    datos1.append(idRegistro.get())
    seccioness[seccionregistro.get()] = datos1
    messagebox.showinfo("Alerta","Alumno guardado")
    

 

def listaalumnoooss():
    aja2= tt.Tk()
    aja2.title("Lista alumnos")
    aja2.geometry("500x500")
    for x, y in seccioness.items():
        tt.Label(aja2,text=(x,y) ,bg="Blue",width="100",font="Arial",foreground="white").pack()
    
    aja2.mainloop()  

##############agregar seccion

listasecciones = ["Sección 1","Sección 2","Sección 3"]


def cargaseccion():
    ventana_agresec = tt.Toplevel(ventanaa)
    ventana_agresec.title("Ventana Registro")
    ventana_agresec.geometry("500x500")
    global nuevaseccion
    global nombreseccion
    nombreseccion = tt.StringVar()
    tt.Label(ventana_agresec,text="Número de la nueva sección").pack()
    entradaseccion = tt.Entry(ventana_agresec,textvariable=nombreseccion).pack()
   
    tt.Button(ventana_agresec,text="Guardar",command=Guardarseccionn).pack()


def Guardarseccionn():
    
    listasecciones.append(nombreseccion.get())
    messagebox.showinfo("Alerta","seccion guardada")
    

 

def seccionesss():
    aja3= tt.Tk()
    aja3.title("Lista secciones")
    aja3.geometry("500x500")
    tt.Label(aja3,text=listasecciones ,bg="Blue",width="100",font="Arial",foreground="white").pack()
    
    aja3.mainloop()  












Inicio()