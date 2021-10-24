class Persona(): 
  def init(self): 
    pass
  def Registro(self): 

#Datos del usuario

    print("--------------------------------------------------")
    print(" ")
    self.nombre=str(input("Señor usuario, por favor digite su nombre: "))
    while self.nombre.isalpha()==False: 
      print("Solo puede ingresar letras:")
      self.nombre=input("Digite nombre: ")
    self.nombre=str(self.nombre)  
        
    self.edad=(input("Señor usuario, por favor digite su edad: "))
    while self.edad.isdigit() == False: 
     print("Solo puede ingresar numeros")
     self.edad= input("Digite su edad: ")
    self.edad=int(self.edad) 
     
    while self.edad<15 or self.edad>99: 
      print("Edad no valida")
      print("Su edad debe ser mayor a 15 años y menor a 99 años")
      self.edad=(input("Digite su edad:"))
      self.edad=int(self.edad)
    
    self.cedula = input("Digite su CC o TI: ")
    comprobarId = self.cedula.isdigit()
    cont = 0
    for i in self.cedula:
      cont = cont + 1
    while cont < 10 or cont > 10: 
      print("La identificacion debe ser de 10 digitos")
      self.cedula = input("Digite su CC o TI: ")
      cont=0
      for i in self.cedula:
       cont = cont + 1
    while comprobarId != True:
      print("Debe digitar solo numeros")
      self.cedula = input("Digite su CC o TI: ")
      
	       
    
class Usuario(Persona):
  def init(self): 
    pass
  def Ussr(self):

#Preguntas
#Smoke
    print(" ")
    print("--------------------------------------------------")
    print(" ")
    print("Digite 1 para NO y 0 para SI: ")
    self.smoke=(input("¿Usted fuma? --> "))
    while (self.smoke.isdigit() == False):
     print("Solo debe digitar numeros")
     self.smoke= input("¿Usted fuma? --> ")
    self.smoke=int(self.smoke)
    while self.smoke>1:
      print("NO VALIDO, solo numero 1 y 0")
      self.smoke=input("¿Usted fuma? --> ")
      self.smoke=int(self.smoke) 
    if self.smoke==1:
      print(" ")
      print("Excelente :D")
    else:
      print("Esto disminuye las posibilidades de donar sangre")

#Genero
#Proteccion al tener relaciones

    print("--------------------------------------------------")
    print("")

    print("Digite 1 si es hombre, si es mujer digite 2")
    self.sexo=(input("--> "))
    while self.sexo.isdigit()==False:
      print("Solo debe digitar numeros")
      self.sexo=input("--> ")

    self.sexo=int(self.sexo)
    while self.sexo<1 or self.sexo>2:
      print("NO VALIDO, solo es valido el 1 y 2")
      self.sexo=input("--> ")
      self.sexo=int(self.sexo)

    if self.sexo==1:
      print("Digite (si) ,si usa protección de lo contrario digite cualquier otra letra")
      self.condon=input("¿Usa protección al tener relaciones sexuales? --> ")
      while self.condon.isalpha()==False:
        print("Opcción no valida, solo digite letras")
        self.condon=input("¿Usa protección al tener relaciones sexuales? --> ")
      self.condon=str(self.condon)
      if self.condon=="si":

       print(" ")
       print("Excelente :D")
      else:
       print(" ")
       print("Uselo, es por su bien ;)")

    if self.sexo==2:


#Metodos anticonceptivos
      print(" ")
      print("--------------------------------------------------")
      print("Digite si, si una metodos anticonceptivos, de lo contrario digite cualquier letra")
      self.metodo=input("¿Usa metodos anticonceptivos?,ejm: pastillas, inyección, diagramas,etc... --> ")
      while self.metodo.isalpha()==False:
        print("Opcción no valida,solo letras")
        self.metodo=input("¿Usa metodos anticonceptivos?,ejm: pastillas, inyección, vasectomia, etc... --> ")
      self.metodo=str(self.metodo)
      if self.metodo=="si":
        print(" ")
        print("EXCELENTE")
      else:
        print(" ")
        print("Se le recomienda el uso de metodos anticonceptivos")

#Alcohol
        
    print("--------------------------------------------------")
    print("Digite 1 para NO y 0 para SI")
    self.drink=input("¿Usted ha tomado alcohol en los ultimos cincos días? ")
    while self.drink.isdigit()==False:
      print("Solo debe digitar numeros")
      self.drink=input("¿Usted ah toma alcohol en estas dos ultimas semanas? ")
    self.drink=int(self.drink)
    while self.drink>1:
      print("NO VALIDO, solo es valido el 0 y el 1")
      self.drink=input("¿Usted ah toma alcohol en estas dos ultimas semanas? ")
      self.drink=int(self.drink)
    if self.drink==1:
      print(" ")
      print("Excelente :D")
    else:
      print(" ")
      print("Disminuye las posibilidades de donar D:")

#Cirugia  
  
    print("--------------------------------------------------")
    print("Digite 1 si no tiene cirugias recientes (no mas de 2 meses), de lo contrario digite 0")
    self.cirugias=input("¿Tiene cirugias? ")
    while self.cirugias.isdigit()==False: 
      print("Solo debe digitar numeros")
      self.cirugias=input("¿Tiene cirugias? ")
    self.cirugias=int(self.cirugias)
    while self.cirugias>1:
      print("NO VALIDO, solo es valido el 0 y el 1")
      self.cirugias=input("¿Tiene cirugias?")
      self.cirugias=int(self.cirugias)
    if self.cirugias==1:
      print(" ")
      print("Excelente :D")
    else:
      print(" ")
      print("Disminuye las posibilidades de donar D:")

#Promedio 
    
    suma=0 
    suma=self.smoke+self.drink+self.cirugias 
    promedio=(suma)/3 

    print("--------------------------------------------------")
    if promedio<0.5:
      print(" ")
      print("NO PUEDE DONAR SANGRE")
    if promedio>0.5:
      print(" ")
      print("HASTA EL MOMENTO ES FAVORABLE PARA DONAR SANGRE")
      print(" ")
      print("--------------------------------------------------") 

#Tatuajes
      print(" ")
      print("Digite 1 si no se ha hecho tatuajes en el ultimo año, de lo contrario digite 0")
      self.tatto=input("¿Tiene tatuajes? ")
      while self.tatto.isdigit()==False:
       print("Solo debe digitar numeros")
       self.tatto=input("¿Tiene tatuajes? ")
      self.tatto=int(self.tatto)
      while self.tatto>1:
        print(" ")
        print("NO VALIDO, solo es valido el 0 y el 1")
        print(" ")
        self.tatto=input("¿Tiene tatuajes?")
        self.tatto=int(self.tatto)
      if self.tatto==1:

#Puede o no donar sangre
       print(" ")
       print("EXCELENTE, USTED PUEDE DONAR SANGRE!:D")
      else:
       print(" ")
       print("NO PUEDE DONAR SANGRE")
       print("--------------------------------------------------")
#Se crean los objetos de la clase Persona, Usuario y metodos.
x=Persona()
x.Registro()
x=Usuario()
x.Ussr()



