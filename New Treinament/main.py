from compra import *
from carro import *
from historico import *

if __name__ == '__main__':
    carro = Carro(120000.0)
    carteira = Comprar(500000.0, carro.preco)
    carteira.comprar()
    carteira.historico.imprimir()

