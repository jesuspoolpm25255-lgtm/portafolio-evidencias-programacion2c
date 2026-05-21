def suma(a,b):
    return a + b

import unittest

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(4, 6), 10)
    
    def test_suma_negativa(self):
        self.assertEqual(suma(-3, -6), -9)

    def test_suma_mixta(self):
        self.assertEqual(suma(-2, 3), 2)

if __name__== '_main_':
    unittest.main()