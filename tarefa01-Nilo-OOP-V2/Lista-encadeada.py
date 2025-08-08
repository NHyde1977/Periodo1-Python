class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:
    def __init__(self):
        self.cabeca = None

    def inserir(self, valor):
        novo = Nodo(valor)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def buscar(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return atual
            atual = atual.proximo
        return None

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual:
            if atual.valor == valor:
                if anterior:
                    anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def remover_duplicatas(self):
        atual = self.cabeca
        while atual and atual.proximo:
            if atual.valor == atual.proximo.valor:
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(f"{atual.valor} → ", end="") #formatação sugerida pela IA
            atual = atual.proximo
        print("None")

lista = Lista()
for v in [0, 1, 1, 5, 7, 10, 10]:
    lista.inserir(v)

print("Antes de remover duplicatas:")
lista.exibir()

lista.remover_duplicatas()

print("Depois de remover duplicatas:")
lista.exibir()