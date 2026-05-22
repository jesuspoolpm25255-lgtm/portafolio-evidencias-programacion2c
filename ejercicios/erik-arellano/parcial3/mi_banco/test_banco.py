import unittest




from cuenta import cuenta
from banco import Banco




class TestIntegracionBanco(unittest.TestCase):




  def setUp(self):
      self.cuenta1 =cuenta("Fulanito perez", "001", 1000)
      self.cuenta2 = cuenta("Perezcila sanches", "002")




      self.banco = Banco()




  def test_transferencia_exitosa(self):
      resultado = self.banco.trasferir(self.cuenta1, self.cuenta2, 350)
      self.assertTrue(resultado, "Deberia realizarce de manera correcta la transferencia")
      self.assertEqual(self.cuenta1.saldo, 650, "El saldo de la cuenta 1 deberia ser 650")
      self.assertEqual(self.cuenta2.saldo, 350, "El saldo de la cuenta destino deberia ser 350")




  def test_trasferencia_saldo_insuficiente(self):
      resultado =self.banco.trasferir(self.cuenta1, self.cuenta2, 1200)
      self.assertFalse(resultado, "La tranferencia no se deberia realizar al no disponer el saldo sufiente")
      self.assertEqual(self.cuenta1.saldo, 100, "El saldo deberia mantenerse sin camabios")
      self.assertEqual(self.cuenta2.saldo, 0, "El saldo de la cuenta destino deberia ser 0")
