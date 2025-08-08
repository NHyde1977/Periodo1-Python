def calcfibo (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcfibo(n-1)+calcfibo(n-2)

numfibo = int(input("indique o número para da posição correspondente na sequencia de Fibonacci: "))
print(f'O valor da posição de número {numfibo} é {calcfibo(numfibo)}')
