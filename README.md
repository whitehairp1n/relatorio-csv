# relatorio-csv

Gerador de relatório de pagamentos a partir de um arquivo CSV, com validação de dados. Feito em Python como projeto de estudo.

## O que o programa faz

1. Lê o arquivo `dados.csv` (pagamentos de unidades de um condomínio fictício).
2. Valida cada linha e separa os registros com problema:
   - valor ausente;
   - status inválido (aceitos: `pago`, `pendente`, `atrasado`);
   - unidade duplicada.
3. Calcula, só com as linhas válidas, o total esperado, o total pago, o total em aberto e o percentual de inadimplência.
4. Mostra o relatório no terminal e o salva em `relatorio.txt`.

Os dados são **fictícios**, criados só para este projeto. Alguns erros foram colocados de propósito para testar as validações.

## Como rodar

Requisito: Python 3 (não usa bibliotecas externas).

```bash
python relatorio.py
```

## Exemplo de saída

```
RELATÓRIO DE PAGAMENTOS
-----------------------
Linhas válidas: 7
Total esperado: R$ 6300.00
Total pago: R$ 3750.00
Total em aberto: R$ 2550.00
Inadimplência: 40.5%

Problemas encontrados:
- Valor ausente na unidade 103
- Unidade duplicada: 102
- Status inválido na unidade 106
```

## Estrutura do código

- `ler_dados`: lê o CSV e devolve as linhas.
- `validar`: separa linhas válidas e problemas.
- `calcular`: soma os valores e calcula a inadimplência.
- `gerar_relatorio`: monta o texto do relatório.
- `main`: executa tudo na ordem.

## O que aprendi

## O que aprendi

- Ler um arquivo CSV com Python (`csv.DictReader`) e acessar cada campo pelo nome da coluna.
- Validar dados antes de usá-los: valor vazio, status fora do esperado e unidade duplicada.
- Converter texto em número (`float`) para fazer cálculos, e deixar de fora as linhas com problema para não distorcer os totais.
- Organizar o código em funções, cada uma com uma responsabilidade (ler, validar, calcular, gerar o relatório).
- Usar Git e GitHub no dia a dia: um commit por etapa, deixando o histórico do projeto registrado.
- O que foi mais difícil: entender o recuo (identação) do Python e o que fica dentro do for e do ifç

## Próximos passos

- Refazer os cálculos em SQL (SQLite) para comparar com a versão em Python.
