from model.estudiante import Estudiante, EstudianteDao

class EstudianteController:
    
    def registerEstudiante(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion):
        estudiante = Estudiante(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)
        EstudianteDao.create(estudiante)
        
    
    def getAllEstudiantes():
        estudiantes = []
        estudiantes = EstudianteDao.readAll()
        return estudiantes
    
    def getEstudianteById(id):
        estudiante = EstudianteDao.read(id)
        return estudiante
    
    def updateEstudiante(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion):
        estudiante = Estudiante(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)
        EstudianteDao.update(estudiante)
    
    def deleteEstudiante(id):
        EstudianteDao.delete(id)