from compra import *
from carro import *
from historico import *

if __name__ == "__main__":
    carro1 = Carro("Prata, ", "Mercedez, ", 120000.0, "SEXO 0800.")
    carteira = Credito(500000.0, carro1.preca)
    carteira.comprar()
    carteira.historico.mostrar()

