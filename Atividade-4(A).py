# Classe Prato
class Prato:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def getNome(self):
        return self.__nome

    def getPreco(self):
        return self.__preco


# Classe Pedido
class Pedido:
    def __init__(self, numPedido):
        self.__numPedido = numPedido
        self.__pratos = []

    def getNumPedido(self):
        return self.__numPedido

    def getPratos(self):
        return self.__pratos

    def addPrato(self, prato):
        self.__pratos.append(prato)

    def remPrato(self, prato):
        if prato in self.__pratos:
            self.__pratos.remove(prato)

    def calcularTotal(self):
        total = sum([prato.getPreco() for prato in self.__pratos])
        return total


# Classe Cliente
class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__pedidos = []

    def getNome(self):
        return self.__nome

    def getPedidos(self):
        return self.__pedidos

    def addPedido(self, pedido):
        self.__pedidos.append(pedido)

    def remPedido(self, pedido):
        if pedido in self.__pedidos:
            self.__pedidos.remove(pedido)

if __name__ == "__main__":
    # Criando pratos
    prato1 = Prato("Lasanha", 30.0)
    prato2 = Prato("Pizza", 40.0)

    # Criando um pedido e adicionando pratos
    pedido1 = Pedido(1)
    pedido1.addPrato(prato1)
    pedido1.addPrato(prato2)

    # Calculando o total do pedido
    print(f"Total do Pedido {pedido1.getNumPedido()}: R${pedido1.calcularTotal()}")

    # Criando um cliente e associando o pedido
    cliente1 = Cliente("Yuri e Vitor")
    cliente1.addPedido(pedido1)

    # Exibindo informações do cliente e seus pedidos
    print(f"Cliente: {cliente1.getNome()}")
    for pedido in cliente1.getPedidos():
        print(f"Pedido {pedido.getNumPedido()}, Total: R${pedido.calcularTotal()}")
