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

    def imprimir(self):
        atual = self.primeiro
        while atual:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()  # Para quebrar linha após imprimir a fila

    def inverter(self):
        anterior = None
        atual = self.primeiro
        self.ultimo = self.primeiro  # O antigo primeiro vira o novo último

        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo

        self.primeiro = anterior  # O último elemento visitado vira o novo primeiro

f = Fila()
f.push(1)
f.push(4)
f.push(5)
f.push(2)

print("Antes de inverter:")
f.imprimir()  # Saída: 1 4 5 2

f.inverter()

print("Depois de inverter:")
f.imprimir()  # Saída: 2 5 4 1


