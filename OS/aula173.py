# os + shutil. move, rename, copy, unlink
import os
import shutil

HOME = os.path.expanduser('~')
CAMINHO_BASE = os.path.join(
    HOME, 'your', 'path', 'goes', 'here',
)
PASTA_ORIGINAL = os.path.join(CAMINHO_BASE, 'exemplo')
NOVA_PASTA = os.path.join(CAMINHO_BASE, 'NOVA_PASTA')

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA, dirs_exist_ok=True)

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir
#             )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#             )
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)
