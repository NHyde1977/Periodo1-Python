class Nodo:
    def __init__(self, dado=0, anterior=None):
        self.dado = dado
        self.anterior = anterior

    def __repr__(self):
        return f"{self.dado} -> {self.anterior}"

class Pilha:
    def __init__(self):
        self.topo = None

    def insere(self, dado):
        novo = Nodo(dado)
        novo.anterior = self.topo
        self.topo = novo

    def remove(self):
        if self.topo is None:
            print("Pilha vazia. Nada a remover.")
            return None
        removido = self.topo.dado
        self.topo = self.topo.anterior
        return removido

    def esta_vazia(self):
        return self.topo is None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

def TPilha2(lista):
    P = Pilha()  # Positivos
    N = Pilha()  # Negativos

    for numero in lista:
        print(f"\nNúmero lido: {numero}")
        if numero > 0:
            print(f"Inserindo {numero} na pilha P")
            P.insere(numero)
        elif numero < 0:
            print(f"Inserindo {numero} na pilha N")
            N.insere(numero)
        else:  # número == 0
            print("Número zero -> desempilhando de ambas as pilhas")
            P.remove()
            N.remove()

    print("\nConteúdo final da pilha P (positivos):", P)
    print("Conteúdo final da pilha N (negativos):", N)

valores = [3, -1, 5, 0, 10, 0, -9, -4, 1, 7, 0, 8, -2, 0]
TPilha2(valores)
