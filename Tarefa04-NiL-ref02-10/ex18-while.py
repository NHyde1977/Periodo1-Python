from itertools import count

numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(4)]
maior = max(numeros)
menor = min(numeros)

while True:
    print(f"Maior Número: {maior}\nMenor número: {menor}")
    break