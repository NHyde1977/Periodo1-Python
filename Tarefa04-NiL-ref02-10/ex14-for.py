from itertools import count

numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(10)]
cont_par = 0
cont_impar = 0

for num in numeros:
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"Números Pares: {cont_par}\nNúmeros Ímpares: {cont_impar}")