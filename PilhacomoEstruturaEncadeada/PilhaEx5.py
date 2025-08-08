class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return f"{self.dado} -> {self.anterior}"

class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, dado):
        nodo = Nodo(dado)
        nodo.anterior = self.topo
        self.topo = nodo

    def remove(self):
        if self.topo is None:
            print("Pilha vazia. Nada a remover.")
            return None
        dado_removido = self.topo.dado
        self.topo = self.topo.anterior
        return dado_removido

    def esta_vazia(self):
        return self.topo is None

def TPilha(lista):
    pilha = Pilha()

    for numero in lista:
        print(f"\nNúmero lido: {numero}")
        if numero % 2 == 0:
            print(f"Par -> empilha {numero}")
            pilha.insere(numero)
        else:
            print(f"Ímpar -> tenta desempilhar")
            pilha.remove()

    print("\nEsvaziando a pilha:")
    while not pilha.esta_vazia():
        valor = pilha.remove()
        print(f"Desempilhado: {valor}")

numeros = [5, 8, 10, 3, 2, 6, 9, 4, 11, 14, 7, 18, 13, 20, 22]
TPilha(numeros)