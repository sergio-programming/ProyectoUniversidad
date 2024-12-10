from model.curso import Curso, CursoDao

class CursoController:
    
    def registerCurso(nombre, descripcion, creditos, programa_id):
        curso = Curso(id, nombre, descripcion, creditos, programa_id)
        CursoDao.create(curso)
        
    def getAllCursos():
        cursos = []
        cursos = CursoDao.readAll()
        return cursos
    
    def getCursoById(id):
        curso = CursoDao.read(id)
        return curso
    
    def updateCurso(id, nombre, descripcion, creditos, programa_id):
        curso = Curso(id, nombre, descripcion, creditos, programa_id)
        CursoDao.update(curso)
        
    def deleteCurso(id):
        CursoDao.delete(id)