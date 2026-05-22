class Cuenta:
    # Constructor de la clase Cuenta
    
    #-----------------------PRUEBA DEL CONSTRUCTOR-----------------------
    def __init__(self, cliente, cuenta, saldo = 0):
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
        """
        Inicializa una nueva cuenta bancaria con el cliente, número de cuenta y saldo inicial.
        
        Args:
            cliente (str): El nombre del cliente.
            cuenta (str): El número de cuenta.
            saldo (float): El saldo inicial de la cuenta. Por defecto es 0.
        """

    # Método para realizar un depósito en la cuenta
    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False
        """
        Realiza un depósito en la cuenta.
        
        Args: cantidad (float): La cantidad a depositar. Debe ser un valor positivo.
        Returns: True si el depósito fue exitoso, False si la cantidad es inválida.
        """

    # Método para realizar un retiro de la cuenta
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
        """
        Realiza un retiro de la cuenta.
        
        Args: cantidad (float): La cantidad a retirar. Debe ser un valor positivo y no puede exceder el saldo.
        Returns: True si el retiro fue exitoso, False si la cantidad es inválida o excede el saldo.
        """