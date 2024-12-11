from controller.programa import ProgramaController
from controller.facultad import FacultadController

def menuProgramas():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION DE PROGRAMAS")
        print("#"*30)
        print("""1. Registro de programas.
2. Consultar datos de un programa.
3. Visualizar programas registrados.
4. Actualizar datos de programas registrados.
5. Eliminar registro de programas.
6. Volver al menú principal.""")
    
    
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarPrograma()
        
            elif opcion == 2:
                consultarPrograma()
        
            elif opcion == 3:
                visualizarProgramas()
        
            elif opcion == 4:
                actualizarPrograma()
        
            elif opcion == 5:
                eliminarPrograma()
        
            elif opcion == 6:
                break
        
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")    
    
    
def registrarPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE PROGRAMAS")
    print("#"*30)
    nombre = input("\nIngrese el nombre del programa: ")
    while True:
        try:
            facultad_id = int(input("Ingrese el id de la facultad a la que pertenece el programa: "))
            facultad = FacultadController.getFacultadById(facultad_id)
            if facultad is None:
                raise Exception("No existe una facultad con el numero de id ingresado. Por favor intente de nuevo.")
            break
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
        except Exception as e:
            print(f"\n{e}")
            input("Presione <Enter> para continuar")
    ProgramaController.registerPrograma(nombre, facultad_id)
    
def visualizarProgramas():
    programas = []
    programas = ProgramaController.getAllProgramas()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE PROGRAMAS")
    print("#"*30)
    for i, programa in enumerate(programas, start=1):
        print(f"""\nPROGRAMA #{i}
              Id: {programa.id}
              Nombre de Programa: {programa.nombre}
              Id de Facultad: {programa.facultad_id}""")
        
def consultarPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE PROGRAMA")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del programa a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        programa = ProgramaController.getProgramaById(id)
        if programa is None:
            print("\nNo existe un programa con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos del programa:
                  Id: {programa.id}
                  Nombre del Programa: {programa.nombre}
                  Id de Facultad: {programa.facultad_id}""")
            
def actualizarPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE PROGRAMA")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id del programa a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    programa = ProgramaController.getProgramaById(id)
    
    if programa is None:
        print("\nNo existe un programa con el numero de ID ingresado")
        input("Presione <Enter> para continuar")
        return
    else:
        nombre = input("Ingrese el nombre del programa: ")
        if nombre == "":
            nombre = programa.nombre   
        while True:
            try:
                facultad_id = int(input("Ingrese el id de la facultad a la que pertenece el programa: "))
                facultad = FacultadController.getFacultadById(facultad_id)
                if facultad is None:
                    raise Exception("\nLa facultad con el numero de id ingresado no existe. Por favor intente de nuevo.")
                break
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            except Exception as e:
                print(f"\n{e}")
                input("Presione <Enter> para continuar")
        ProgramaController.updatePrograma(id, nombre, facultad_id)
        

def eliminarPrograma():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE PROGRAMA")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del programa a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        programa = ProgramaController.getFacultadById(id)
        if programa == None:
            print("\nNo existe un programa con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            ProgramaController.deletePrograma(id)  