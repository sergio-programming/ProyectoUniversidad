

def menu():
    while True:
        print()
        print("#"*30)
        print("MENÚ PRINCIPAL GESTION UNIVERSIDAD")
        print("#"*30)
        print("""1. Gestion de Estudiantes.
2. Gestion de Docentes.""")
        
        try:
            opcion = int(input("\nPor favor digite la opción deseada: "))
        except ValueError:
            print("EL tipo de dato ingresado no es valido. Por favor ingrese un número.")
            input("Presione <Enter> para continuar")
            return
        else:
            if opcion == 1:
                pass
            
            elif opcion == 2:
                pass
            
            else:
                print("La opción ingresada no es valida. Por favor intente de nuevo.")
                input("Presione <Enter> para continuar")
                