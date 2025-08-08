# Representa cada processo na fila
class Processo:
    def __init__(self, pid, nome):
        self.pid = pid
        self.nome = nome

    def __repr__(self):
        return f"PID: {self.pid}, Nome: {self.nome}"

# Nó da fila
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

# Fila dinâmica para gerenciar processos
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def push(self, dado):  # Adiciona um processo ao final da fila
        novo = Nodo(dado)
        if self.primeiro is None:
            self.primeiro = novo
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo

    def pop(self):  # Executa (remove) o primeiro processo da fila
        if self.primeiro is None:
            raise IndexError("Fila vazia")

        removido = self.primeiro
        self.primeiro = self.primeiro.proximo

        if self.primeiro is None:
            self.ultimo = None

        return removido.dado

    def matar_mais_antigo(self):  # Mata o processo com mais tempo de espera
        return self.pop()

    def __repr__(self):  # Imprime a fila de processos
        atual = self.primeiro
        elementos = []
        while atual:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return "Fila de Processos:\n" + "\n".join(elementos)

# Criando a fila
fila = Fila()

# Inserindo processos
fila.push(Processo(1, "Chrome"))
fila.push(Processo(2, "VSCode"))
fila.push(Processo(3, "Photoshop"))
fila.push(Processo(input("Indique o ID do aplicativo: "),input("Indique o ID do aplicativo: ")))

print(fila)

print("\nExecutando processo:", fila.pop())

# Mata o processo com maior tempo de espera - após o pop acima é o segundo da fila de execução.
print("\nMatando processo mais antigo:", fila.matar_mais_antigo())

print("\nFila após as operações:")
print(fila)