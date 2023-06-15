# sys argv
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('vc nao passou argumentos')
else:
    print(f'vc passou os argumentos {argumentos[1:]}')
    print(f'faça algo com {argumentos[1]}')
