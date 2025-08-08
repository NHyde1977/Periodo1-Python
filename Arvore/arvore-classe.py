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

# def imprimir_arvore(no, nivel=0):
#     if no is not None:
#         imprimir_arvore(no.direita, nivel+1)
#         print('    ' * nivel + f'-> {no.chave}')
#         imprimir_arvore(no.esquerda, nivel +1)
#
# # print("imprimir árvore:")
# # imprimir_arvore(raiz)

def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)

    print(raiz.chave)

    em_ordem(raiz.direita)

em_ordem(raiz)

def pre_ordem(raiz):
    if not raiz:
        return
    print(raiz.chave)
    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave)


def insere (raiz, nodo):
    if raiz is None:
        raiz = nodo

    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def busca(raiz,chave):
    if raiz is None:
        return None

    if raiz.chave == chave:
        return raiz

    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    return busca(raiz.esquerda, chave)

raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
em_ordem(raiz)

for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))