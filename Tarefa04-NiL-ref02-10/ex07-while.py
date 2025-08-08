contador = 0
maior_numero_inicial = float('-1000000000000000000000000000000000000000000000000')

while contador < 5:
    numero = float(input(f'Indique o {contador + 1}º número: '))

    if numero > maior_numero_inicial:
        maior_numero_inicial = numero

    contador = contador + 1

# Exibe o maior número encontrado
print(f'O maior número informado foi: {maior_numero_inicial}')
