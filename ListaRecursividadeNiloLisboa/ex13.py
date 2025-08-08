def imprimirdescrecente(n):
    if n == 0:
        print(0)
    else:
        print(n)
        imprimirdescrecente(n - 1)


num = int(input("Digite um número inteiro positivo: "))
imprimirdescrecente(num)