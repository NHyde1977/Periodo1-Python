class BichoVirtual:
    def __init__(self, nome="B1", fome=5, saude=5, idade=0):
        self.__name = nome
        self.__hungry = max(0, min(fome, 10))  # Fome entre 0 e 10
        self.__health = max(0, min(saude, 10)) # Saúde entre 0 e 10
        self.__age = max(0, idade)  # Idade não pode ser negativa

    def alterar_nome(self, novo_nome):
        self.__name = novo_nome

    def alterar_fome(self, fome):
        self.__hungry = max(0, min(fome, 10))  # Mantém o valor entre 0 e 10

    def alterar_saude(self, saude):
        self.__health = max(0, min(saude, 10))  # Mantém o valor entre 0 e 10

    def alterar_idade(self, idade):
        if idade >= 0:
            self.__age = idade

    def get_nome(self):
        return self.__name

    def get_idade(self):
        return self.__age

    def get_fome(self):
        return self.__hungry

    def get_saude(self):
        return self.__health

    def get_humor(self):
        return (self.__health + (10 - self.__hungry)) / 2  # Humor é uma média entre saúde e saciedade

    def exibir_status(self):
        return f"Nome: {self.__name}, Idade: {self.__age}, Fome: {self.__hungry}, Saúde: {self.__health}, Humor: {self.get_humor():.1f}"
