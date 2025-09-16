
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
        return
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
        return result

def general_search(general_search):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    conditions = []
    values = []
    for key, value in general_search.items():
            if key in ["Model", "Part", "Serial", "Car", "Year", "Color", "Version"]:
                conditions.append(f"{key} = %s")
                values.append(value)
    if not conditions:
            return []  

    sql = f"SELECT * FROM `data_ursers`.`part` WHERE {' AND '.join(conditions)}"
    cursor.execute(sql, values)
    results = cursor.fetchall()
    return results


def eliminate(eliminates):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        
        if isinstance(eliminates, str):
            eliminates_list = [eliminates]
        elif isinstance(eliminates, (list, tuple)):
            eliminates_list = list(eliminates)
        else:
            return

        placeholders = ', '.join(['%s'] * len(eliminates_list))
        query = f"DELETE FROM data_ursers.part WHERE serial IN ({placeholders})"

        cursor.execute(query, tuple(eliminates_list))
        connection.commit()

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()