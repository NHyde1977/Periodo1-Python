# 4. Calcule a altura de uma BST.


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)


raiz = NodoArvore(7)
raiz.esquerda = NodoArvore(2)
raiz.esquerda.esquerda = NodoArvore(1)
raiz.esquerda.direita = NodoArvore(5)
raiz.esquerda.direita.direita =NodoArvore(7)
raiz.esquerda.direita.esquerda =NodoArvore(4)
raiz.direita =NodoArvore(14)
raiz.direita.esquerda =NodoArvore(8)
raiz.direita.direita = NodoArvore(17)

def altura(raiz):
    if raiz is None:
        return 0
    else:
        altura_esquerda = altura(raiz.esquerda)
        altura_direita = altura(raiz.direita)
        return max(altura_esquerda, altura_direita)+1

print(altura(raiz))