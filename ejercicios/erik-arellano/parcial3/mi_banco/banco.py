from cuenta import Cuenta

class Banco:
    
    def transferir(self, origen, destino, cantidad):
        if origen.retirar(cantidad):
            destino.deposito(cantidad)
            return  True
        return False