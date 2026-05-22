from banco import Banco
from cuenta import cuenta


def main():
   def menu():
       print("MENU DEL PROGRAMA MI BANCO")
       print("1. Aperturar nueva cuenta")
       print("2.ver cliente")
       print("3.Depositar a una cuenta")
       print("4.Retirar de una cuenta")
       print("5.Transferencias de cuentas")
       print("6.Busca cuenta")
       print("7.Elimnar una cuenta")
       print("8.Salir del progrma")
   banco = Banco()
   while True:
       menu()
       opcion = input("Seleccione una opcion: ")
       if opcion == "1":
           nombre_cliente = input("Ingrese el nombre del cliente: ")
           numero_cuenta = input("Ingrese el numero de cuenta: ")
           nueva_cuenta = cuenta(nombre_cliente, numero_cuenta)
           print(f"Cuenta creada exitosamente para {nombre_cliente} con numero de cuenta {numero_cuenta}")
       elif opcion == "2":
           pass
       elif opcion == "3":
           pass
       elif opcion == "4":
           pass
       elif opcion == "5":
           pass
       elif opcion == "6":
           pass
       elif opcion == "7":
           pass
       elif opcion == "8":
           print("Gracias por usar Mi Banco. ¡Hasta luego!")
           break
       else:
           print("Opcion no valida. Por favor, seleccione una opcion del menu.")


if __name__ == "__main__":




   main()
   from banco import Banco
from cuenta import cuenta


def main():
   def menu():
       print("MENU DEL PROGRAMA MI BANCO")
       print("1. Aperturar nueva cuenta")
       print("2.ver cliente")
       print("3.Depositar a una cuenta")
       print("4.Retirar de una cuenta")
       print("5.Transferencias de cuentas")
       print("6.Busca cuenta")
       print("7.Elimnar una cuenta")
       print("8.Salir del progrma")
   banco = Banco()
   while True:
       menu()
       opcion = input("Seleccione una opcion: ")
       if opcion == "1":
           nombre_cliente = input("Ingrese el nombre del cliente: ")
           numero_cuenta = input("Ingrese el numero de cuenta: ")
           nueva_cuenta = cuenta(nombre_cliente, numero_cuenta)
           print(f"Cuenta creada exitosamente para {nombre_cliente} con numero de cuenta {numero_cuenta}")
       elif opcion == "2":
           pass
       elif opcion == "3":
           pass
       elif opcion == "4":
           pass
       elif opcion == "5":
           pass
       elif opcion == "6":
           pass
       elif opcion == "7":
           pass
       elif opcion == "8":
           print("Gracias por usar Mi Banco. ¡Hasta luego!")
           break
       else:
           print("Opcion no valida. Por favor, seleccione una opcion del menu.")


if __name__ == "__main__":
   main()
