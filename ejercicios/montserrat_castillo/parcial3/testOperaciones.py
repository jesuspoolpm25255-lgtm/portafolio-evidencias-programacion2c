import unittest
# Asegúrate de que la ruta 'parcial2.calculadoraBasica' sea correcta en tu estructura de carpetas
from parcial2.claculadoraBasica import suma, resta, multi, div

class TestOperaciones(unittest.TestCase):

    # --- PRUEBAS DE SUMA ---
    def test_suma_positivo(self):
        self.assertEqual(suma(300, 3), 303)

    def test_suma_negativos(self):
        self.assertEqual(suma(-4, -6), -10)

    # --- PRUEBAS DE RESTA ---
    def test_resta_basica(self):
        self.assertEqual(resta(10, 5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(10, 30), -20)

    def test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5, -5), 0)

    # --- PRUEBAS DE MULTIPLICACIÓN ---
    def test_multiplicacion(self):
        self.assertEqual(multi(5, 4), 20)
        self.assertEqual(multi(-2, 3), -6)

    # --- PRUEBAS DE DIVISIÓN ---
    def test_division_exacta(self):
        self.assertEqual(div(10, 2), 5)

    def test_division_por_cero(self):
        # Es buena práctica verificar cómo maneja tu función el error de dividir por cero
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

if __name__ == '__main__':
    unittest.main()