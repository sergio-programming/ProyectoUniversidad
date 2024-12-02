from database import getDatabaseConnection

class Estudiante:
    def __init__(self, id: int, nombre: str, apellido: str, fecha_nacimiento: str, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        
class EstudianteDao:
    
    @staticmethod
    def create(estudiante: Estudiante):
        conexion = getDatabaseConnection()
        #Creamos un cursor que es un espacio para añadir setencias SQL
        cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion) VALUES ('{estudiante.nombre}', '{estudiante.apellido}', '{estudiante.fecha_nacimiento}', '{estudiante.genero}', '{estudiante.email}', '{estudiante.telefono}', '{estudiante.direccion}')")
        #Con el .commit comprometemos los cambios que se hicieron en esta conexion.
        #Con esto los cambios quedan persistentes en la base de datos
        conexion.commit()
        #Cerramos el cursor y la conexion a la base de datos
        cursor.close()
        conexion.close()
        
     
    @staticmethod    
    def read(id: int):
        conexion = getDatabaseConnection()
        #Creamos un cursor que es un espacio para añadir setencias SQL
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM estudiantes WHERE id = {id}")
        #fetchone es un metodo para trabajar con bases de datos
        #Lo que hace es devolver una fila de una consulta SQL
        #La variable result alamacena el resultado de la consulta
        result = cursor.fetchone()
        #Cerramos el cursor y la conexion a la base de datos
        cursor.close()
        conexion.close()
        if result is None:
            return None
        else:
            return Estudiante(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
                 
    @staticmethod
    def readAll():
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        results = cursor.fetchall()
        cursor.close()
        conexion.close()
        estudiantes = []
        for result in results:
            estudiante = Estudiante(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
            estudiantes.append(estudiante)
        return estudiantes
    
    @staticmethod
    def update(estudiante: Estudiante):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"""
                       UPDATE estudiantes
                        SET nombre = '{estudiante.nombre}',
                           apellido = '{estudiante.apellido}',
                           fecha_nacimiento = '{estudiante.fecha_nacimiento}',
                           genero = '{estudiante.genero}',
                           email = '{estudiante.email}',
                           telefono = '{estudiante.telefono}',
                           direccion = '{estudiante.direccion}' 
                        WHERE id = {estudiante.id}
                       """)
        conexion.commit()
        cursor.close()
        conexion.close()
    
    @staticmethod
    def delete(id: int):
        conexion = getDatabaseConnection()
        cursor = conexion.cursor()
        cursor.execute(f"DELETE from estudiantes WHERE id = {id}")
        conexion.commit()
        cursor.close()
        conexion.close()  