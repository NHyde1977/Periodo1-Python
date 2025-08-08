lista = []
contador = 0

while contador < 5:
    numero = float(input(f'Indique o {contador + 1}º número: '))
    lista.append(numero)
    contador = contador + 1

soma = sum(lista)
media = soma / len(lista)

print(f'Soma : {soma}')
print(f'Média : {media}')
