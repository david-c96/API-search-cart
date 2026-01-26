
import bcrypt 
import mysql.connector
from mysql.connector import Error
# base

# bcrypt de la contraseña
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    passwords = bcrypt.hashpw(password.encode('utf-8'), salt)
    return passwords.decode('utf-8')

# Verifica la contraseña
def check_password(stored_password: str, provided_password: str) -> bool:
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

# Configuración de la conexión a la base de datos
config = {
    "host": "127.0.0.1",
    "port": "3306",
    "database": "data_ursers",
    "user": "root",
    "password": "tiger9605"
    }

# Almacena un nuevo usuario en la base de datos
def store_user(usre: str, passwords: str, ):
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


# Recupera el hash de la contraseña para un usuario dado
def retrieve_user(usre: str) -> str:
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



# insertar datos en la base de datos
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

# buscar datos en la base de datos
def search(model):
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        query = f"SELECT * FROM data_ursers.part WHERE model IN ('{model}')"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

# búsqueda general en la base de datos
def general_search(general_search):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    conditions = []
    values = []
    for key, value in general_search.items():
            if key in ["Model", "Part", "Serial", "Car", "Year", "Color", "Version"]:
                conditions.append(f"{key} LIKE %s")
                values.append(f"%{value}%")
    if not conditions:
            return []  

    sql = f"SELECT * FROM `data_ursers`.`part` WHERE {' OR '.join(conditions)}"
    cursor.execute(sql, values)
    results = cursor.fetchall()
    return results

# eliminar datos en la base de datos
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