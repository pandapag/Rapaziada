from historico import *

class Comprar:
    def __init__(self, saldo, preco):
        self.saldo = saldo
        self.preco = preco
        self.historico = Historico()

    def comprar(self):
        if self.saldo >= self.preco:
            print('Você comprou o carro com sucesso!')
            self.saldo -= self.preco
            print(f'Seu novo saldo é de: {self.saldo}')
            self.historico.transacoes.append(self.preco)
        else:
            print('Cartão recusado!')

