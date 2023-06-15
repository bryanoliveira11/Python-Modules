# os.path.getsize e os.stat
import math
import os
from itertools import count
from pathlib import Path

diretorio = Path(__file__).parent
counter = count()


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    if tamanho_em_bytes <= 0:
        return "0B"

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = tamanho_em_bytes / potencia
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


for root, dirs, files in os.walk(diretorio):
    the_counter = next(counter)
    print(the_counter, 'PASTA ATUAL', root)

    for dir in dirs:
        print('', the_counter, 'DIR', dir)

    for file in files:
        tamanho = os.path.getsize(diretorio)
        print('', the_counter, 'FILE', file, formata_tamanho(tamanho))
