from view.facultad import Facultad, FacultadDao

class FacultadController:
    
    def registerFacultad(nombre):
        facultad = Facultad(nombre)
        FacultadDao.create(facultad)
        
    def getAllFacultades():
        facultades = []
        facultades = FacultadDao.readAll()
        return facultades
    
    def getFacultadById(id):
        facultad = FacultadDao.read(id)
        return facultad
    
    def updateFacultad(id, nombre):
        facultad = Facultad(id, nombre)
        FacultadDao.update(facultad)
        
    def deleteFacultad(id):
        FacultadDao.delete(id)