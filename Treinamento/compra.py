from carro import *
from historico import *

class Credito:
    def __init__(self, saldo, preco):
        self.saldo = saldo
        self.preco = preco
        self.historico = Historico()

    def comprar(self):
        if self.saldo >= self.preco:
            self.saldo -= self.preco
            print(f'Você comprou o seu novo carro com sucesso!')
            print(f'Seu saldo atual é de R$ {self.saldo}.')
            self.historico.transacoes.append(self.preco)
        else:
            print('Cartão recusado!')

