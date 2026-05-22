import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada prueba
        """
        self.cuenta = Cuenta("Fulanito Perez Mengano", "001")

    # ------------- PRUEBAS DEL CONSTRUCTOR --------------

    def test_validar_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0,"El saldo inicial deberia ser 0 por defecto")

    def test_validar_cliente(self):
        self.assertEqual(self.cuenta.cliente, "Fulanito Perez Mengano", "El nombre de cliente no es valido")

    # ------------ PRUEBAS DE DEPOSITO -------------------

    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberia ser de 500.00")

    def test_depositar_cantidad_negativa(self):
        result = self.cuenta.deposito(-200)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    # test para validar deposito en 0

    # ---------------- PRUEBAS DE RETIRO ------------------------

    #1. test para validar retiro con cantidad 0
    def test_retirar_cantidad_cero(self):
        result = self.cuenta.retiro(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "No se puede retirar cero")
    #2. test para validar retiro con cadef test_retirar_cantidad_cero(self):
    def test_retirar_cantidad_negativa(self):
        result = self.cuenta.retiro(-50)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "No se puede retirar montos negativos")
    #3. test para validar retirodef test_retirar_cantidad_negativa(self):
    def test_retirar_mas_del_saldo(self):
        result = self.cuenta.retiro(1000)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "No se puede retirar más de lo que hay en la cuenta")
        