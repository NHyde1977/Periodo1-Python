# 6. Determine se uma árvore é simétrica.

class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return f'{self.esquerda and self.esquerda.chave} <- {self.chave} -> {self.direita and self.direita.chave}'

def eh_espelho(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (a.chave == b.chave and
            eh_espelho(a.esquerda, b.direita) and
            eh_espelho(a.direita, b.esquerda))
#a func. diz se as duas sub-árvores são idênticas (falso/verdadeiro)

def eh_simetrica(raiz):
    if raiz is None:
        return True
    return eh_espelho(raiz.esquerda, raiz.direita)
#a func. pega a raiz, checa os lados esquerdo(A) e direito(B) c/ a função acima.

raiz_simetrica = NodoArvore(1,
    NodoArvore(2,
        NodoArvore(3),
        NodoArvore(4)
    ),
    NodoArvore(2,
        NodoArvore(4),
        NodoArvore(3)
    )
)

raiz_nao_simetrica = NodoArvore(1,
    NodoArvore(2,
        None,
        NodoArvore(3)
    ),
    NodoArvore(2,
        None,
        NodoArvore(3)
    )
)

print("Árvore simétrica?", eh_simetrica(raiz_simetrica))
print("Árvore simétrica?", eh_simetrica(raiz_nao_simetrica))
