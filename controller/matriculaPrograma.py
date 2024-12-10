from model.matriculaPrograma import MatriculaPrograma, MatriculaProgramaDao

class MatriculaCursoController:
    
    def registerMatriculaPrograma(estudiante_id, programa_id, fecha_matricula):
        matriculaPrograma = MatriculaPrograma(id, estudiante_id, programa_id, fecha_matricula)
        MatriculaProgramaDao.create(matriculaPrograma)
        
    def getAllMatriculasProgramas():
        matriculasProgramas = []
        matriculasProgramas = MatriculaProgramaDao.readAll()
        return matriculasProgramas
    
    def getMatriculaProgramaById(id):
        matriculaPrograma = MatriculaProgramaDao.read(id)
        return matriculaPrograma
    
    def updateMatriculaPrograma(id, estudiante_id, curso_id, fecha_matricula):
        matriculaPrograma = MatriculaPrograma(id, estudiante_id, curso_id, fecha_matricula)
        MatriculaProgramaDao.update(matriculaPrograma)
        
    def deleteMatriculaPrograma(id):
        MatriculaProgramaDao.delete(id)