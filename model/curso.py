from database import getDatabaseConnection

class Curso:
    def __init__(self, id: int, nombre: str, descripcion: str, creditos: int, programa_id: int):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.programa_id = programa_id
        
class CursoDao:
    
    @staticmethod
    def create(curso: Curso):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO cursos (nombre, descripcion, creditos, programa_id) VALUES ('{curso.nombre}', '{curso.descripcion}', {curso.creditos}, {curso.programa_id})")
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod    
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM cursos WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result is None:
            return None
        return Curso(result[0], result[1], result[2], result[3], result[4])
    
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cursos")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        cursos = []
        for result in results:
            curso = Curso(result[0], result[1], result[2], result[3], result[4])
            cursos.append(curso)
        return cursos
    
    @staticmethod
    def update(curso: Curso):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE cursos
                        SET nombre = {curso.nombre},
                        SET descripcion = {curso.descripcion},
                        SET creditos = {curso.creditos},
                        SET programa_id = {curso.programa_id}
                       WHERE id = {curso.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM cursos WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()
        