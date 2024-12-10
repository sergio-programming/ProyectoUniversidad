from datetime import date
from database import getDatabaseConnection

class MatriculaPrograma:
    def __init__(self, id: int, estudiante_id: int, programa_id: int, fecha_matricula: date):
        self.id = id
        self.estudiante_id = estudiante_id
        self.programa_id = programa_id
        self.fecha_matricula = fecha_matricula
    

class MatriculaProgramaDao:
    
    @staticmethod
    def create(matriculaPrograma: MatriculaPrograma):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO matriculasProgramas VALUES ({matriculaPrograma.estudiante_id}, {matriculaPrograma.programa_id}, '{matriculaPrograma.fecha_matricula}')")
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod    
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM matriculasProgramas WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result is None:
            return None
        return MatriculaPrograma(result[0], result[1], result[2], result[3])
    
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM matriculasProgramas")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        matriculasProgramas = []
        for result in results:
            matriculaPrograma = MatriculaPrograma(result[0], result[1], result[2], result[3])
            matriculasProgramas.append(matriculaPrograma)
        return matriculasProgramas
    
    @staticmethod
    def update(matriculaPrograma: MatriculaPrograma):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE matriculasProgramas
                        SET estudiante_id = {matriculaPrograma.estudiante_id},
                        SET programa_id = {matriculaPrograma.programa_id},
                        SET fecha_matricula = '{matriculaPrograma.fecha_matricula}'
                       WHERE id = {matriculaPrograma.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM matriculasProgramas WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()