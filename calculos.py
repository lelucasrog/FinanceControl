def verificar_situacao(saldo):
    if saldo >= 500:
        return "Saldo positivo dentro dos parâmetros. Parabéns!"
    elif saldo > 0:
        return "Saldo positivo, porém tome cuidado."
    elif saldo == 0:
        return "Você gastou tudo, sem reservas."
    else:
        return "Você gastou mais do que recebe. Alerta!"


def calcular_resumo(sal, fixas, extras):
    total_fixas = sum(fixas.values())
    total_extras = sum(extras.values())
    total_gastos = total_fixas + total_extras
    saldo_final = sal - total_gastos
    return {
        "total_fixas": total_fixas,
        "total_extras": total_extras,
        "total_gastos": total_gastos,
        "saldo_final": saldo_final,
        "situacao": verificar_situacao(saldo_final),
    }
