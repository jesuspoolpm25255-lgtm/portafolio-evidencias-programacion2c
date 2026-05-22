from banco import banco
from cuenta import Cuenta

def main():
    mi_banco = banco()
    
    while True:
        opcion = input("\n1. Nueva cuenta\n2. Ver Clientes\n3. Depositar\n4. Retirar\n5. Transferir\n6. Buscar\n7. Eliminar\n8. Salir\n\nSelecciona una opción: ")
        
        if opcion == "1":
            pass  # para crear cuenta
        elif opcion == "2":
            pass  # para ver clientes
        elif opcion == "3":
            pass  # para depositar
        elif opcion == "4":
            pass  # para retirar
        elif opcion == "5":
            pass  # para transferir
        elif opcion == "6":
            pass  # para buscar
        elif opcion == "7":
            pass  # para eliminar
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()