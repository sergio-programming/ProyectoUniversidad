from mysql.connector import connect

def getDatabaseConnection():
    return connect(
        host = "localhost",
        user = "root",
        password = "admin",
        database = "gestion_universidad"
    )

