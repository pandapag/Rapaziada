from compra import *

class Historico:
    def __init__(self):
        self.transacoes = []
    
    def mostrar(self):
        print('Histórico de transaçções:\n', self.transacoes)

