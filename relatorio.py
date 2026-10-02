import csv

STATUS_VALIDOS = ["pago", "pendente", "atrasado"]


def ler_dados(caminho):
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        return list(csv.DictReader(arquivo))


def validar(linhas):
    unidades_vistas = []
    problemas = []
    linhas_validas = []
    for linha in linhas:
        valido = True
        if linha["valor"] == "":
            problemas.append("Valor ausente na unidade " + linha["unidade"])
            valido = False
        if linha["status"] not in STATUS_VALIDOS:
            problemas.append("Status inválido na unidade " + linha["unidade"])
            valido = False
        if linha["unidade"] in unidades_vistas:
            problemas.append("Unidade duplicada: " + linha["unidade"])
            valido = False
        else:
            unidades_vistas.append(linha["unidade"])
        if valido:
            linhas_validas.append(linha)
    return linhas_validas, problemas


def calcular(linhas_validas):
    total_esperado = 0
    total_pago = 0
    total_aberto = 0
    for linha in linhas_validas:
        valor = float(linha["valor"])
        total_esperado = total_esperado + valor
        if linha["status"] == "pago":
            total_pago = total_pago + valor
        else:
            total_aberto = total_aberto + valor
    if total_esperado > 0:
        percentual = total_aberto / total_esperado * 100
    else:
        percentual = 0
    return total_esperado, total_pago, total_aberto, percentual


def gerar_relatorio(qtd_validas, problemas, esperado, pago, aberto, percentual):
    linhas = [
        "RELATÓRIO DE PAGAMENTOS",
        "-----------------------",
        f"Linhas válidas: {qtd_validas}",
        f"Total esperado: R$ {esperado:.2f}",
        f"Total pago: R$ {pago:.2f}",
        f"Total em aberto: R$ {aberto:.2f}",
        f"Inadimplência: {percentual:.1f}%",
        "",
        "Problemas encontrados:",
    ]
    for problema in problemas:
        linhas.append("- " + problema)
    return "\n".join(linhas)


def main():
    linhas = ler_dados("dados.csv")
    linhas_validas, problemas = validar(linhas)
    esperado, pago, aberto, percentual = calcular(linhas_validas)
    texto = gerar_relatorio(
        len(linhas_validas), problemas, esperado, pago, aberto, percentual
    )
    print(texto)
    with open("relatorio.txt", "w", encoding="utf-8") as saida:
        saida.write(texto)


if __name__ == "__main__":
    main()
