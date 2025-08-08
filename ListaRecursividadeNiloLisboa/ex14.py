def imprimir_pares_crescente(n):
    if n == 0:
        print(0)
    else:
        imprimir_pares_crescente(n - 1)
        if n % 2 == 0:
            print(n)

num = int(input("Digite um número inteiro, positivo e par: "))
imprimir_pares_crescente(num)