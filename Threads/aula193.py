from threading import Lock, Thread
from time import sleep


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Estoque Insuficiente')
            return

        sleep(1)

        print(
            f'Você Comprou {quantidade} Ingresso(s).'
            f'Quantidade Disponível {self.estoque}'
        )

        self.estoque -= quantidade

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)
