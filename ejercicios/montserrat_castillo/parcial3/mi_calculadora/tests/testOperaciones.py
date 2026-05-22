import unittest
from mi_calculadora.src.operaciones import suma, resta, multi, div, expo

class testOperaciones(unittest.TestCase):

    def test_suma_positivo (self):
        self.assertEqual(suma(300,3), 303)

    def test_suma_negativo(self):
        self.assertEqual(suma(-4,-6), -10)

    def test_resta_basica(self): 
        self.assertEqual(resta(10,5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(10,30), -20)

    def test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5,-5), 0)

    def test_multi_basica(self):
        self.assertEqual(multi(5,5), 25)

    def test_multi_conNegativo(self):
        self.assertEqual(multi(-5,5), -25)

    def test_multi_dosNegativo(self):
        self.assertEqual(multi(-5,-5), 25)

    def test_division_basica(self):
        self.assertEqual(div(10,2), 5)

    def test_division_conNegativos(self):
        self.assertEqual(div(-10,2), 5)

    def test_division_dosNegativos(self):
        self.assertEqual(div(-10,-2), 5)

    def test_expo_basico(self):
        self.assertEqual(expo(2,3), 8)

    def test_expo_conNegativos(self):
        self.assertEqual(expo(2,-3), 0.125)

    def test_expo_dosNegativo(self):
        self.assertEqual(expo(-2,-3), -0.125)