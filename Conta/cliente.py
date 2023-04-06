from conta import *

class Cliente:
    def __init__(self, cpf, nome, cep):
        self.cpf = cpf
        self.nome = nome
        self.cep = cep

    def exibir(self):
        print(self.cpf, self.nome, self.cep)

