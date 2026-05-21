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
            result = self.cuenta.retirar(0)
            self.assertFalse(result)
            self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #2. test para validar retiro con cantidad negativa 
        def test_retirar_cantidad_negativa(self):
            result = self.cuenta.retirar(-100)
            self.assertFalse(result)
            self.assertEqual(self.cuenta.saldo, 0, "El saldo actual deberia ser 0")

    #3. test para validar retiro con cantidad mayor al saldo
        def test_retirar_cantidad_mayor_al_saldo(self):
            self.cuenta.depositar(300)
            result = self.cuenta.retirar(400)
            self.assertFalse(result)
            self.assertEqual(self.cuenta.saldo, 300, "El saldo actual deberia ser 300")