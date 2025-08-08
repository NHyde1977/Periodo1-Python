def imprimircrescente(n):
    if n == 0:
        print(0)
    else:
        imprimircrescente(n - 1)
        print(n)

num = int(input("Digite um número inteiro positivo: "))
imprimircrescente(num)