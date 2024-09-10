import unittest
from Equipo7_Legibilidad_V1_1 import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_multiplicacion(self):
        resultado = self.calculadora.calculo(4,5)
        self.assertEqual(resultado, 20)

    def test_division(self):
        resultado = self.calculadora.calculo(10,2)
        self.assertEqual(resultado, 5)

    def test_division_en_cero(self):
        with self.assertRaises(ValorError):
            self.calculadora.calculo(10,0)

if __name__ == '__main__':
    unittest.main()
