def fatoriald (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatoriald(n-2)

nf = int(input("indique o número para o calculo do FatorialDuplo: "))
print(f'O fatorial de {nf} é {fatoriald(nf)}')
