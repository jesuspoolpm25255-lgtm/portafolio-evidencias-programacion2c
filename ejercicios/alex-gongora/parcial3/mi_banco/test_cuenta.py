import unittest
from cuenta import cuenta

class testCuenta(unittest.TestCase):


   def setUp(self):
       self.cuenta = cuenta("fulanito pesez nengabo","001")
   #----------PRUEBAS DE CONSTRUCTOR----_-----


   def test_validad_saldo(self):
       self.assertEqual(self.cuenta.saldo,0,"El saldo inicial deberia ser cero por defecto")


   def test_validar_cliente(self):
       self.assertEqual(self.cuenta.cliente,"fulanito mendez megabo","el nombre de ")


   #----------PRUEBAS DE DEPOSITO---------


   def test_depositar_dinero_valido(self):
       result = self.cuenta.deposito(500)
       self.assertTrue(result)
       self.assertEqual(self.cuenta.saldo, 500, "El saldo actual deberias ser 500")
          
   def test_depositar_cantidad_negativa(self):
       result=self.cuenta.deosito(-200)
       self.assertFalse(result)
       self.assertEqual(self.cuenta.saldo,0, "El saldo actual deberia aser 0")


   #tesst para validar el deposito en 0
   def test_depositar_cantidad_cero(self):
       result=self.cuenta.deposito(0)
       self.assertFalse(result)
       self.assertEqual(self.cuenta.saldo,0,"El saldo actual deberia ser 0")


   #----------PRUEBAS DE RETIRO---------


   #1. Test para validar retiro con cantidad 0
   def test_retirar_cantidad_cero(self):
       result=self.cuenta.retirar(0)
       self.assertFalse(result)
       self.assertEqual(self.cuenta.saldo,0,"El saldo actual deberia ser 0")


   #2. Test para validar retiro con cantidad negativa
   def test_retirar_cantidad_negativa(self):
       result=self.cuenta.retirar(-100)
       self.assertFalse(result)
       self.assertEqual(self.cuenta.saldo,0,"El saldo actual deberia ser 0")


   #3. Test para validar cantidad mayor al saldo
   def test_retirar_cantidad_mayor_al_saldo(self):
       result=self.cuenta.retirar(100)
       self.assertFalse(result)
       self.assertEqual(self.cuenta.saldo,0,"El saldo actual deberia ser 0")

