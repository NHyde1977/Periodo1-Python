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

    def insere(self, novo_dado):
        novo_nodo = Nodo(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Pilha vazia"
        dado_removido = self.topo.dado
        self.topo = self.topo.anterior
        return dado_removido

    def esta_vazia(self):
        return self.topo is None

    def contem(self, valor):
        atual = self.topo
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.anterior
        return False

# Cria a rua como uma pilha
rua = Pilha()

# Adiciona carros (placas fictícias)
placas = [111, 222, 333, 444, 555]
for placa in placas:
    rua.insere(placa)

print("placas em ordem na rua:", rua)

# Placa a ser retirada
placa_desejada = 333

if not rua.contem(placa_desejada):
    print(f"Carro com placa {placa_desejada} não está na rua.")
else:
    ruaauxiliar = Pilha()
    print(f"\nRetirando carros para liberar a placa {placa_desejada}:")

    # Remove carros até achar a placa desejada
    while True:
        placa = rua.remove()
        if placa == placa_desejada:
            print(f"Carro {placa} saiu da rua.")
            break
        else:
            print(f"Carro {placa} retirado temporariamente.")
            ruaauxiliar.insere(placa)