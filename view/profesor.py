from controller.profesor import ProfesorController
from controller.facultad import FacultadController

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
                actualizarProfesor()
            
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
    fecha_nacimiento = input("Ingrese la feha de nacimiento del profesor (AAAA-MM-DD): ")
    genero = input("Ingrese el genero del profesor (F/M): ")
    email = input("Ingrese el email del profesor: ")
    telefono = input("Ingrese el número telefónico del profesor: ")
    while True:
        try:
            facultad_id = input("Ingrese el id de la facultad a la que pertenece el profesor: ")
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
            
    ProfesorController.registerProfesor(nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id)
    
    
def visualizarProfesores():
    profesores = []
    profesores = ProfesorController.getAllProfesores()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE PROFESORES")
    print("#"*30)
    for i, profesor in enumerate(profesores, start=1):
        print(f"""\nPROFESOR #{i}
              Id: {profesor.id}
              Nombre: {profesor.nombre}
              Apellido: {profesor.apellido}
              Fecha de Nacimiento: {profesor.fecha_nacimiento}
              Genero: {profesor.genero}
              Email: {profesor.email}
              Telefono: {profesor.telefono}
              Id Facultad: {profesor.facultad_id}""")
        
def consultarProfesor():
    print()
    print("#"*30)
    print("\nMODULO DE CONSULTA DE PROFESOR")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del profesor a consultar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        profesor = ProfesorController.getProfesorById(id)
        if profesor is None:
            print("\nNo existe un profesor con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos del profesor:
                  Id: {profesor.id}
                  Nombre: {profesor.nombre}
                  Apellido: {profesor.apellido}
                  Fecha de Nacimiento: {profesor.fecha_nacimiento}
                  Genero: {profesor.genero} 
                  Email: {profesor.email}
                  Telefono: {profesor.telefono}
                  Id Facultad: {profesor.facultad_id}""")
            
def actualizarProfesor():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE PROFESOR")
    print("#"*30)
    while True:
        try:
            id = int(input("\nIngrese el id del profesor a actualizar: "))
        except ValueError:
            print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")    
        else:
            break
        
    profesor = ProfesorController.getProfesorById(id)
    
    
    if profesor is None:
        print("\nNo existe un profesor con el numero de ID ingresado")
        input("Presione <Enter> para continuar")
        return
    else:
        nombre = input("Ingrese el nombre del profesor: ")
        if nombre == "":
            nombre = profesor.nombre

        apellido = input("Ingrese el apellido del profersor: ")
        if apellido == "":
            apellido = profesor.apellido
            
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del profesor (AAAA-MM-DD): ")
        if fecha_nacimiento == "":
            fecha_nacimiento = profesor.fecha_nacimiento
            
        genero = input("Ingrese el genero del profesor (F/M): ")
        if genero == "":
            genero = profesor.genero
            
        email = input("Ingrese el email del profesor: ")
        if email == "":
            email = profesor.email
            
        telefono = input("Ingrese el número telefónico del profesor: ")
        if telefono == "":
            telefono = profesor.telefono
        
        while True:
            try:
                facultad_id = int(input("Ingrese el id de la facultad a la que pertenece el profesor: "))
                facultad = FacultadController.getFacultadById(facultad_id)
                if facultad is None:
                    raise Exception("\nLa facultad con el numero de id ingresado no existe. Por favor intente de nuevo.")
            except ValueError:
                print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            except Exception as e:
                print(f"\n{e}")
                input("Presione <Enter> para continuar")
            else:
                break
        
        ProfesorController.updateProfesor(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, facultad_id)
        

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
        profesor = ProfesorController.getProfesorById(id)
        if profesor is None:
            print("\nNo existe un profesor con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            ProfesorController.deleteProfesor(id)
            print("!Registro de Profesor eliminado exitosamente!")
            input("Presione <Enter> para continuar")