from controller.estudiante import EstudianteController

def menuEstudiantes():
    while True:
        print()
        print("#"*30)
        print("MENÚ GESTION ESTUDIANTES")
        print("#"*30)
        print("""1. Registro de estudiantes.
2. Consultar datos de un estudiante.
3. Visualizar estudiantes registrados.
4. Actualizar datos de estudiantes registrados.
5. Eliminar registro de estudiantes.
6. Volver al menú principal.""")
        
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                registrarEstudiante()
            
            elif opcion == 2:
                consultarEstudiante()
            
            elif opcion == 3:
                visualizarEstudiantes()
            
            elif opcion == 4:
                actualizarEstudiante()
            
            elif opcion == 5:
                eliminarEstudiante()
            
            elif opcion == 6:
                break
            
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")
                

def registrarEstudiante():
    print()
    print("#"*30)
    print("\nMODULO DE REGISTRO DE ESTUDIANTES")
    print("#"*30)
    nombre = input("\nIngrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (AAAA/MM/DD): ")
    genero = input("Ingrese el genero del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    telefono = input("Ingrese el número telefonico del estudiante: ")
    direccion = input("Ingrese la dirección del estudiante: ")
    EstudianteController.registerEstudiante(nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)
    
    
def visualizarEstudiantes():
    estudiantes = []
    estudiantes = EstudianteController.getAllEstudiantes()
    print()
    print("#"*30)
    print("\nMODULO DE VISUALIZACIÓN DE ESTUDIANTES")
    print("#"*30)
    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"""\nESTUDIANTE #{i}
              Id: {estudiante.id}
              Nombre: {estudiante.nombre}
              Apellido: {estudiante.apellido}
              Fecha de Nacimiento: {estudiante.fecha_nacimiento}
              Genero: {estudiante.genero}
              Email: {estudiante.email}
              Telefono: {estudiante.telefono}
              Dirección: {estudiante.direccion}""")
        
def consultarEstudiante():
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
        estudiante = EstudianteController.getEstudianteById(id)
        if estudiante == None:
            print("\nNo existe un estudiante con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            print(f"""\nEstos son los datos del estudiante:
                  Id: {estudiante.id}
                  Nombre: {estudiante.nombre}
                  Apellido: {estudiante.apellido}
                  Fecha de Nacimiento: {estudiante.fecha_nacimiento}
                  Genero: {estudiante.genero}
                  Email: {estudiante.email}
                  Telefono: {estudiante.telefono}
                  Dirección: {estudiante.direccion}""")
            
def actualizarEstudiante():
    print()
    print("#"*30)
    print("\nMODULO DE ACTUALIZACIÓN DE DATOS DE ESTUDIANTE")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del estudiante a actualizar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        estudiante = EstudianteController.getEstudianteById(id)
        if estudiante == None:
            print("\nNo existe un estudiante con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            nombre = input("\nIngrese el nombre del estudiante: ")
            if nombre == '':
                nombre = estudiante.nombre
            
            apellido = input("Ingrese el apellido del estudiante: ")
            if apellido == '':
                apellido= estudiante.apellido
                
            fecha_nacimiento = input("Ingrese la fecha de nacimiento del estudiante (DD/MM/AAAA): ")
            if fecha_nacimiento == '':
                fecha_nacimiento = estudiante.nombrefecha_nacimiento
                
            genero = input("Ingrese el genero del estudiante: ")
            if genero == '':
                genero = estudiante.genero
                
            email = input("Ingrese el email del estudiante: ")
            if email == '':
                email = estudiante.email
                
            telefono = input("Ingrese el telefono del estudiante: ")
            if telefono == '':
                telefono = estudiante.telefono
                
            direccion = input("Ingrese el telefono del estudiante: ")
            if direccion == '':
                direccion = estudiante.direccion
            
            EstudianteController.updateEstudiante(id, nombre, apellido, fecha_nacimiento, genero, email, telefono, direccion)     
             

def eliminarEstudiante():
    print()
    print("#"*30)
    print("\nMODULO DE ELIMINACION DE REGISTRO DE ESTUDIANTE")
    print("#"*30)
    try:
        id = int(input("\nIngrese el id del estudiante a eliminar: "))
    except ValueError:
        print("\nEl tipo de dato ingresado no es valido. Por favor ingrese un número.")
        input("Presione <Enter> para continuar")
    else:
        estudiante = EstudianteController.getEstudianteById(id)
        if estudiante == None:
            print("\nNo existe un estudiante con el numero de ID ingresado")
            input("Presione <Enter> para continuar")
            return
        else:
            EstudianteController.deleteEstudiante(id)