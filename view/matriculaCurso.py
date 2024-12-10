from controller.matriculaCurso import MatriculaCursoController
from controller.estudiante import EstudianteController
from controller.curso import CursoController

def menuCursos():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION DE MATRICULAS DE CURSOS")
        print("#"*30)
        print("""1. Registro de matriculas de cursos.
2. Consultar datos de una matricula.
3. Visualizar matriculas registradas.
4. Actualizar datos de matriculas registradas.
5. Eliminar registro de matriculas.
6. Volver al menú principal.""")
    
    
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarMatriculaCurso()
        
            elif opcion == 2:
                consultarMatriculaCurso()
        
            elif opcion == 3:
                visualizarMatriculasCursos()
        
            elif opcion == 4:
                actualizarMatriculaCurso()
        
            elif opcion == 5:
                eliminarMatriculaCurso()
        
            elif opcion == 6:
                break
        
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")    
    
    
def registrarMatriculaCurso():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE MATRICULAS DE CURSOS")
    print("#"*30)
    while True:
        try:
            estudiante_id = int(input("Ingrese el id del estudiante a matricular: "))
            estudiante = EstudianteController.getEstudianteById(estudiante_id)
            if estudiante is None:
                raise Exception("No existe un estudiante con el numero de id ingresado. Por favor intente de nuevo.")
            break
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
        except Exception as e:
            print(f"\n{e}")
            input("Presione <Enter> para continuar")
    
    while True:
        try:
            curso_id = int(input("Ingrese el id del curso al que pertenece el curso: "))
            curso = CursoController.getCursoById(curso_id)
            if curso is None:
                raise Exception("No existe un curso con el numero de id ingresado. Por favor intente de nuevo.")
            break
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
        except Exception as e:
            print(f"\n{e}")
            input("Presione <Enter> para continuar")
            
    fecha_matricula = input("Ingrese la fecha en que se efectuo la matricula: ")   
    MatriculaCursoController.registerMatriculaCurso(estudiante_id, curso_id, fecha_matricula)
    
def visualizarMatriculasCursos():
    matriculasCursos = []
    matriculasCursos = MatriculaCursoController.getAllMatriculasCursos()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE MATRICULAS DE CURSOS")
    print("#"*30)
    for i, matriculaCurso in enumerate(matriculasCursos, start=1):
        print(f"""\nMATRICULA #{i}
              Id: {matriculaCurso.id}
              Id del Estudiante: {matriculaCurso.estudiante_id}
              Id del Curso: {matriculaCurso.curso_id}
              Fecha de Matricula: {matriculaCurso.fecha_matricula}""")
        
def consultarMatriculaCurso():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE MATRICULA DE CURSO")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la matricula a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        matriculaCurso = MatriculaCursoController.getMatriculaCursoById(id)
        if matriculaCurso is None:
            print("\nNo existe una matricula con el numero de ID ingresado. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos de la matricula:
                  Id: {matriculaCurso.id}
                  Id del Estudiante: {matriculaCurso.estudiante_id}
                  Id del Curso: {matriculaCurso.curso_id}
                  Fecha de Matricula: {matriculaCurso.fecha_matricula}""")
            
def actualizarMatriculaCurso():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE MATRICULA DE CURSO")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id de la matricula a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    matriculaCurso = MatriculaCursoController.getMatriculaCursoById(id)
    
    if matriculaCurso is None:
        print("\nNo existe una matricula con el numero de ID ingresado. Por favor intente de nuevo.")
        input("Presione <Enter> para continuar")
        return
    else:
        while True:
            try:
                estudiante_id = int(input("Ingrese el id del estudiante a matricular: "))
                estudiante = EstudianteController.getEstudianteById(estudiante_id)
                if estudiante is None:
                    raise Exception("No existe un estudiante con el numero de id ingresado. Por favor intente de nuevo.")
                break
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            except Exception as e:
                print(f"\n{e}")
                input("Presione <Enter> para continuar")
    
        while True:
            try:
                curso_id = int(input("Ingrese el id del curso al que pertenece el curso: "))
                curso = CursoController.getCursoById(curso_id)
                if curso is None:
                    raise Exception("No existe un curso con el numero de id ingresado. Por favor intente de nuevo.")
                break
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            except Exception as e:
                print(f"\n{e}")
                input("Presione <Enter> para continuar")
            
        fecha_matricula = input("Ingrese la fecha en que se efectuo la matricula: ")
        MatriculaCursoController.updateMatriculaCurso(id, estudiante_id, curso_id, fecha_matricula)
        

def eliminarMatriculaCurso():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE MATRICULA DE CURSO")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la matricula a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        matriculaCurso = MatriculaCursoController.getMatriculaCursoById(id)
        if matriculaCurso is None:
            print("\nNo existe una matricula con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            MatriculaCursoController.deleteMatriculaCurso(id)