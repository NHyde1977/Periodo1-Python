# 2. Encontre o maior elemento em uma BST.


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

def buscarmaiord(raiz):
    if raiz.direita is None:
        return raiz
    else:
        return buscarmaiord(raiz.direita)

def buscarmaiore(raiz):
    if raiz is None or raiz.esquerda is None:
        return None
    nodo = raiz.esquerda
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo

raiz = NodoArvore(7)
raiz.esquerda = NodoArvore(2)
raiz.esquerda.esquerda = NodoArvore(1)
raiz.esquerda.direita = NodoArvore(5)
raiz.esquerda.direita.direita =NodoArvore(7)
raiz.esquerda.direita.esquerda =NodoArvore(4)
raiz.direita =NodoArvore(14)
raiz.direita.esquerda =NodoArvore(8)
raiz.direita.direita = NodoArvore(17)

maior = buscarmaiord(raiz)
print(f"O menor valor da árvore à direita é: {maior.chave}")
maior = buscarmaiore(raiz)
print(f"O menor valor da árvore à esquerda é: {maior.chave}")