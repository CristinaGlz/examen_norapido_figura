import unittest
from Figuras import Figuras

class TestFiguras(unittest.TestCase):
    def test_cuadrado_2_2(self):
        fig = Figuras()
        self.assertEqual(4,fig.cuadrado(2,2))
    def test_cuadrado_5_5(self):
        fig = Figuras()
        self.assertEqual(25,fig.cuadrado(5,5))
    def test_cuadrado_9_9(self):
        fig = Figuras()
        self.assertEqual(81,fig.cuadrado(9,9))
    def test_circulo_5(self):
        fig = Figuras()
        self.assertEqual(78.53999999999999,fig.circulo(5))
    def test_circulo_2(self):
        fig = Figuras()
        self.assertEqual(12.5664,fig.circulo(2))
    def test_circulo_1(self):
        fig = Figuras()
        self.assertEqual(3.1416,fig.circulo(1))
    def test_triangulo_2_1(self):
        fig = Figuras()
        self.assertEqual(1,fig.triangulo(2,1))
    def test_triangulo_5_3(self):
        fig = Figuras()
        self.assertEqual(7,fig.triangulo(5,3))
    def test_triangulo_9_1(self):
        fig = Figuras()
        self.assertEqual(4,fig.triangulo(9,1))
    def test_elipse_2_1(self):
        fig = Figuras()
        self.assertEqual(6.2832,fig.elipse(2,1))
    def test_elipse_5_3(self):
        fig = Figuras()
        self.assertEqual(47.124,fig.elipse(5,3))
    def test_elipse_9_1(self):
        fig = Figuras()
        self.assertEqual(28.2744,fig.elipse(9,1))
        
if __name__ == "__main__":
    unittest.main()
