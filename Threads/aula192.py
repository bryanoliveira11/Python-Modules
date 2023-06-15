from threading import Thread
from time import sleep


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Olá Mundo', 10))
t.start()

t2 = Thread(target=vai_demorar, args=('hello world', 4))
t2.start()

t3 = Thread(target=vai_demorar, args=('oi', 5))
t3.start()

for i in range(5):
    sleep(1)
    print('vai demorar ?')

while t.is_alive():
    print('esperando thread')
    sleep(1)
