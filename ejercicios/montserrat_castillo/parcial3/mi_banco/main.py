from banco import banco
from cuenta import Cuenta

def main():
    mi_banco = banco()
    
    while True:
        print("\n*****MENU DEL PROGRAMA MI BANCO*****")
        print("1. Aperturar nueva cuenta")
        print("2. Ver Clientes")
        print("3. Depositar a cuenta")
        print("4. Retirar de una cuenta")
        print("5. Transferencia entre cuentas")
        print("6. Buscar cuenta")
        print("7. Eliminar una cuenta")
        print("8. Salir del programa")

        opcion = input("Selecciona una opción (1-8): ")
        
        if opcion == "1":
            print("\n--- Aperturar nueva cuenta ---")
            pass
            
        elif opcion == "2":
            print("\n--- Ver Clientes ---")

            pass
            
        elif opcion == "3":
            print("\n--- Depositar a cuenta ---")
            pass
            
        elif opcion == "4":
            print("\n--- Retirar de una cuenta ---")
            pass
            
        elif opcion == "5":
            print("\n--- Transferencia entre cuentas ---")
            print("\n--- Buscar cuenta ---")
            pass
            
        elif opcion == "7":
            print("\n--- Eliminar una cuenta ---")
            pass
            
        elif opcion == "8":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 8.")

if __name__ == "__main__":
    main()