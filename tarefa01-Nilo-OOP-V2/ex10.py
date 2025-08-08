class Fuelpump:
    def __init__(self, tipocombustivel, valorlitro, qtdcombustivel):
        self.__fueltype = tipocombustivel
        self.__lprice = valorlitro
        self.__fuelamount = qtdcombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.__lprice


        if litros > self.__fuelamount:
            print("Erro: Combustível insuficiente na bomba!")
            return

        self.__fuelamount -= litros  # Atualiza o combustível restante
        print(f"Abastecido {litros:.2f} litros de {self.__fueltype}.")

    def abastecerPorLitro(self, litros):
        if litros > self.__fuelamount:
            print("Erro: Combustível insuficiente na bomba!")
            return

        valor_a_pagar = litros * self.__lprice
        self.__fuelamount -= litros  # Atualiza o combustível restante
        print(f"Abastecido {litros:.2f} litros. Total a pagar: R$ {valor_a_pagar:.2f}")

    def alterarValor(self, novo_valor):
        self.__lprice = novo_valor
        print(f"Novo valor do litro: R$ {self.__lprice:.2f}")

    def alterarCombustivel(self, novo_tipo):
        self.__fueltype = novo_tipo
        print(f"Tipo de combustível alterado para: {self.__fueltype}")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.__fuelamount = nova_quantidade
        print(f"Quantidade de combustível na bomba agora é: {self.__fuelamount} litros.")

    def verBomba(self):
            print(f"Tipo: {self.__fueltype} | Preço/Litro: R$ {self.__lprice:.2f} | Quantidade: {self.__fuelamount}L")


bomba = Fuelpump("Gasolina", 9.99, 100)

bomba.verBomba()

bomba.abastecerPorValor(50)
bomba.verBomba()

bomba.abastecerPorLitro(10)
bomba.verBomba()

bomba.alterarValor(7)
bomba.alterarCombustivel("Etanol")
bomba.alterarQuantidadeCombustivel(2000)
bomba.verBomba()