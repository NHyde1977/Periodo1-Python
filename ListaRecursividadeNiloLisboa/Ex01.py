def fatorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

nf = int(input("indique o número para o calculo do Fatorial: "))
print(f'O fatorial de {nf} é {fatorial(nf)}')
