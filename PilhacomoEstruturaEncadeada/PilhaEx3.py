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

        #self.topo = self.topo.anterior
        dado_removido = self.topo.dado  # GPT: guarda o valor antes de remover
        self.topo = self.topo.anterior  # GTP: atualiza o topo
        return dado_removido

def maior_elemento(pilha):
    assert pilha.topo is not None, "Pilha está vazia."

    atual = pilha.topo
    maior = atual.dado

    while atual is not None:
        if atual.dado > maior:
            maior = atual.dado
        atual = atual.anterior #vai para próximo nodo da pilha

    return maior

def pilhas_iguais(p1, p2):
    nodoatual1 = p1.topo
    nodoatual2 = p2.topo

    while nodoatual1 is not None and nodoatual2 is not None:
        if nodoatual1.dado != nodoatual2.dado:
            return False  # elemento diferente
        nodoatual1 = nodoatual1.anterior
        nodoatual2 = nodoatual2.anterior

    # Se um terminou antes do outro, têm tamanhos diferentes
    if nodoatual1 is not None or nodoatual2 is not None:
        return False

    return True  # pilhas são idênticas

p1 = Pilha()
p2 = Pilha()

for valor in [1, 2, 3, 4, 5]:
    p1.insere(valor)
    p2.insere(valor)

print("Pilha 1:", p1)
print("Pilha 2:", p2)
print("As pilhas são iguais?", pilhas_iguais(p1, p2))

p1.insere(4)
print("Pilha 1:", p1)
print("Pilha 2:", p2)
print("As pilhas são iguais após inserção?", pilhas_iguais(p1, p2))

p1.insere(6)
print("Pilha 1:", p1)
print("Pilha 2:", p2)
print("As pilhas são iguais após inserção?", pilhas_iguais(p1, p2))  # Deve imprimir False