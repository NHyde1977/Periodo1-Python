class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def push(self, dado):
        novo = Nodo(dado)
        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

    def pop(self):
        if self.primeiro is None:
            raise IndexError("Fila vazia")

        removido = self.primeiro
        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

        return removido.dado

    def __repr__(self):
        atual = self.primeiro
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "Fila: " + " -> ".join(elementos)

    def buscar(self, valor):
        atual = self.primeiro
        posicao = 0
        while atual:
            if atual.dado == valor:
                return posicao
            atual = atual.proximo
            posicao += 1
        return "valor não encontrado"

f = Fila()
f.push(10)
f.push(20)
f.push(30)

print(f.buscar(20))
print(f.buscar(40))
