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

p = Pilha()
numeros = [1, 21, 32, 43, 54]

print("Números inseridos:")
for numero in numeros:
    print(numero)
    p.insere(numero)

# Tira da pilha e coloca na Lista:
lista_numeros = []
while p.topo is not None:
    valor = p.remove()
    lista_numeros.append(valor)

print("\nLista com os números retirados da pilha:", lista_numeros)

# Ordenação crescente
lista_numeros.sort()
print("Ordem crescente:", lista_numeros)

# Ordenação decrescente
lista_numeros.sort(reverse=True)
print("Ordem decrescente:", lista_numeros)