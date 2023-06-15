# os.walk
import os
from itertools import count
from pathlib import Path

diretorio = Path(__file__).parent
counter = count()

for root, dirs, files in os.walk(diretorio):
    the_counter = next(counter)
    print(the_counter, 'PASTA ATUAL', root)

    for dir in dirs:
        print('', the_counter, 'DIR', dir)

    for file in files:
        print('', the_counter, 'FILE', file)
