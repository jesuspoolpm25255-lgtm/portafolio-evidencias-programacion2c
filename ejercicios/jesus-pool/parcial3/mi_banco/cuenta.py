class Cuenta:
    """
    Clase que modela una cuenta bancaria con operaciones basicas.
    Atributos:
      cliente (str): Nombre completo del titular de la cuenta
      cuenta (str):Numero o indentificador unico de la cuenta
      saldo (float): Montode dinero disponible, por defecto inicia en 0
    """
    def _init_(self, cliente, cuenta, saldo=0):
        """
        Constructor de la clase cuenta
        Se ejecuta automaticamente al crear una nueva cuenta.
        Parámetros:
           cliente (str): Nombre del dueño de la cuenta 
           cuenta (str): Numero de cuenta asigando
           saldo (float, opcional): Saldo inicial,valor predetermiando = 0
        """
        
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
    def deposito(self, cantidad):
        """
        Realiza un deposito de dinero en la cuenta
        Solo acepta cantidades mayores a 0.
        Parámetros: 
           cantidad (float): Monto de dinero a ingresar
        Retorna:
           bool: True si el deposito fue exitoso, False si la cantidad es válida
    
        """
        
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Realiza un retiro de dinero que la cuenta.
        valida que la cantidad sea positiva y que haya sificiente saldo.
        Parámetros:
           cantidad (float): Monto de dinero a retirat
        Retorna:
           bool: True si el retiro fue exitoso, False si no cumple las condiciones
        """
        
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    
def main():
    """Funcion principal(pendiente de implementacion si se requiere ejecucion directa)"""
    pass

if __name__ == "_main_":
      main()