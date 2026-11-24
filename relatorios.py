def exibir_relatorio(salario, despesas_fixas, despesas_extras, qtd_extras, resumo):
    print("\n================ DETALHAMENTO DOS GASTOS ================")
    print("\n> DESPESAS FIXAS:")
    for chave, valor in despesas_fixas.items():
        porcentagem_fixa = (valor / salario) * 100
        print(f"- {chave}: R$ {valor:.2f} ({porcentagem_fixa:.1f}%)")

    print(f"\n> DESPESAS EXTRAS ({qtd_extras} lançamentos):")
    if despesas_extras:
        for chave, valor in despesas_extras.items():
            porcentagem_extra = (valor / salario) * 100
            print(f"- {chave}: R$ {valor:.2f} ({porcentagem_extra:.1f}%)")
    else:
        print("- Nenhuma despesa extra cadastrada.")

    print("\n===================== RESUMO GERAL =====================")
    print(f"Total de Despesas Fixas: R$ {resumo['total_fixas']:.2f}")
    print(f"Total de Despesas Extras: R$ {resumo['total_extras']:.2f}")
    print(f"Total Geral de Gastos: R$ {resumo['total_gastos']:.2f}")
    print(f"Saldo Final Livre: R$ {resumo['saldo_final']:.2f}")
    print("========================================================")
    print(resumo["situacao"])
