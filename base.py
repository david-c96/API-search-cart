
import bcrypt 
import mysql.connector
from mysql.connector import Error
# base
def hash_password(password: str) -> str:
    """Hashea la contraseña usando bcrypt."""
    salt = bcrypt.gensalt()
    passwords = bcrypt.hashpw(password.encode('utf-8'), salt)
    return passwords.decode('utf-8')

def check_password(stored_password: str, provided_password: str) -> bool:
    """Verifica la contraseña proporcionada contra el hash almacenado."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

config = {
    "host": "127.0.0.1",
    "port": "3306",
    "database": "data_ursers",
    "user": "root",
    "password": "tiger9605"
    }


def store_user(usre: str, passwords: str, ):
    """Almacena un nuevo usuario con su contraseña hasheada en la base de datos."""
    
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "INSERT INTO usre (usre, passwords) VALUES (%s, %s)"
        cursor.execute(query, (usre, passwords))
        connection.commit()
        print("Usuario almacenado correctamente.")
    except Error as e:
        print("Error al almacenar usuario:", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def retrieve_user(usre: str) -> str:
    """Recupera el hash de la contraseña para un usuario dado."""
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = "SELECT passwords FROM usre WHERE usre = %s"
        cursor.execute(query, (usre,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            print("Usuario no encontrado.")
            return None
    except Error as e:
        print("Error al recuperar usuario:", e)
        return None
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()




def insert( model, part, serial, car, year, color, version):

        try:
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            query = "INSERT INTO part (model, part, serial, car, year, color, version) VALUES (%s, %s, %s, %s, %s, %s, %s  )"
            cursor.execute(query, (model, part, serial, car, year, color, version))
            connection.commit()
            print("Correcto al almacenar")
        except Error as e:
            print("Error al almacenar:", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


def search(model):

        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = f"SELECT * FROM data_ursers.part WHERE model IN ('{model}')"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in result:
            if row:
                print(row)
            else:
                print("Modelo no encontrado.")
                cursor.close()
                connection.close()   

def eliminate(eliminates):

        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = f"DELETE FROM data_ursers.part WHERE serial IN ({eliminates})"
        cursor.execute(query,)
        connection.commit()
        connection.is_connected
        cursor.close()
        connection.close()  