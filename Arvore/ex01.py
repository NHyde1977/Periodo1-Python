# 1. Encontre o menor elemento em uma BST.


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

def buscarmenore(raiz):
    if raiz.esquerda is None:
        return raiz
    else:
        return buscarmenore(raiz.esquerda)

def buscarmenord(raiz):
    if raiz.direita is None:
        return raiz
    else:
        return raiz.direita


raiz = NodoArvore(7)
raiz.esquerda = NodoArvore(2)
raiz.esquerda.esquerda = NodoArvore(1)
raiz.esquerda.direita = NodoArvore(5)
raiz.esquerda.direita.direita =NodoArvore(7)
raiz.esquerda.direita.esquerda =NodoArvore(4)
raiz.direita =NodoArvore(14)
raiz.direita.esquerda =NodoArvore(8)
raiz.direita.direita = NodoArvore(17)

menor = buscarmenord(raiz)
print(f"O menor valor da árvore à direita é: {menor.chave}")
menor = buscarmenore(raiz)
print(f"O menor valor da árvore à esquerda é: {menor.chave}")
