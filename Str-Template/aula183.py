import locale
import string
from datetime import datetime
from pathlib import Path

TXT = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float | int) -> str:
    brl = 'R$' + locale.currency(numero, symbol=False, grouping=False)
    return brl


data = datetime(2023, 6, 13)
dados = dict(
    nome='pessoa',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='HELLO',
    telefone='+55 40028922'
)

with open(TXT, 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

template = string.Template(texto)
print(template.substitute(dados))
