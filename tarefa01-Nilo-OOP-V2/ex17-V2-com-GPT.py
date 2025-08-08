import random

class Animal:
    def __init__(self, fome=None, tedio=None):
        self.__hungry = random.randint(0, 10) if fome is None else max(0, min(fome, 10))
        self.__boredom = random.randint(0, 10) if tedio is None else max(0, min(tedio, 10))

    def alimentar(self, qtdcomida):
        self.__hungry = max(0, self.__hungry - qtdcomida)

    def brincar(self, horas):
        self.__boredom = max(0, self.__boredom - horas)

    def get_status(self):
        return f"Fome: {self.__hungry}, Tédio: {self.__boredom}"

class Porco(Animal):
    def __init__(self, fome=None, tedio=None):
        super().__init__(fome, tedio) # o "super" puxa o método da classe pai para o filho.

class Galinha(Animal):
    def __init__(self, fome=None, tedio=None):
        super().__init__(fome, tedio)

class Vaca(Animal):
    def __init__(self, fome=None, tedio=None):
        super().__init__(fome, tedio)

class Fazenda:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def alimentar_todos(self, qtdcomida):
        for animal in self.animais:
            animal.alimentar(qtdcomida)

    def brincar_todos(self, horas):
        for animal in self.animais:
            animal.brincar(horas)

    def exibir_status_todos(self):
        for i, animal in enumerate(self.animais, 1):
            print(f"Animal {i}: {animal.get_status()}")

fazendateste = Fazenda()
fazendateste.adicionar_animal(Porco())
fazendateste.adicionar_animal(Galinha())
fazendateste.adicionar_animal(Vaca())

print("Status inicial dos animais:")
fazendateste.exibir_status_todos()

print("\nAlimentando todos com 3 unidades de comida.")
fazendateste.alimentar_todos(3)
fazendateste.exibir_status_todos()

print("\nBrincando com todos por 2 horas.")
fazendateste.brincar_todos(2)
fazendateste.exibir_status_todos()

while True:
    print("\n===== MENU DA FAZENDA =====")
    print("1 - Adicionar animal")
    print("2 - Alimentar todos")
    print("3 - Brincar com todos")
    print("4 - Exibir status")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tipo = input("Qual animal deseja adicionar? (porco/galinha/vaca): ").strip().lower()
        if tipo in ["porco", "galinha", "vaca"]:
            nome = input("Dê um nome para o animal: ").strip()
            fazenda.adicionar_animal(tipo, nome)
            print(f"{nome} foi adicionado(a) à fazenda!")
        else:
            print("Tipo inválido! Escolha entre porco, galinha ou vaca.")

    elif opcao == "2":
        if not fazenda.animais:
            print("\nNão há animais para alimentar!")
        else:
            qtd = int(input("Quanto de comida deseja fornecer? "))
            fazenda.alimentar_todos(qtd)
            print("\nTodos os animais foram alimentados!")

    elif opcao == "3":
        if not fazenda.animais:
            print("\nNão há animais para brincar!")
        else:
            horas = int(input("Quantas horas deseja brincar? "))
            fazenda.brincar_todos(horas)
            print("\nTodos os animais se divertiram!")

    elif opcao == "4":
        fazenda.exibir_status_todos()

    elif opcao == "5":
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")