# Esse foi bem chatGPT forte
import random

vetor = [round(random.uniform(0, 100), 2) for i in range(100)]
print(vetor)

def invertv (vetor, inicio, fim):
    if inicio >= fim:
        return
    else:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        invertv(vetor, inicio + 1, fim - 1)

invertv(vetor, 0, len(vetor) - 1)

print("\nVetor invertido:")
print(vetor)