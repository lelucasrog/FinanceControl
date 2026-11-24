import math


def validar_salario(valor):
    return valor > 0


def validar_despesa(valor):
    return valor >= 0


def ler_valor_valido(mensagem, funcao_validacao, mensagem_erro):
    """Lê um número do usuário e repete até ser válido, finito e não gerar erro de texto."""
    while True:
        try:
            entrada = input(mensagem).replace(",", ".")
            valor = float(entrada)
            if not math.isfinite(valor):
                print("Entrada inválida! Digite um número real e finito.\n")
                continue
            if funcao_validacao(valor):
                return valor
            else:
                print(f"{mensagem_erro}\n")
        except ValueError:
            print("Entrada inválida! Digite apenas números (ex: 150.00).\n")
