import mysql.connector

class registro_datos():
    
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost', database ='base_datos', user = 'root', password ='admin')
        



def inserta_paciente(self, nombre, edad, genero, documento, correo_electronico, donar):
        cur = self.conexion.cursor()
        sql='''INSERT INTO insertar_paciente(self,nombre,edad,genero,correo_electronico,donar)
        VALUES('{}', '{}','{}', '{}','{}')'''.format(nombre,edad,genero,correo_electronico,donar)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

def mostrar_paciente(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

def busca_paciente(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

def elimina_paciente(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()





















