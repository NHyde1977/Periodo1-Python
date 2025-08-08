class Nodo:
    def __init__(self, dado=0, proximo=None):
        self.dado = dado
        self.proximo = proximo

    def __repr__(self):
        return f'{self.dado} -> {self.proximo}'

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def put(self, valor):
        novo = Nodo(valor)
        if self.ultimo:
            self.ultimo.proximo = novo
        self.ultimo = novo
        if not self.primeiro:
            self.primeiro = novo

    def get(self):
        if not self.primeiro:
            return None
        valor = self.primeiro.dado
        self.primeiro = self.primeiro.proximo
        if not self.primeiro:
            self.ultimo = None
        return valor

    def esta_vazia(self):
        return self.primeiro is None

fila_senac = Fila()
