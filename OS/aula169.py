import os
from pathlib import Path

caminho = os.path.join('your', 'path', 'here', 'arquivo.txt')
print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(diretorio, arquivo, caminho_arquivo, extensao_arquivo)

path = Path(__file__).parent

if not os.path.exists(path):
    print('NÃO EXISTE')
else:
    print('EXISTE')

print(path, os.path.basename(path))
print(os.path.dirname(path))
