# Classe Veiculo
class Veiculo:
    def __init__(self, placa, marca, tipo):
        self.__placa = placa
        self.__marca = marca
        self.__tipo = tipo

    def getPlaca(self):
        return self.__placa

    def getMarca(self):
        return self.__marca

    def getTipo(self):
        return self.__tipo

# Classe Carro (herda de Veiculo)
class Carro(Veiculo):
    def __init__(self, placa, marca, tipo, numero_de_portas):
        super().__init__(placa, marca, tipo)
        self.__numero_de_portas = numero_de_portas

    def getPortas(self):
        return self.__numero_de_portas

# Classe Caminhao (herda de Veiculo)
class Caminhao(Veiculo):
    def __init__(self, placa, marca, tipo, capacidade_de_carga):
        super().__init__(placa, marca, tipo)
        self.__capacidade_de_carga = capacidade_de_carga

    def getCarga(self):
        return self.__capacidade_de_carga

# Classe Motorista
class Motorista:
    def __init__(self, nome):
        self.__nome = nome
        self.__veiculo = None

    def addVeiculo(self, veiculo):
        self.__veiculo = veiculo

    def remVeiculo(self):
        self.__veiculo = None

    def getNome(self):
        return self.__nome

    def getVeiculo(self):
        if self.__veiculo:
            return self.__veiculo
        else:
            return "Nenhum veículo atribuído."

    def remMotorista(self):
        if self.__veiculo:
            print(f"Excluindo o veículo: {self.__veiculo.getTipo()}, Placa: {self.__veiculo.getPlaca()}")
            del self.__veiculo  # Excluindo o veículo ao remover o motorista
        print(f"Excluindo o motorista: {self.__nome}")
        self.__nome = None

if __name__ == "__main__":
    # Criando veículos
    carro1 = Carro("ABC-1234", "Toyota", "Carro", 4)
    caminhao1 = Caminhao("XYZ-5678", "Volvo", "Caminhão", 15000)

    # Criando motorista e associando veículos
    motorista1 = Motorista("Yuri e Vitor")
    motorista1.addVeiculo(carro1)

    # Exibindo informações do motorista e do veículo
    print(f"Motorista: {motorista1.getNome()}")
    veiculo = motorista1.getVeiculo()
    print(f"Veículo: {veiculo.getTipo()}, Marca: {veiculo.getMarca()}, Placa: {veiculo.getPlaca()}")

    # Mudando o veículo do motorista
    motorista1.addVeiculo(caminhao1)
    print(f"Veículo alterado para: {motorista1.getVeiculo().getTipo()}")

    # Removendo o motorista e o veículo junto
    motorista1.remMotorista()

    try:
        print(veiculo.getPlaca())  # Tentativa de acessar o veículo após exclusão
    except AttributeError:
        print("O veículo foi excluído junto com o motorista.")
        
    del motorista1

    print(veiculo)
