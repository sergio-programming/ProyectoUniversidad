from model.matriculaCurso import MatriculaCurso, MatriculaCursoDao

class MatriculaCursoController:
    
    def registerMatriculaCurso(estudiante_id, curso_id, fecha_matricula):
        matriculaCurso = MatriculaCurso(id, estudiante_id, curso_id, fecha_matricula)
        MatriculaCursoDao.create(matriculaCurso)
        
    def getAllMatriculasCursos():
        matriculasCursos = []
        matriculasCursos = MatriculaCursoDao.readAll()
        return matriculasCursos
    
    def getMatriculaCursoById(id):
        matriculaCurso = MatriculaCursoDao.read(id)
        return matriculaCurso
    
    def updateMatriculaCurso(id, estudiante_id, curso_id, fecha_matricula):
        matriculaCurso = MatriculaCurso(id, estudiante_id, curso_id, fecha_matricula)
        MatriculaCursoDao.update(matriculaCurso)
        
    def deleteMatriculaCurso(id):
        MatriculaCursoDao.delete(id)
    
        