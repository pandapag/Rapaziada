from cliente import *

class Conta:
    def __init__(self, saldo, limite, agencia):
        self.saldo = saldo
        self.limite = limite
        self.agencia = agencia

    def consulta(self):
        print(f'Seu saldo é de: {self.saldo}')

    def deposito(self, valor):
        self.saldo += valor
        print(f'Você depositou: {self.saldo} com sucesso!')
    
    def sacar(self, valor):
        if self.saldo >= valor:
            print(f'Seu saque de {valor} feito com sucesso!')
            self.saldo -= valor
            print(f'Seu novo saldo é de: {self.saldo}')
        else:
            print('Você não tem dinheiro o suficiente para esse saque.')

    def transfere(self, destino, valor):
        if self.saldo >= valor:
           self.saldo -= valor
           destino.saldo += valor
           print(f'Você transferiu: {valor}')

        else:
            print('Você não tem saldo suficiente para transferir!')
    
    def investir(self, valor, tempo):
        if self.saldo >= valor:
            valor *= 0.008
            valor *= tempo
            self.saldo += valor

    
    def exibir(self):
        print(self.saldo, self.limite, self.agencia)

