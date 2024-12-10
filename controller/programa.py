from model.programa import Programa, ProgramaDao

class ProgramaController:
    
    def registerPrograma(nombre, facultad_id):
        programa = Programa(id, nombre, facultad_id)
        ProgramaDao.create(programa)
        
    def getAllProgramas():
        programas = []
        programas = ProgramaDao.readAll()
        return programas
    
    def getProgramaById(id):
        programa = ProgramaDao.read(id)
        return programa
    
    def updatePrograma(id, nombre, facultad_id):
        programa = Programa(id, nombre, facultad_id)
        ProgramaDao.update(programa)
        
    def deletePrograma(id):
        ProgramaDao.delete(id)