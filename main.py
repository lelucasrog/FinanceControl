from validacoes import ler_valor_valido, validar_salario, validar_despesa
from calculos import calcular_resumo
from relatorios import exibir_relatorio


def main():
    # 1. Entrada de dados
    salario = ler_valor_valido(
        "Quanto você recebe por mês R$: ",
        validar_salario,
        "Salário inválido! Digite um valor maior que zero.",
    )

    despesas_fixas = {
        "Alimentação": 0.0,
        "Aluguel": 0.0,
        "Energia": 0.0,
        "Internet": 0.0,
    }

    print("\n--- Cadastro de Despesas Fixas ---")
    for chave in despesas_fixas:
        despesas_fixas[chave] = ler_valor_valido(
            f"Quanto você gasta de {chave} por mês R$: ",
            validar_despesa,
            "Despesa inválida! O valor não pode ser negativo.",
        )

    despesas_extras = {}
    qtd_extras = 0

    print("\n***** Cadastro de despesas extras (digite sair no nome para encerrar) *****")
    while True:
        nome_extra = (
            input(f"Digite o nome da despesa extra {qtd_extras + 1}: ")
            .strip()
            .title()
        )
        if nome_extra.lower() == "sair" or nome_extra == "":
            break

        gasto = ler_valor_valido(
            f"Digite o valor de {nome_extra} R$: ",
            validar_despesa,
            "Despesa inválida! O valor não pode ser negativo.",
        )
        despesas_extras[nome_extra] = despesas_extras.get(nome_extra, 0.0) + gasto
        qtd_extras += 1

    # 2. Processamento
    resumo = calcular_resumo(salario, despesas_fixas, despesas_extras)

    # 3. Exibição do relatório
    exibir_relatorio(salario, despesas_fixas, despesas_extras, qtd_extras, resumo)


if __name__ == "__main__":
    main()
