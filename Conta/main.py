from conta import *
from cliente import *

if __name__ == '__main__':
    cliente1 = Cliente('00000000000', 'The Big Cleyton', '00000000')
    cliente2 = Cliente('00000000000', 'The Big Lopes', '00000000')
    conta = Conta(100.0, 500000.0, '555-555')
    conta2 = Conta(100.0, 500000.0, '555-555')
    conta.exibir()
    conta2.exibir()
    conta.investir(100, 12)
    conta.exibir()
    conta2.exibir()

