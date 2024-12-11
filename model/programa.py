from database import getDatabaseConnection

class Programa:
    def __init__(self, id: int, nombre: str, facultad_id: int):
        self.id = id
        self.nombre = nombre
        self.facultad_id = facultad_id
        
class ProgramaDao:
    
    @staticmethod
    def create(programa: Programa):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO programas (nombre, facultad_id) VALUES ('{programa.nombre}', {programa.facultad_id})")
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM programas WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result is None:
            return None
        return Programa(result[0], result[1], result[2])
        
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM programas")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        programas = []
        for result in results:
            programa = Programa(result[0], result[1], result[2])
            programas.append(programa)
        return programas
    
    @staticmethod
    def update(programa: Programa):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE programas
                        SET nombre = {programa.nombre},
                        SET facultad_id = {programa.facultad_id}
                        WHERE id = {programa.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM programas WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()