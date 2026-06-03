# Sistema bancario orientado a objetos
from cuenta import Cuenta

class AppBanco:

    def _init_(self):
        self.lista_cuentas = []

    def buscar(self, numero):
        for c in self.lista_cuentas:
            if c.num_cuenta == numero:
                return c
        return None

    def ejecutar(self):

        while True:
            print("\n====== SISTEMA BANCO ======")
            print("1. Nueva cuenta")
            print("2. Ver cuentas")
            print("3. Depositar")
            print("4. Retirar")
            print("5. Transferir")
            print("6. Buscar")
            print("7. Eliminar")
            print("8. Salir")

            op = input("Opción: ")

            # Crear cuenta
            if op == "1":
                nombre = input("Nombre: ")
                numero = input("No. cuenta: ")
                try:
                    saldo = float(input("Saldo inicial: "))
                except:
                    saldo = 0
                nueva = Cuenta(nombre, numero, saldo)
                self.lista_cuentas.append(nueva)

                print("Cuenta creada correctamente.")
            # Mostrar cuentas
            elif op == "2":

                if not self.lista_cuentas:
                    print("No hay cuentas.")
                else:
                    for c in self.lista_cuentas:
                        print("\nCliente:", c.cliente)
                        print("Cuenta:", c.num_cuenta)
                        print("Saldo:", c.saldo)
            # Depositar
            elif op == "3":
                numero = input("Cuenta: ")
                cuenta = self.buscar(numero)
                if cuenta:
                    monto = float(input("Cantidad: "))
                    cuenta.saldo += monto
                    print("Depósito hecho.")
                else:
                    print("No existe.")

            # Retirar
            elif op == "4":
                numero = input("Cuenta: ")
                cuenta = self.buscar(numero)
                if cuenta:
                    monto = float(input("Cantidad: "))
                    if monto <= cuenta.saldo:
                        cuenta.saldo -= monto
                        print("Retiro hecho.")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("No existe.")

            # Transferir
            elif op == "5":
                c1 = input("Origen: ")
                c2 = input("Destino: ")
                origen = self.buscar(c1)
                destino = self.buscar(c2)
                if origen and destino:
                    monto = float(input("Cantidad: "))
                    if monto <= origen.saldo:
                        origen.saldo -= monto
                        destino.saldo += monto
                        print("Transferencia exitosa.")
                    else:
                        print("No hay saldo.")
                else:
                    print("Cuenta no encontrada.")

            # Buscar
            elif op == "6":

                numero = input("Cuenta: ")
                cuenta = self.buscar(numero)
                if cuenta:
                    print("Cliente:", cuenta.cliente)
                    print("Saldo:", cuenta.saldo)
                else:
                    print("No existe.")
            # Eliminar
            elif op == "7":
                numero = input("Cuenta: ")
                cuenta = self.buscar(numero)
                if cuenta:
                    self.lista_cuentas.remove(cuenta)
                    print("Cuenta eliminada.")
                else:
                    print("No existe.")
            # Salir
            elif op == "8":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")


if __name__ == "_main_":
    main()