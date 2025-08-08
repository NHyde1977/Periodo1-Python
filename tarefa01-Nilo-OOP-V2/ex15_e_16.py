class BichoVirtualPlus:
    def __init__(self, nome="B1", fome=5, saude=5, idade=0):
        self.__name = nome
        self.__hungry = max(0, min(fome, 10))  # Fome entre 0 e 10
        self.__health = max(0, min(saude, 10)) # Saúde entre 0 e 10
        self.__age = max(0, idade)  # Idade não pode ser negativa

    def alterar_nome(self, novo_nome):
        self.__name = novo_nome

    def alterar_fome(self, fome):
        self.__hungry = max(0, min(fome, 10))

    def alterar_saude(self, saude):
        self.__health = max(0, min(saude, 10))

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
        return (self.__health + (10 - self.__hungry)) / 2  # Média entre saúde e saciedade

    def darcomida(self, qtdcomida):
        self.__hungry = max(0, self.__hungry - qtdcomida)  # Reduz a fome sem ultrapassar os limites

    def brincar(self, horas):
        self.__health = min(10, self.__health + horas)  # Aumenta a saúde sem ultrapassar 10

    def exibir_status(self):
        return f"Nome: {self.__name}, Idade: {self.__age}, Fome: {self.__hungry}, Saúde: {self.__health}, Humor: {self.get_humor():.1f}"

    def __str__(self):
        return f"[DEBUG] Nome: {self.__name}, Idade: {self.__age}, Fome: {self.__hungry}, Saúde: {self.__health}"

# Exemplo de uso:
bicho = BichoVirtualPlus("Euclides", fome=7, saude=6)
print(bicho.exibir_status())

bicho.darcomida(3)  # Alimenta o bichinho
bicho.brincar(2)    # Brinca com o bichinho
print(bicho.exibir_status())

# Porta secreta
print(bicho)
