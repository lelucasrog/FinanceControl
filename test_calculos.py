import unittest
from calculos import calcular_resumo


class TestCalcularResumo(unittest.TestCase):

    def test_calculo_resumo(self):
        salario = 3000

        fixas = {
            "Aluguel": 1000,
            "Energia": 200
        }

        extras = {
            "Lazer": 300,
            "Compras": 200
        }

        resultado = calcular_resumo(salario, fixas, extras)

        self.assertEqual(resultado["total_fixas"], 1200)
        self.assertEqual(resultado["total_extras"], 500)
        self.assertEqual(resultado["total_gastos"], 1700)
        self.assertEqual(resultado["saldo_final"], 1300)