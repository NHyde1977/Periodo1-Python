# 5. Verifique se uma árvore binária é balanceada.

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

def alturamax(raiz):
    if raiz is None:
        return 0
    else:
        altura_esquerda = alturamax(raiz.esquerda)
        altura_direita = alturamax(raiz.direita)
        return max(altura_esquerda, altura_direita)+1

def alturamin(raiz):
    if raiz is None:
        return 0
    else:
        altura_esquerda = alturamin(raiz.esquerda)
        altura_direita = alturamin(raiz.direita)
        return min(altura_esquerda, altura_direita)+1

print("Altura máxima: ", (alturamax(raiz)))
print("Altura mínima: ", (alturamin(raiz)))

def eh_balanceada(raiz):
    if raiz is None:
        return True

    altura_esq = alturamax(raiz.esquerda)
    altura_dir = alturamax(raiz.direita)

    if abs(altura_esq - altura_dir) > 1: #o 'abs' é a função que desconsidera o sinal final da operação, ela pega só
                                         #o valor absoluto
        return False

    return eh_balanceada(raiz.esquerda) and eh_balanceada(raiz.direita)
    print("Essa árvore é balanceada!")

if eh_balanceada(raiz) is True:
    print("Essa árvore é balanceada!")
else:
    print("Essa árvore não é balanceada!")