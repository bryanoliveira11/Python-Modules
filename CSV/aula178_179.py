# CSV ; reader e dict reader

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula178-ex.csv'

# ler em formato de lista.
# with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)

# ler em formato de dicionario
with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)
