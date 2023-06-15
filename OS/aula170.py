# os.listdir
import os
from pathlib import Path

diretorio = Path(__file__).parent

for pasta in os.listdir(diretorio):
    if not os.path.isdir(pasta):
        continue

    for item in os.listdir(pasta):
        file, extension = os.path.splitext(item)
        if extension in ['.png', '.jpg', '.jpeg']:
            print(item)
