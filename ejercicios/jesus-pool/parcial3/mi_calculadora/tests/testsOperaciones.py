import unittest
from src.operaciones import suma, resta, multi, div


class test_operaciones(unittest.TestCase):

    def test_suma_positivos (self):
        self.assertEqual(suma(25,25),50)

    def test_suma_negativos(self):
        self.assertEqual(suma(-9,-6),-15)

    def test_resta_basica(self):
        self.assertEqual(resta(15,5),10)

    def test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5,-9),4)

if __name__ == 'main':
    unittest.main()