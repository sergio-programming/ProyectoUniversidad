from controller.facultad import FacultadController

def menuFacultades():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION DE FACULTADES")
        print("#"*30)
        print("""1. Registro de facultades.
2. Consultar datos de una facultad.
3. Visualizar facultades registradas.
4. Actualizar datos de facultades registradas.
5. Eliminar registro de facultades.
6. Volver al menú principal.""")
    
    
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarFacultad()
        
            elif opcion == 2:
                consultarFacultad()
        
            elif opcion == 3:
                visualizarFacultades()
        
            elif opcion == 4:
                actualizarFacultad()
        
            elif opcion == 5:
                eliminarFacultad()
        
            elif opcion == 6:
                break
        
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")    
    
    
def registrarFacultad():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE FACULTADES")
    print("#"*30)
    nombre = input("\nIngrese el nombre de la facultad: ")
    FacultadController.registerFacultad(nombre)
    
def visualizarFacultades():
    facultades = []
    facultades = FacultadController.getAllFacultades()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE FACULTADES")
    print("#"*30)
    for i, facultad in enumerate(facultades, start=1):
        print(f"""\nFACULTAD #{i}
              Id: {facultad.id}
              Nombre de Facultad: {facultad.nombre}""")
        
def consultarFacultad():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE FACULTAD")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la facultad a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        facultad = FacultadController.getFacultadById(id)
        if facultad == None:
            print("\nNo existe una facultad con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos de la facultad:
                  Id: {facultad.id}
                  Nombre de Facultad: {facultad.nombre}""")
            
def actualizarFacultad():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE FACULTAD")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id de la facultad a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    facultad = FacultadController.getFacultadById(id)
    
    if facultad == None:
        print("\nNo existe un estudiante con el numero de ID ingresado")
        input("Presione <Enter> para continuar")
        return
    else:
        nombre = input("Ingrese el nombre de la facultad: ")
        if nombre == "":
            nombre = facultad.nombre        
        FacultadController.updateFacultad(id, nombre)
        

def eliminarFacultad():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE FACULTAD")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id de la facultad a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        facultad = FacultadController.getFacultadById(id)
        if facultad == None:
            print("\nNo existe una facultad con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            FacultadController.deleteFacultad(id)        