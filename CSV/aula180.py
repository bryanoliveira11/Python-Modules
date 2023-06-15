# csv writer

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

# COM LISTA
# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]

# with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)
#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)


# COM DICIONÁRIO

lista_clientes = [
    {'Nome': 'Pessoa1', 'Endereço': 'Centro 24'},
    {'Nome': 'Pessoa2', 'Endereço': 'Centro 25'},
    {'Nome': 'Pessoa3', 'Endereço': 'Centro 26'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
