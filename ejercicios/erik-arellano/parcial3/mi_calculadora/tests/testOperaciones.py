import unittest
from parcial2.calculadoraBasica import suma, resta, multi, div


class testOperaciones(unittest.TestCase):
  
   def test_suma_positivos (self):
       self.assertEqual(suma(45,45),90)


   def test_suma_negativo (self):
       self.assertEqual(suma(-8, -9),-16)


   def test_resta_basica (self):
       self.assertEqual(resta(10,5), 5)


   def test_resta_negativo (self):
       self.assertEqual(resta(20,40), -20)


  
   def test_resta_valoresNegativos (self):
       self.assertEqual(resta(-10,-10), 0)


if __name__ == '__main__':
   unittest.main
