import unittest

from cuenta import Cuenta
from banco import banco

class TestIntegracionBanco(unittest.TestCase):

    def setUp(self):
        self.cuenta1 = Cuenta("Fulanito Perez", "001", 1000)
        self.cuenta2 = Cuenta("Perezcils Sanchez", "002")

        self.banco = self.banco()

    def Test_transferencia_exitosa(self):
        resultado = self.banco.trasferir(self.cuenta1, self.cuenta2, 350)
        self.assertTrue(resultado, "Deberia realisarse de manera correcta la transferencia")
        self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
        self.assertEqual(self.cuenta2.saldo, 350, "el saldo de la cuenta 2 deberia ser 350")

    def test_transferencia_saldo_insufuciente(self):
        resultado = self.banco.trasferir(self.cuenta1, self.cuenta2, 1200)
        self.assertFalse(resultado, "la transferencia no se deberia realizar al no disponer")
        self.assertEqual(self.cuenta1.saldo, 1000, "El saldodeberia mantenerse sin cambios")
        self.assertEqual(self.cuenta2.saldo, 0, "El saldo de la cuenta 2 deberia ser 0")