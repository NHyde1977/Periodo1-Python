lista = []

for contador in range(5):
    numero = float(input(f'Indique o {contador + 1}º número: '))
    lista.append(numero)

soma = sum(lista)
media = soma / len(lista)

print(f'Soma : {soma}')
print(f'Média : {media}')
