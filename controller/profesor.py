from model.profesor import Profesor, ProfesorDao

class ProfesorController:
    
    def registerProfesor(nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id):
        profesor = Profesor(nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id)
        ProfesorDao.create(profesor)
        
    
    def getAllProfesores():
        profesores = []
        profesores = ProfesorDao.readAll()
        return profesores
    
    def getProfesorById(id):
        profesor = ProfesorDao.read(id)
        return profesor
    
    def updateProfesor(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id):
        profesor = Profesor(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id)
        ProfesorDao.update(profesor)
    
    def deleteProfesor(id):
        ProfesorDao.delete(id)