# random

import os
import random

r_range = random.randrange(10, 20, 2)
print(r_range, 'Range')

r_randint = random.randint(10, 20)
print(r_randint, 'Randint')

nomes = ['maria', 'helena', 'joana']
random.shuffle(nomes)
print(nomes, 'Shuffle')

novos_nomes = random.sample(nomes, k=2)  # sample não repete valores
print(novos_nomes, 'Sample')


novos_nomes = random.choices(nomes, k=2)  # choice pode repetir valores
print(novos_nomes, 'Choice')
