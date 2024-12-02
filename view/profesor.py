from controller.profesor import ProfesorController

def menuProfesores():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION PROFESORES")
        print("#"*30)
        print("""1. Registro de profesores.
2. Consultar datos de un profesor.
3. Visualizar profesores registrados.
4. Actualizar datos de profesores registrados.
5. Eliminar registro de Profesores.
6. Volver al menú principal.""")
        
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarProfesor()
            
            elif opcion == 2:
                consultarProfesor()
            
            elif opcion == 3:
                visualizarProfesores()
            
            elif opcion == 4:
                pass
            
            elif opcion == 5:
                eliminarProfesor()
                pass
            
            elif opcion == 6:
                break
            
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")
                

def registrarProfesor():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE PROFESORES")
    print("#"*30)
    nombre = input("\nIngrese el nombre del profesor: ")
    apellido = input("Ingrese el apellido del profesor: ")
    email = input("Ingrese el email del profesor: ")
    telefono = input("Ingrese el número telefonico del profesor: ")
    facultad_id = input("Ingrese la dirección del profesor: ")
    ProfesorController.registerProfesor(nombre, apellido, email, telefono, facultad_id)
    
    
def visualizarProfesores():
    profesores = []
    profesores = ProfesorController.getAllProfesores()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE ESTUDIANTES")
    print("#"*30)
    for i, profesor in enumerate(profesores, start=1):
        print(f"""\nESTUDIANTE #{i}
              Id: {profesor.id}
              Nombre: {profesor.nombre}
              Apellido: {profesor.apellido}
              Email: {profesor.email}
              Telefono: {profesor.telefono}
              Id Facultad: {profesor.facultad_id}""")
        
def consultarProfesor():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE ESTUDIANTE")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del estudiante a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        profesor = ProfesorController.getProfesorById(id)
        if profesor == None:
            print("\nNo existe un profesor con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos del profesor:
                  Id: {profesor.id}
                  Nombre: {profesor.nombre}
                  Apellido: {profesor.apellido}
                  Email: {profesor.email}
                  Telefono: {profesor.telefono}
                  Id Facultad: {profesor.facultad_id}""")
            
             

def eliminarProfesor():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE PROFESOR")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del profesor a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        estudiante = ProfesorController.getProfesorById(id)
        if estudiante == None:
            print("\nNo existe un profesor con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            ProfesorController.deleteProfesor(id)