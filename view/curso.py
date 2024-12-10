from controller.curso import CursoController
from controller.programa import ProgramaController

def menuCursos():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION DE CURSOS")
        print("#"*30)
        print("""1. Registro de cursos.
2. Consultar datos de un curso.
3. Visualizar cursos registrados.
4. Actualizar datos de cursos registrados.
5. Eliminar registro de cursos.
6. Volver al menú principal.""")
    
    
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarCurso()
        
            elif opcion == 2:
                consultarCurso()
        
            elif opcion == 3:
                visualizarCursos()
        
            elif opcion == 4:
                actualizarCurso()
        
            elif opcion == 5:
                eliminarCurso()
        
            elif opcion == 6:
                break
        
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")    
    
    
def registrarCurso():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE CURSOS")
    print("#"*30)
    nombre = input("\nIngrese el nombre del curso: ")
    descripcion = input("Ingrese la descripción del curso: ")
    while True:
        try:
            creditos = int(input("Ingrese el número de creditos del curso: "))
            break
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
    
    while True:
        try:
            programa_id = int(input("Ingrese el id del programa al que pertenece el curso: "))
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
    CursoController.registerCurso(nombre, descripcion, creditos, programa_id)
    
def visualizarCursos():
    cursos = []
    cursos = CursoController.getAllCursos()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE CURSOS")
    print("#"*30)
    for i, curso in enumerate(cursos, start=1):
        print(f"""\nCURSO #{i}
              Id: {curso.id}
              Nombre del Curso: {curso.nombre}
              Descripción del Curso: {curso.descripcion}
              Creditos del Curso: {curso.creditos}
              Id del programa: {curso.programa_id}""")
        
def consultarCurso():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE CURSO")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del curso a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        curso = CursoController.getCursoById(id)
        if curso is None:
            print("\nNo existe un curso con el numero de ID ingresado. Por favor intente de nuevo.")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos del curso:
                  Id: {curso.id}
                  Nombre del Curso: {curso.nombre}
                  Descripción del Curso: {curso.descripcion}
                  Creditos del Curso: {curso.creditos}
                  Id del programa: {curso.programa_id}""")
            
def actualizarCurso():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE CURSO")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id del curso a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    curso = CursoController.getCursoById(id)
    
    if curso == None:
        print("\nNo existe un curso con el numero de ID ingresado. Por favor intente de nuevo.")
        input("Presione <Enter> para continuar")
        return
    else:
        nombre = input("Ingrese el nombre del curso: ")
        if nombre == "":
            nombre = curso.nombre  
        descripcion = input("Ingrese la descripción del curso: ") 
        if descripcion == "":
            descripcion = curso.descripcion
        while True:
            try:
                creditos = int(input("Ingrese el número de creditos del curso: "))
                break
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
    
        while True:
            try:
                programa_id = int(input("Ingrese el id del programa al que pertenece el curso: "))
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
        CursoController.updateCurso(id, nombre, descripcion, creditos, programa_id)
        

def eliminarCurso():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE CURSO")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del curso a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        curso = CursoController.getCursoById(id)
        if curso == None:
            print("\nNo existe un curso con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            CursoController.deleteCurso(id)