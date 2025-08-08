# 3. Verifique se duas árvores binárias são idênticas.


class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

def identicas(arvore1, arvore2):
    if arvore1 is None and arvore2 is None:
        return True
    elif arvore1 is not None and arvore2 is not None:
        return (arvore1.chave == arvore2.chave and
                identicas(arvore1.esquerda, arvore2.esquerda) and
                identicas(arvore1.direita, arvore2.direita))
    else:
        return False

t1 = NodoArvore(2, NodoArvore(2), NodoArvore(3))
t2 = NodoArvore(2, NodoArvore(2), NodoArvore(3))
t3= NodoArvore(5, NodoArvore(6), NodoArvore(4))

if (identicas(t1, t2)) == True:
    print("árvores são identicas")
else:
    print("árvores NÃO são identicas")
if (identicas(t2, t3)) == True:
    print("árvores são identicas")
else:
    print("árvores NÃO são identicas")
