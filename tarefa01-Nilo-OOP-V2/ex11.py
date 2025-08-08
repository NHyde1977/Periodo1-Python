class Carro:
    def __init__(self, consumo =15, combustivel =150): #consumo km por litro
        self.__dpl = consumo
        self.__gas = combustivel

    def andarcarro(self, distancia):
        (distancia / self.__dpl) = consumo
        self.__gas -= consumo

    def checargasolina(self):
        print(f"Quantidade de combustível no veículo é: {self.__gas} litros.")

    def abastecer(self, litros):
        self.__gas += litros

    