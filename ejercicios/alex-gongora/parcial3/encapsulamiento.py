class cuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def set_saldo(self, saldo):
        self._saldo = saldo 

    def get_saldo(self):
        return self._saldo
    
    def depositar (self, cantidad):
        self._saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        print(f"saldo: (self._saldo)")

cuenta = cuentaBancaria(5000)
cuenta.set_saldo(-5000)
print(cuenta.get_saldo())
cuenta.mostrar_saldo()