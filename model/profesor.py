from database import getDatabaseConnection

class Profesor:
    def __init__(self, id: int, nombre: str, apellido: str, fecha_nacimiento: str, genero: str, email: str, telefono: str, facultad_id: int):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.facultad_id = facultad_id
    
class ProfesorDao:
    
    @staticmethod
    def create(profesor: Profesor):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO profesores (nombre, apellido, fecha_nacimiento, genero, email, telefono, departamento_id) VALUES ('{profesor.nombre}', '{profesor.apellido}', '{profesor.fecha_nacimiento}', '{profesor.genero}' '{profesor.email}', '{profesor.telefono}', {profesor.facultad_id})")
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    def read(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM profesores WHERE id = {id}")
        result = cursor.fetchone()
        cursor.close()
        conexion.close()
        if result == None:
            return None
        else:
            return Profesor(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
    
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesores")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        profesores = []
        for result in results:
            profesor = Profesor(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
            profesores.append(profesor)
        return profesores
    
    @staticmethod
    def update(profesor: Profesor):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE profesores
                        SET nombre = '{profesor.nombre}',
                            apellido = '{profesor.apellido}',
                            fecha_nacimiento = '{profesor.fecha_nacimiento}',
                            genero = '{profesor.genero}',
                            email = '{profesor.email}',
                            telefono = '{profesor.telefono}',
                            departamento_id = {profesor.facultad_id}
                        WHERE id = {profesor.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM profesores WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()
        