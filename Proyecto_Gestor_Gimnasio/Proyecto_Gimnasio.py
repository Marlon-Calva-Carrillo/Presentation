#Proyecto Gimnasio
#Con el siguiente codigo puedes gestionar tus ventas.
#Seleccionar el producto y la cantidad que deseas vender.
#Descarga el ticket y guardalo en la ubicacion que desees.

#Importo librerias
from tkinter import *
import random
import datetime
from tkinter import  filedialog, messagebox #Filedialog=dialogo de archivo, Messagebox= caja de mensajes

operador = ''
precios_suplementos = [600, 700, 900, 900, 900, 700, 550, 1499]
precios_productos = [38, 22, 45, 20, 17, 8, 30, 20]
precios_accesorios = [230, 700, 400, 320, 350, 500, 250, 430]

#************FUNCIONES************
#Funcion para ingresar numero y operadores a la calculadora.
def click_boton(numero):
    global operador #Debemos acceder a un operador pero como esta fuera de la funcion la hacemos global.
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

#Funcion para eliminar el contenido del visor.
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

#Funcion para obtener el resultado.
def obtener_resultador():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0, resultado)
    operador = ''

#Funcion para validar los check box
def revisar_check():  #Funcion que valida cuando seleccionamos los check box, limpia y permite ingresar un dato.
    x = 0
    for c in cuadros_suplementos:
        if variables_suplementos[x].get() == 1:
            cuadros_suplementos[x].config(state=NORMAL)
            if cuadros_suplementos[x].get() == '0':
                cuadros_suplementos[x].delete(0, END)
            cuadros_suplementos[x].focus() #Focus es un metodo que sirve para poder poner el cursos enfocado en ese elemento.
        else:
            cuadros_suplementos[x].config(state=DISABLED)
            texto_suplementos[x].set('0')
        x += 1

    x = 0
    for c in cuadros_productos:
        if variables_productos[x].get() == 1:
            cuadros_productos[x].config(state=NORMAL)
            if cuadros_productos[x].get() == '0':
                cuadros_productos[x].delete(0, END)
            cuadros_productos[x].focus()
        else:
            cuadros_productos[x].config(state=DISABLED)
            texto_productos[x].set('0')
        x += 1

    x = 0
    for c in cuadros_accesorios:
        if variables_accesorios[x].get() == 1:
            cuadros_accesorios[x].config(state=NORMAL)
            if cuadros_accesorios[x].get() == '0':
                cuadros_accesorios[x].delete(0, END)
            cuadros_accesorios[x].focus()
        else:
            cuadros_accesorios[x].config(state=DISABLED)
            texto_accesorios[x].set('0')
        x += 1

#Funcion para calcular el total.
def total():
    sub_total_suplementos = 0
    p = 0
    for cantidad in texto_suplementos:
        sub_total_suplementos = sub_total_suplementos + (float(cantidad.get()) * precios_suplementos[0])
        p += 1

    sub_total_productos = 0
    p = 0
    for cantidad in texto_productos:
        sub_total_productos = sub_total_productos + (float(cantidad.get()) * precios_productos[0])
        p += 1

    sub_total_accesorios = 0
    p = 0
    for cantidad in texto_accesorios:
        sub_total_accesorios = sub_total_accesorios + (float(cantidad.get()) * precios_accesorios[0])
        p += 1

    sub_total = sub_total_suplementos + sub_total_productos + sub_total_accesorios
    impuestos = sub_total * 0.07
    total = sub_total+impuestos

    var_costo_suplementos.set(f'$ {round(sub_total_suplementos, 2)}')
    var_costo_productos.set(f'$ {round(sub_total_productos, 2)}')
    var_costo_accesorios.set(f'$ {round(sub_total_accesorios, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

#Funcion para generar el recibo.
def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' *  63 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for suplemento in texto_suplementos:
        if suplemento.get() != '0':
            texto_recibo.insert(END, f'{lista_suplementos[x]}\t\t{suplemento.get()}\t'
                                     f'$ {int(suplemento.get()) * precios_suplementos[x]}\n')
        x += 1

    x = 0
    for productos in texto_productos:
        if productos.get() != '0':
            texto_recibo.insert(END, f'{lista_productos[x]}\t\t{productos.get()}\t'
                                     f'${int(productos.get()) * precios_productos[x]}\n')
        x += 1

    x = 0
    for accesorio in texto_accesorios:
        if accesorio.get() != '0':
            texto_recibo.insert(END, f'{lista_accesorios[x]}\t\t{accesorio.get()}\t'
                                     f'${int(accesorio.get()) * precios_accesorios[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Costo de Suplementos: \t\t\t{var_costo_suplementos.get()}\n')
    texto_recibo.insert(END, f'Costo de los Productos: \t\t\t{var_costo_productos.get()}\n')
    texto_recibo.insert(END, f'Costo de los Accesorios: \t\t\t{var_costo_accesorios.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Sub-Total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' *  63 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')

#Funcion para guardar el recibo en un archivo de texto.
def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    #Asignamos el modo (w es de escritura) y extension del archivo.
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Aviso', 'Su recibo ha sido guardado')

#Funcion para limpiar cada espacio de la interfaz
def resetear():
    texto_recibo.delete(0.1, END) #Ciclo para limpiar los cuadros de texto de cada categoria.
    for texto in texto_suplementos:
        texto.set('0')
    for texto in texto_productos:
        texto.set('0')
    for texto in texto_accesorios:
        texto.set('0')

    for cuadro in cuadros_suplementos:  #Ciclo para desactivar los cuadros de texto.
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_productos:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_accesorios:
        cuadro.config(state=DISABLED)

    for v in variables_suplementos:  #Ciclo para limpiar los textbox.
        v.set(0)
    for v in variables_productos:
        v.set(0)
    for v in variables_accesorios:
        v.set(0)
    var_costo_suplementos.set('')
    var_costo_productos.set('')
    var_costo_accesorios.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

#Iniciar tkinter
aplicacion = Tk()

#Tamaño de la ventana
aplicacion. geometry('1020x630+0+0') #Tamaño de pantalla (ancho y alto, ubicacion eje x y eje y)

#Evitar maximizar
aplicacion.resizable ()#Se usa para que el usuario no pueda modificar el tamaño de la pantalla

#Titulo de la ventana
aplicacion.title("Marlon's Gym (Facturacion)")

#Color de fondo de la vantana
#Puedes conseguir mas colores en:
#https:**es.wikibooks.org*wiki*Python*Interfaz_gr%C3%A1fica_con_Tkinter*Los_nombres_de_los_colores
#En la pagina anterior sustituir los '*' por 'diagonal'
aplicacion.config(bg='azure1') #bg=background

#PANEL SUPERIOR
#Frame nos permite crear cuadros, br=borde, relievef=relieve (puedes usar: Flat, Raised, Sunken, Groove, Ridge)
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP) #Lado, top=arriba

#Etiqueta (Titulo)
#Los argumentos de un label son, ubicacion, contenido, color (()), tipo de fuente (font),
etiqueta_titulo = Label(panel_superior, text='Facturacion Gym', fg='azure4',
                        font=('Dosis',58), bg='azure2', width=27)
etiqueta_titulo.grid(row=0,column=0)  #grid es cuadricula

#PANEL IZQUIERDO
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

#Panel costos (izquierdo)
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50) #Dentro del lado izquierdo
panel_costos.pack(side=BOTTOM) #Ubicamos al panel costos a traves del pack en el fondo (side) de nuestro panel izquierdo
#Bottom=abajo /al fondo

#Panel suplementos (izquierdo)
#Labframe= cuadro con etiqueta, dentro de panel izquierdo, texto de la etiqueta, contiene fuente tamaño estilo (bold=negritas)
#borde=bd, relief (estilo o efecto visual),
panel_suplementos = LabelFrame (panel_izquierdo, text='Suplemento', font=('Dosis',19, 'bold'),
                            bd=1, relief=FLAT, fg='azure4')
panel_suplementos.pack(side=LEFT)

#Panel productos (izquierdo)
panel_productos = LabelFrame (panel_izquierdo, text='Producto', font=('Dosis', 19, 'bold'),
                              bd=1, relief=FLAT, fg='azure4')
panel_productos.pack(side=LEFT)

#Panel accesorios (izquierdo)
panel_accesorios = LabelFrame (panel_izquierdo, text='Accesorio', font=('Dosis', 19, 'bold'),
                               bd=1, relief=FLAT, fg='azure4')
panel_accesorios.pack(side=LEFT)

#PANEL DERECHA
panel_derecho = Frame(aplicacion, bd=1,relief=FLAT)
panel_derecho.pack(side=RIGHT)

#Panel calculadora (derecha)
panel_calculadora = Frame(panel_derecho, bd=2, relief=FLAT, bg='azure2')
panel_calculadora.pack() #Si pack esta vacio por defecto va arriba

#Panel recibo (derecha)
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg='azure2')
panel_recibo.pack()

#Panel botones (derecha)
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg='azure2')
panel_botones.pack()

#LISTA DE PRODUCTOS.
lista_suplementos = ['Pre-entreno durazno', 'Pre-entreno limón', 'Proteína Vainilla', 'Proteína Chocolate', 'Proteína Fresa', 'Creatina', 'Omega-3', 'Testosterona']
lista_productos = ['Monster', 'Volt', 'RedBull', 'Amper', 'Barra-chocolate', 'Toalla sanitaria', 'Gatorade limon', 'Electrolit']
lista_accesorios = ['Muñequeras', 'Faja', 'Cinturon', 'Ganchos', 'Straps', 'Seguros-Barra', 'Clips-Pesas', 'Guantes']

#Crear un checkbutton, posicionar, establecer el texto de cada etiqueta.
#Onvalue= valor que va a tener checkbox cuando esta activada la casilla.
#Offvalue= Cuando la casilla este desactivada.

#Generar items de suplementos
variables_suplementos = []
cuadros_suplementos = []
texto_suplementos = []
contador = 0
for suplemento in lista_suplementos:
    #Crear checkbutton
    variables_suplementos.append('')
    variables_suplementos[contador] = IntVar()  #IntVar=variable integer, es una clase de tkinter que permite crear variables especif.
    suplemento = Checkbutton(panel_suplementos, text=suplemento.title(),
                             font=('dosis', 19, 'bold',),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_suplementos[contador],
                             command=revisar_check)
    suplemento.grid(row=contador,
                    column=0,
                    sticky=W) #Grid nos permite establecer filas y columnas

    #Crear cuadros de entrada
    cuadros_suplementos.append('')
    texto_suplementos.append('')
    texto_suplementos[contador] = StringVar() #Variable de tipo String (tkinter)
    texto_suplementos[contador].set('0')

    cuadros_suplementos[contador] = Entry (panel_suplementos,
                                           font=('Dosis', 18, 'bold'),
                                           bd=1,
                                           width=6,
                                           state=DISABLED,
                                           textvariable=texto_suplementos[contador])
    cuadros_suplementos[contador].grid(row=contador,
                                       column=1)
    contador += 1

#Generar items de los productos
variables_productos = []
cuadros_productos = []
texto_productos = []
contador = 0
for producto in lista_productos:
    #Crear checkbutton
    variables_productos.append('')
    variables_productos[contador] = IntVar()  # IntVar=variable integer, es una clase de tkinter que permite crear variables especif.
    producto = Checkbutton(panel_productos, text=producto.title(),
                           font=('dosis', 19, 'bold'),
                           onvalue=1,
                           offvalue=0,
                           variable=variables_productos[contador],
                           command=revisar_check)
    producto.grid(row=contador,
                  column=0,
                  sticky=W)  # Grid nos permite establecer filas y columnas

    #Crear cuadros de entrada
    cuadros_productos.append('')
    texto_productos.append('')
    texto_productos[contador] = StringVar() #Variable de tipo String (tkinter)
    texto_productos[contador].set('0')

    cuadros_productos[contador] = Entry (panel_productos,
                                         font=('Dosis', 18, 'bold'),
                                         bd=1,
                                         width=6,
                                         state=DISABLED,
                                         textvariable=texto_productos[contador])
    cuadros_productos[contador].grid(row=contador,
                                     column=1)
    contador += 1

#Generar items de Accesorios
variables_accesorios = []
cuadros_accesorios = []
texto_accesorios = []
contador = 0
for accesorio in lista_accesorios:
    #Crear checkbutton
    variables_accesorios.append('')
    variables_accesorios[
        contador] = IntVar()  # IntVar=variable integer, es una clase de tkinter que permite crear variables especif.
    accesorio = Checkbutton(panel_accesorios, text=accesorio.title(),
                            font=('dosis', 19, 'bold'),
                            onvalue=1,
                            offvalue=0,
                            variable=variables_accesorios[contador],
                            command=revisar_check)
    accesorio.grid(row=contador,
                   column=0,
                   sticky=W)  # Grid nos permite establecer filas y columnas

    #Crear cuadros de entrada
    cuadros_accesorios.append('')
    texto_accesorios.append('')
    texto_accesorios[contador] = StringVar() #Variable de tipo String (tkinter)
    texto_accesorios[contador].set('0')
    cuadros_accesorios[contador] = Entry (panel_accesorios,
                                          font=('Dosis', 18, 'bold'),
                                          bd=1,
                                          width=6,
                                          state=DISABLED,
                                          textvariable=texto_accesorios[contador])
    cuadros_accesorios[contador].grid(row=contador,
                                      column=1)
    contador += 1

#VARIABLES
var_costo_suplementos = StringVar()
var_costo_productos = StringVar()
var_costo_accesorios = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

#ETIQUETAS DE COSTOS (SUPLEMENTOS) Y CAMPOS DE ENTRADA
etiqueta_costo_suplementos = Label(panel_costos,
                                   text = 'Costo Suplemento',
                                   font = ('Dosis', 12, 'bold'),
                                   bg = 'azure4',
                                   fg = 'white')

etiqueta_costo_suplementos.grid(row=0, column=0)
texto_costo_suplementos = Entry(panel_costos,
                                font=('Dosis',12,'bold'),
                                bd=1,
                                width=10,
                                state='readonly',
                                textvariable=var_costo_suplementos)
texto_costo_suplementos.grid(row=0, column=1, padx=41)


#ETIQUETAS DE COSTOS (PRODUCTOS) Y CAMPOS DE ENTRADA
etiqueta_costo_productos = Label(panel_costos,
                                 text = 'Costo Producto',
                                 font = ('Dosis', 12, 'bold'),
                                 bg = 'azure4',
                                 fg = 'white')

etiqueta_costo_productos.grid(row=1, column=0)
texto_costo_productos = Entry(panel_costos,
                              font=('Dosis',12,'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_productos)
texto_costo_productos.grid(row=1, column=1, padx=41)

#ETIQUETAS DE COSTOS (ACCESORIO) Y CAMPOS DE ENTRADA
etiqueta_costo_accesorio = Label(panel_costos,
                                 text = 'Costo Accesorio',
                                 font = ('Dosis', 12, 'bold'),
                                 bg = 'azure4',
                                 fg = 'white')

etiqueta_costo_accesorio.grid(row=2, column=0)
texto_costo_accesorio = Entry(panel_costos,
                              font=('Dosis',12,'bold'),
                              bd=1,
                              width=10,
                              state='readonly',
                              textvariable=var_costo_accesorios)
texto_costo_accesorio.grid(row=2, column=1, padx=41)

#ETIQUETAS DE SUBTOTAL Y CAMPOS DE ENTRADA
etiqueta_subtotal = Label(panel_costos,
                              text = 'Subtotal',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3, padx=41)

#ETIQUETAS DE IMPUESTO Y CAMPOS DE ENTRADA
etiqueta_impuesto = Label(panel_costos,
                              text = 'Impuesto',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3, padx=41)


#ETIQUETAS DE TOTAL Y CAMPOS DE ENTRADA
etiqueta_total = Label(panel_costos,
                              text = 'Total',
                              font = ('Dosis', 12, 'bold'),
                              bg = 'azure4',
                              fg = 'white')

etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                           font=('Dosis',12,'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2,column=3, padx=41)

#BOTONES
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas+=1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


#AREA DE RECIBO
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12,'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

#CALCULADORA
visor_calculadora=Entry(panel_calculadora,
                        font=('Dosis',16,'bold'),
                        width=32,
                        bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7','8','9','+', '4','5','6','-',
                       '1','2','3','x', 'R','Borrar','0','/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,   #Ubicacion
                 text=boton.title(),
                 font=('Dosis', 16, 'bold'),
                 fg='white',
                 bg='azure4',
                 bd=1,
                 width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultador)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

#Evitar que la pantalla se cierre
aplicacion.mainloop()
