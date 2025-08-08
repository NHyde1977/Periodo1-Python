class Nodo:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado=dado
        self.anterior= nodo_anterior

    def __repr__(self):
        return '% -> %s' % (self.dado, self.anterior)

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
