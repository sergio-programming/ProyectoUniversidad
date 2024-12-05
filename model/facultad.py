from database import getDatabaseConnection

class Facultad:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        
class FacultadDao:
    
    @staticmethod
    def create(facultad: Facultad):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO facultades (nombre) VALUES ('{facultad.nombre}')")
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM facultades WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result == None:
            None
        else:
            return Facultad(result[0], result[1])
    
    @staticmethod    
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM facultades")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        facultades = []
        for result in results:
            facultad = Facultad(result[0], result[1])
            facultades.append(facultad)
        return facultades
    
    @staticmethod
    def update(facultad: Facultad):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE facultades
                        SET nombre = {facultad.nombre}
                        WHERE id = {facultad.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod    
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM facultades WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()