import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):

    def setUp(self):
        self.cuenta = Cuenta("Fulanito Perez Mengano", "001")

    #-----------------------PRUEBA DEL CONSTRUCTOR-----------------------

    def test_validad_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial deberia serl 0 por defecto")

    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito Perez Mengano", "El nombre del cliente no es valid")

    #-----------------------PRUEBAS DE DEPOSITO-----------------------

    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser 500.00")

    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #test para validar deposito con cantidad 0
    def test_depositar_cantidad_cero(self):
        result = self.cuenta.deposito(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #-----------------------PRUEBA DE RETIRO-----------------------

    #1. test para validar retiro con cantidad 0
    def test_retirar_cantidad_cero(self):
        result = self.cuenta.retirar(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #2. test para validar retiro con cantidad negativa
    def test_retirar_cantidad_negativa(self):
        result = self.cuenta.retirar(-100)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #3. test para validar cantedad mayor al saldo
    def test_retirar_cantidad_mayor_al_saldo(self):
        self.cuenta.deposito(300)
        result = self.cuenta.retirar(400)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual deberia ser 300")

if __name__ == "__main__":
    unittest.main()