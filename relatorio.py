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

print("Problemas encontrados:")
for problema in problemas:
    print(problema)
print("Linhas válidas:", len(linhas_validas))
