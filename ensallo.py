
'''
Clase (gestor de contexto con los métodos mágicos __enter__ y __exit__) para la conexión a MySQL
'''

import mysql.connector as mysql #Conector específico para MySQL

class MySQL:

    SERVIDOR = 'localhost' #Atributos de clase privados (no se ha de acceder a ellos desde fuera de la clase) para definir la instancia de conexión
    USUARIO = 'root'
    CONTRASENA = 'tiger9605'
    BASE_DATOS = 'data_ursers'

    @classmethod
    def __enter__(self): #Método que se invoca al comenzar la declaración "with"

        self.conexion = mysql.connect(self.SERVIDOR, self.USUARIO, self.CONTRASENA, self.BASE_DATOS, ) #Se crea la conexión ("**" indica que se trata de un diccionario)
        self.cursor = self.conexion.cursor() #Y a partir de ella, el cursor, que es el que ejecuta las consultas sobre la BD
        return self.cursor

