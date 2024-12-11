from view.estudiante import menuEstudiantes
from view.profesor import menuProfesores
from view.facultad import menuFacultades
from view.programa import menuProgramas
from view.curso import menuCursos
from view.matriculaCurso import menuMatriculasCursos
from view.matriculaPrograma import menuMatriculasProgramas

def menu():
    while True:
        print()
        print("#"*30)
        print("MENÚ PRINCIPAL GESTION UNIVERSIDAD")
        print("#"*30)
        print("""1. Gestión de Facultades.
2. Gestión de Programas.
3. Gestión de Estudiantes.
4. Gestión de Profesores.
5. Gestión de Cursos.
6. Gestión de Matriculas de Programas.
7. Gestión de Matriculas de Cursos.
8. Salir del programa.""")
        
        while True:
            try:
                opcion = int(input("\nPor favor digite la opción deseada: "))
            except ValueError:
                print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
                input("Presione <Enter> para continuar")
            else:
                if opcion == 1:
                    menuFacultades()
            
                elif opcion == 2:
                    menuProgramas()
                
                elif opcion == 3:
                    menuEstudiantes()
                
                elif opcion == 4:
                    menuProfesores()
                    
                elif opcion == 5:
                    menuCursos()
                    
                elif opcion == 6:
                    menuMatriculasProgramas()
                
                elif opcion == 7:
                    menuMatriculasCursos()
                    
                elif opcion == 8:
                    print("Gracias por usar nuestro programa. HASTA PRONTO!!")
                    input("Presione <Enter> para continuar")
                    break
            
                else:
                    print("La opción ingresada no es valida. Por favor intente de nuevo.")
                    input("Presione <Enter> para continuar")
                