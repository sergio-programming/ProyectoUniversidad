from datetime import date
from database import getDatabaseConnection

class MatriculaCurso:
    def __init__(self, id: int, estudiante_id: int, curso_id: int, fecha_matricula: date):
        self.id = id
        self.estudiante_id = estudiante_id
        self.curso_id = curso_id
        self.fecha_matricula = fecha_matricula
    

class MatriculaCursoDao:
    
    @staticmethod
    def create(matriculaCurso: MatriculaCurso):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO matriculasCursos VALUES ({matriculaCurso.estudiante_id}, {matriculaCurso.curso_id}, '{matriculaCurso.fecha_matricula}')")
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod    
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM matriculasCursos WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result is None:
            return None
        return MatriculaCurso(result[0], result[1], result[2], result[3])
    
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM matriculasCursos")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        matriculasCursos = []
        for result in results:
            matriculaCurso = MatriculaCurso(result[0], result[1], result[2], result[3])
            matriculasCursos.append(matriculaCurso)
        return matriculasCursos
    
    @staticmethod
    def update(matriculaCurso: MatriculaCurso):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE matriculasCursos
                        SET estudiante_id = {matriculaCurso.estudiante_id},
                        SET curso_id = {matriculaCurso.curso_id},
                        SET fecha_matricula = '{matriculaCurso.fecha_matricula}'
                       WHERE id = {matriculaCurso.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
        
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM matriculasCursos WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()
        