from model.profesor import Profesor, ProfesorDao

class ProfesorController:
    
    def registerProfesor(nombre, apellido, email, telefono, facultad_id):
        profesor = Profesor(nombre, apellido, email, telefono, facultad_id)
        ProfesorDao.create(profesor)
        
    
    def getAllProfesores():
        profesores = []
        profesores = ProfesorDao.getAll()
        return profesores
    
    def getProfesorById(id):
        profesor = ProfesorDao.get(id)
        return profesor
    
    def updateProfesor(id, nombre, apellido, email, telefono, facultad_id):
        profesor = Profesor(id, nombre, apellido, email, telefono, facultad_id)
        ProfesorDao.update(profesor)
    
    def deleteProfesor(id):
        ProfesorDao.delete(id)