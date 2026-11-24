import unittest
from validacoes import (
    validar_salario,
    validar_despesa,
    ler_valor_valido
)
from unittest.mock import patch


class TestValidarSalario(unittest.TestCase):

    def test_salario_positivo(self):
        self.assertTrue(validar_salario(3000))

    def test_salario_zero(self):
        self.assertFalse(validar_salario(0))

    def test_salario_negativo(self):
        self.assertFalse(validar_salario(-500))


class TestValidarDespesa(unittest.TestCase):

    def test_despesa_positiva(self):
        self.assertTrue(validar_despesa(150))

    def test_despesa_zero(self):
        self.assertTrue(validar_despesa(0))

    def test_despesa_negativa(self):
        self.assertFalse(validar_despesa(-50))


class TestLerValorValido(unittest.TestCase):

    def test_ler_numero_valido(self):
        with patch("builtins.input", return_value="3000"):
            resultado = ler_valor_valido(
                "Digite o salário: ",
                validar_salario,
                "Salário inválido!"
            )

        self.assertEqual(resultado, 3000)

    def test_entrada_texto_invalido(self):
        with patch("builtins.input", side_effect=["abc", "3000"]):
            resultado = ler_valor_valido(
                "Digite o salário: ",
                validar_salario,
                "Salário inválido!"
            )

        self.assertEqual(resultado, 3000)

    def test_salario_negativo(self):
        with patch("builtins.input", side_effect=["-500", "3000"]):
            resultado = ler_valor_valido(
                "Digite o salário: ",
                validar_salario,
                "Salário inválido!"
            )

        self.assertEqual(resultado, 3000)

    def test_valores_nao_finitos(self):
        with patch("builtins.input", side_effect=["nan", "inf", "3000"]):
            resultado = ler_valor_valido(
                "Digite o salário: ",
                validar_salario,
                "Salário inválido!"
            )

        self.assertEqual(resultado, 3000)


if __name__ == "__main__":
    unittest.main()