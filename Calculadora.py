from tkinter import *
from PIL import ImageTk, Image
#------------------------------------------------Creación de la ventana------------------------------------------
raiz = Tk() #Crea la ventana
raiz.title("Calculadora") #titulo de la ventana
ancho_ventana = 400
alto_ventana = 200
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
posicion_x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
posicion_y = int((alto_pantalla / 2) - (alto_ventana / 2))
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")  # Establecer el tamaño y posición de la ventana 
#---------------------------------------------------Creacion de mi frame---------------------------------------------------------
miFrame = Frame(raiz) #Crea un que esta alfrente de la ventana
miFrame.pack(fill="both", expand=True) #Contiene lo que esta en la ventana
operacion="" #identificar la operación
pantalla=False
resultado=0
#--------------------Fondo de frame------------------------
imagen_fondo = Image.open("rosa.png")
imagen_fondo = imagen_fondo.resize((1560, 1600), Image.LANCZOS)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
label_fondo = Label(miFrame, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
#----------------------Ventana-----------------------------
numero_de_Pantalla = StringVar()
pantalla = Entry(miFrame,textvariable=numero_de_Pantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4, sticky="nsew")
pantalla.config(background="black",fg="#03f943", justify=RIGHT,font=("Arial", 24))
miFrame.columnconfigure(0, weight=0)
#------------------------Funciones de la calculadora--------------
def numeroDigitado(num):
    global operacion
    global pantalla
    if pantalla!=False:
        numero_de_Pantalla.set(num)
        pantalla=False
    else:
        numero_de_Pantalla.set(numero_de_Pantalla.get() + num)
#---------------------------Borrar un número----------------------
def borrar_numero():
    contenido_actual = numero_de_Pantalla.get()
    nuevo_contenido = contenido_actual[:-1]  # Elimina el último carácter
    numero_de_Pantalla.set(nuevo_contenido)
#---------------------------Operacion suma------------------------
def suma(num):
    global operacion
    global resultado
    global pantalla
    resultado+=int(num) #resultado=resultado+int(num)
    operacion="suma"
    pantalla=True
    numero_de_Pantalla.set(resultado)
#--------------------------Operacion resta-----------------------
num1=0
contador_resta=0
def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global pantalla
	if contador_resta==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-int(num)
		else:
			resultado=int(resultado)-int(num)	
		numero_de_Pantalla.set(resultado)
		resultado=numero_de_Pantalla.get()
	contador_resta=contador_resta+1
	operacion="resta"
	pantalla=True
#------------------------Operacion multipical----------------------
contador_multi=0
def multiplica(num):
	global operacion
	global resultado
	global num1
	global contador_multi
	global pantalla
	if contador_multi==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_multi==1:
			resultado=num1*int(num)
		else:
			resultado=int(resultado)*int(num)	
		numero_de_Pantalla.set(resultado)
		resultado=numero_de_Pantalla.get()
	contador_multi=contador_multi+1
	operacion="multiplicacion"
	pantalla=True
#-----------------funcion division---------------------
contador_divi=0
def divide(num):
	global operacion
	global resultado
	global num1
	global contador_divi
	global pantalla
	if contador_divi==0:
		num1=float(num)
		resultado=num1
	else:
		if contador_divi==1:
			resultado=num1/float(num)
		else:
			resultado=float(resultado)/float(num)	
		numero_de_Pantalla.set(resultado)
		resultado=numero_de_Pantalla.get()
	contador_divi=contador_divi+1
	operacion="division"
	pantalla=True
#---------------------------Operacion resultado--------------------
def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi
    if operacion=="suma":
        numero_de_Pantalla.set(resultado+int(numero_de_Pantalla.get()))
        resultado=0
    elif operacion=="resta":
        numero_de_Pantalla.set(int(resultado)-int(numero_de_Pantalla.get()))
        resultado=0
        contador_resta=0
    elif operacion=="multiplicacion":
        numero_de_Pantalla.set(int(resultado)*int(numero_de_Pantalla.get()))
        resultado=0
        contador_multi=0
    elif operacion=="division":
        numero_de_Pantalla.set(int(resultado)/int(numero_de_Pantalla.get()))
        resultado=0
        contador_divi=0
#-----------------------Fila 1 ------------------------------
boton_7 = Button(miFrame,text="7",width="3",bg="violet",command=lambda:numeroDigitado("7"))
boton_7.grid(row=2, column=1,sticky="nsew")
boton_8 = Button(miFrame,text="8",width="3",bg="violet",command=lambda:numeroDigitado("8"))
boton_8.grid(row=2, column=2,sticky="nsew")
boton_9 = Button(miFrame,text="9",width="3",bg="violet",command=lambda:numeroDigitado("9"))
boton_9.grid(row=2, column=3,sticky="nsew")
boton_multi = Button(miFrame,text="X",width="3",bg="#FF00FF",command=lambda:multiplica(numero_de_Pantalla.get()))
boton_multi.grid(row=2, column=4,sticky="nsew")
miFrame.columnconfigure(1, weight=1)
miFrame.rowconfigure(1, weight=1)
miFrame.columnconfigure(2, weight=1)
miFrame.columnconfigure(3, weight=1)
miFrame.columnconfigure(4, weight=1)
#-------------------------Fila 2 ----------------------------
boton_4 = Button(miFrame,text="4",width="3",bg="violet",command=lambda:numeroDigitado("4"))
boton_4.grid(row=3, column=1,sticky="nsew")
boton_5 = Button(miFrame,text="5",width="3",bg="violet",command=lambda:numeroDigitado("5"))
boton_5.grid(row=3, column=2,sticky="nsew")
boton_6 = Button(miFrame,text="6",width="3",bg="violet",command=lambda:numeroDigitado("6"))
boton_6.grid(row=3, column=3,sticky="nsew")
boton_divi = Button(miFrame,text="÷",width="3",bg="#FF00FF",command=lambda:divide(numero_de_Pantalla.get()))
boton_divi.grid(row=3, column=4,sticky="nsew")
#-------------------------Fila 3 ----------------------------
boton_1 = Button(miFrame,text="1",width="3",bg="violet",command=lambda:numeroDigitado("1"))
boton_1.grid(row=4, column=1,sticky="nsew")
boton_2 = Button(miFrame,text="2",width="3",bg="violet",command=lambda:numeroDigitado("2"))
boton_2.grid(row=4, column=2,sticky="nsew")
boton_3 = Button(miFrame,text="3",width="3",bg="violet",command=lambda:numeroDigitado("3"))
boton_3.grid(row=4, column=3,sticky="nsew")
boton_resta = Button(miFrame,text="-",width="3",bg="#FF00FF",command=lambda:resta(numero_de_Pantalla.get()))
boton_resta.grid(row=4, column=4,sticky="nsew")
#-------------------------Fila 4 ----------------------------
boton_0 = Button(miFrame,text="0",width="3",bg="violet",command=lambda:numeroDigitado("0"))
boton_0.grid(row=5, column=1,sticky="nsew")
boton_coma = Button(miFrame,text=",",width="3",bg="#FF00FF",command=lambda:numeroDigitado(","))
boton_coma.grid(row=5, column=2,sticky="nsew")
boton_igual = Button(miFrame,text="=",width="3",bg="#FF00FF",command=lambda:el_resultado())
boton_igual.grid(row=5, column=3,sticky="nsew")
boton_suma = Button(miFrame,text="+",width="3",bg="#FF00FF",command=lambda:suma(numero_de_Pantalla.get()))
boton_suma.grid(row=5, column=4,sticky="nsew")
boton_borrar = Button(miFrame, text="⌫", width="3", bg="#FF00FF", command=borrar_numero)
boton_borrar.grid(row=6, column=1, sticky="nsew", columnspan=4)
raiz.mainloop() #Lo que muestra en la ventana