from mysql.connector import connect, Error

def getDatabaseConnection():
    try:
        return connect(
            host="localhost",
            user="root",
            password="admin",
            database="gestion_universidad",
            port=3306
        )
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        raise
