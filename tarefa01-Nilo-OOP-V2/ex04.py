#envelhecer+crescer, engordar, emagrecer
class Pessoa:
    def __init__(self,nome=None, idade=0, peso=0.5, altura=0.45):
        self.__name = nome
        self.__age = idade
        self.__weight = peso
        self.__height = altura

    def set_name(self, nome):
        self.__name = nome

    def set_envelhecer(self):
        self.__age += 1
        if self.__age <= 21:
            self.__height += self.__age * 0.05

    def set_engordar(self, peso):
        self.__weight += peso

    def set_emagrecer(self, perdapeso):
        self.__weight -= perdapeso