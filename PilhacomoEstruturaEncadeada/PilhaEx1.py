import random

class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado=dado
        self.anterior= nodo_anterior

    def __repr__(self):
        return f"{self.dado} -> {self.anterior}"

class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)

        novo_nodo.anterior = self.topo

        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossível remover valor da pilha vazia."

        self.topo = self.topo.anterior

def maior_elemento(pilha):
    assert pilha.topo is not None, "Pilha está vazia."

    atual = pilha.topo
    maior = atual.dado

    while atual is not None:
        if atual.dado > maior:
            maior = atual.dado
        atual = atual.anterior #vai para próximo nodo da pilha

    return maior

p = Pilha()
for i in range(4):
    valor = random.randint(1,50)
    print(f"valor inserido: {valor}")
    p.insere(valor)

print("Pilha", p)
print(maior_elemento(p))