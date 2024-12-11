from controller.matriculaPrograma import MatriculaProgramaController
from controller.estudiante import EstudianteController
from controller.programa import ProgramaController

def menuMatriculasProgramas():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION DE MATRICULAS DE PROGRAMAS")
        print("#"*30)
        print("""1. Registro de matriculas de programas.
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
                registrarMatriculaPrograma()
        
            elif opcion == 2:
                consultarMatriculaPrograma()
        
            elif opcion == 3:
                visualizarMatriculasProgramas()
        
            elif opcion == 4:
                actualizarMatriculaPrograma()
        
            elif opcion == 5:
                eliminarMatriculaPrograma()
        
            elif opcion == 6:
                break
        
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")    
    
    
def registrarMatriculaPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE MATRICULAS DE PROGRAMAS")
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
            programa_id = int(input("Ingrese el id del programa al cual se va a matricular: "))
            programa = ProgramaController.getProgramaById(programa_id)
            if programa is None:
                raise Exception("No existe un programa con el numero de id ingresado. Por favor intente de nuevo.")
            break
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
        except Exception as e:
            print(f"\n{e}")
            input("Presione <Enter> para continuar")
            
    fecha_matricula = input("Ingrese la fecha en que se efectuo la matricula: ")   
    MatriculaProgramaController.registerMatriculaPrograma(estudiante_id, programa_id, fecha_matricula)
    
def visualizarMatriculasProgramas():
    matriculasProgramas = []
    matriculasProgramas = MatriculaProgramaController.getAllMatriculasProgramas()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE MATRICULAS DE PROGRAMAS")
    print("#"*30)
    for i, matriculaPrograma in enumerate(matriculasProgramas, start=1):
        print(f"""\nMATRICULA #{i}
              Id: {matriculaPrograma.id}
              Id del Estudiante: {matriculaPrograma.estudiante_id}
              Id del Programa: {matriculaPrograma.programa_id}
              Fecha de Matricula: {matriculaPrograma.fecha_matricula}""")
        
def consultarMatriculaPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE MATRICULA DE PROGRAMA")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la matricula a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        matriculaPrograma = MatriculaProgramaController.getMatriculaProgramaById(id)
        if matriculaPrograma is None:
            print("\nNo existe una matricula con el numero de ID ingresado. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos de la matricula:
                  Id: {matriculaPrograma.id}
                  Id del Estudiante: {matriculaPrograma.estudiante_id}
                  Id del Programa: {matriculaPrograma.programa_id}
                  Fecha de Matricula: {matriculaPrograma.fecha_matricula}""")
            
def actualizarMatriculaPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE MATRICULA DE PROGRAMA")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id de la matricula a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    matriculaPrograma = MatriculaProgramaController.getMatriculaProgramaById(id)
    
    if matriculaPrograma is None:
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
                programa_id = int(input("Ingrese el id del programa al cual se va a matricular: "))
                programa = ProgramaController.getProgramaById(programa_id)
                if programa is None:
                    raise Exception("No existe un programa con el numero de id ingresado. Por favor intente de nuevo.")
                break
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            except Exception as e:
                print(f"\n{e}")
                input("Presione <Enter> para continuar")
            
        fecha_matricula = input("Ingrese la fecha en que se efectuo la matricula: ")
        MatriculaProgramaController.updateMatriculaPrograma(id, estudiante_id, programa_id, fecha_matricula)
        

def eliminarMatriculaPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE MATRICULA DE PROGRAMA")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la matricula a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        matriculaPrograma = MatriculaProgramaController.getMatriculaProgramaById(id)
        if matriculaPrograma is None:
            print("\nNo existe una matricula con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            MatriculaProgramaController.deleteMatriculaPrograma(id)