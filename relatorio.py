import csv

with open("dados.csv", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(
            linha["unidade"],
            "-",
            linha["morador"],
            "-",
            linha["valor"],
            "-",
            linha["status"],
        )
