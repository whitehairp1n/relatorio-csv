import csv

with open("dados.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if linha["valor"] == "":
            print("Valor ausente na unidade", linha["unidade"])
        if linha["status"] not in ["pago", "pendente", "atrasado"]:
            print("Status inválido na unidade", linha["unidade"])
            