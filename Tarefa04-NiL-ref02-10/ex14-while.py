from itertools import count

numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(10)]
cont_par = 0
cont_impar = 0
i = 0

while i < len(numeros):
    num = numeros[i]
    if num % 2 == 0:
        cont_par = cont_par + 1
    else:
            cont_impar = cont_impar + 1
    i = i + 1
print(f"Números Pares: {cont_par}\nNúmeros Ímpares: {cont_impar}")
