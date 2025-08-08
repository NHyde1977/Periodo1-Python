def somavetor (vetor):
    if len(vetor) == 0:
        return 0
    elif len(vetor) == 1:
        return vetor[0]
    else:
        return vetor[0] + somavetor(vetor[1:])

vteste = [1,4,7]
print(somavetor(vteste))