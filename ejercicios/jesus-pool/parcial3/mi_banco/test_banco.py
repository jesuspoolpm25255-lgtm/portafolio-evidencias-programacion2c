import unittest 

from cuenta import Cuenta
from banco import Banco

class TestIntegracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = Cuenta("Fulanito Perez", "001", 1000)
        self.cuenta2 = Cuenta("Perezcila Sanchez", "002")

        self.banco = Banco()

    def test_tranferencia_exitosa(self):
        resultado = self.banco.transferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia realizarse de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta destino deberia ser 350")