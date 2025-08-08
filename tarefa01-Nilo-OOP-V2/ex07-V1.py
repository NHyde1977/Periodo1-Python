#Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
class BichoV
    def __init__(self, nome=None, fome, saude, idade):
        self.__name = nome
        self.__hungry = fome
        self.__health = saude
        self.__age = idade

    def alterar_nome(self, novo_nome):
        self.__name = novo_nome

    def status_fome(self, fome):
        self.__hungry = fome

    def status_saude(self, saude):
        self.__health = saude

    def alterar_idade(self, idade):
        self.__age = idade

    def get_nome(self):
        return self.__name

    def get_idade(self):
        return self.__age

    def get_fome(self):
        return self.__hungry

    def get_saude(self):
        return self.__health