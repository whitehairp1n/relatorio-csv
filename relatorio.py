import csv

unidades_vistas = []
problemas = []
linhas_validas = []

with open("dados.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        valido = True
        if linha["valor"] == "":
            problemas.append("Valor ausente na unidade " + linha["unidade"])
            valido = False
        if linha["status"] not in ["pago", "pendente", "atrasado"]:
            problemas.append("Status inválido na unidade " + linha["unidade"])
            valido = False
        if linha["unidade"] in unidades_vistas:
            problemas.append("Unidade duplicada: " + linha["unidade"])
            valido = False
        else:
            unidades_vistas.append(linha["unidade"])
        if valido:
            linhas_validas.append(linha)

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

percentual = total_aberto / total_esperado * 100

linhas_relatorio = [
    "RELATÓRIO DE PAGAMENTOS",
    "-----------------------",
    f"Linhas válidas: {len(linhas_validas)}",
    f"Total esperado: R$ {total_esperado:.2f}",
    f"Total pago: R$ {total_pago:.2f}",
    f"Total em aberto: R$ {total_aberto:.2f}",
    f"Inadimplência: {percentual:.1f}%",
    "",
    "Problemas encontrados:",
]
for problema in problemas:
    linhas_relatorio.append("- " + problema)

texto = "\n".join(linhas_relatorio)
print(texto)

with open("relatorio.txt", "w", encoding="utf-8") as saida:
    saida.write(texto)
