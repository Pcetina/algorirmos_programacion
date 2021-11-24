
from tkinter import *


#CrearVentana 
ventana = Tk()
ventana.title("Hospital Regional de Orinoquia")
ventana.geometry("740x700")
ventana.configure(background="medium purple")

def Enviar():
    
    lblrespuesta=Label(ventana,text="El formulario se envio correctamente!",font=("Courier New",10),background="purple3").place(x=430,y=625)


#Titulo
titulo=Label(ventana,text="HOSPITAL REGIONAL ORINOQUIA",font=("Segoe UI Black",18),background="medium purple")
titulo.pack()
titulo.grid(row=0,column=0)
titulo.place(x=180,y=0)


#Nombres
Nombre=Label(ventana,text="Digite su NOMBRE",font=("Courier New",14),background="medium purple")
Nombre.grid(row=1,column=0)
Nombre.place(x=10,y=70)
cuadro_Nombre=Entry(ventana)
cuadro_Nombre.grid(row=1,column=1)
cuadro_Nombre.place(x=250,y=70)


#Apellidos
apellidos=Label(ventana,text="Digite su APELLIDO",font=("Courier New",14),background="medium purple")
apellidos.grid(row=2,column=0)
apellidos.place(x=10,y=120)
apellidos_cuadro=Entry(ventana)
apellidos_cuadro.grid(row=2,column=1)
apellidos_cuadro.place(x=260,y=120)


#Edad
edad=Label(ventana,text="Digite su EDAD",font=("Courier New",14),background="medium purple")
edad.grid(row=3,column=0)
edad.place(x=10,y=170)
edad_cuadro=Entry(ventana)
edad_cuadro.grid(row=3,column=1)
edad_cuadro.place(x=240,y=170)


#Genero
Genero=Label(ventana,text="Digite su GENERO",font=("Courier New",14),background="medium purple")
Genero.grid(row=4,column=0)
Genero.place(x=10,y=220)
Genero_cuadro=Entry(ventana)
Genero_cuadro.grid(row=4,column=1)
Genero_cuadro.place(x=250,y=220)


#CC_TI
CC_TI=Label(ventana,text="Digite su CC/TI",font=("Courier New",14),background="medium purple")
CC_TI.grid(row=5,column=0)
CC_TI.place(x=10,y=270)
CC_TI_cuadro=Entry(ventana)
CC_TI_cuadro.grid(row=5,column=1)
CC_TI_cuadro.place(x=250,y=270)


#Correo_electronico
Correo_electronico=Label(ventana,text="Digite su CORREO ELECTRONICO",font=("Courier New",14),background="medium purple")
Correo_electronico.grid(row=6,column=0)
Correo_electronico.place(x=10,y=320)
Correo_electronico_cuadro=Entry(ventana)
Correo_electronico_cuadro.grid(row=6,column=1)
Correo_electronico_cuadro.place(x=340,y=320)

#Pregunta1 --> Alcohol
Alcohol=Label(ventana,text="¿Ha tomado alcohol estas dos ultimas semanas?",font=("Courier New",14),background="medium purple")
Alcohol.grid(row=7,column=0)
Alcohol.place(x=10,y=370)
Alcohol_cuadro=Entry(ventana)
Alcohol_cuadro.grid(row=7,column=1)
Alcohol_cuadro.place(x=540,y=370)

#Pregunta2 --> Anticonceptivos
Anticonceptivos=Label(ventana,text="¿Que metodo anticonceptivo utiliza?",font=("Courier New",14),background="medium purple")
Anticonceptivos.grid(row=8,column=0)
Anticonceptivos.place(x=10,y=420)
Anticonceptivos_cuadro=Entry(ventana)
Anticonceptivos_cuadro.grid(row=8,column=1)
Anticonceptivos_cuadro.place(x=450,y=420)

#Pregunta3 --> Fumar
Fumar=Label(ventana,text="¿Usted fuma?",font=("Courier New",14),background="medium purple")
Fumar.grid(row=9,column=0)
Fumar.place(x=10,y=470)
Fumar_cuadro=Entry(ventana)
Fumar_cuadro.grid(row=9,column=1)
Fumar_cuadro.place(x=200,y=470)

#Pregunta4 --> Cirugias
Cirugias=Label(ventana,text="¿Usted se ha hecho cirugías en el ultimo año?",font=("Courier New",14),background="medium purple")
Cirugias.grid(row=10,column=0)
Cirugias.place(x=10,y=520)
Cirugias_cuadro=Entry(ventana)
Cirugias_cuadro.grid(row=10,column=1)
Cirugias_cuadro.place(x=550,y=520)

#Pregunta5 --> Tatuajes
Tatuajes=Label(ventana,text="¿Usted se ha hecho tatuajes en el ultimo año?",font=("Courier New",14),background="medium purple")
Tatuajes.grid(row=11,column=0)
Tatuajes.place(x=10,y=570)
Tatuajes_cuadro=Entry(ventana)
Tatuajes_cuadro.grid(row=11,column=1)
Tatuajes_cuadro.place(x=550,y=570)

boton1=Button(ventana,command=Enviar,text="Enviar",font=("Verdana",13),background="green")
boton1.place(x=250,y=620)
boton2=Button(ventana,command=ventana.quit,text="Salir",font=("Verdana",13),background="red")
boton2.place(x=360,y=620)

ventana.mainloop()