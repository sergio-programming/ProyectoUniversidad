from view.estudiante import menuEstudiantes
from view.profesor import menuProfesores
from view.facultad import menuFacultades
from view.programa import menuProgramas

def menu():
    while True:
        print()
        print("#"*30)
        print("MENÚ PRINCIPAL GESTION UNIVERSIDAD")
        print("#"*30)
        print("""1. Gestión de Facultades.
2. Gestión de Programas.
3. Gestión de Estudiantes.
4. Gestion de Profesores.""")
        
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                menuFacultades()
            
            elif opcion == 2:
                menuProgramas()
                
            elif opcion == 3:
                menuEstudiantes()
                
            elif opcion == 4:
                menuProfesores()
            
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")
                