from compra import *
from carro import *

class Historico:
    def __init__(self):
        self.transacoes = []

    def imprimir(self):
        print('Extrato: \n', self.transacoes)

