def produtorio (n):
    if n == 1:
        return 1
    else:
        return n * produtorio(n - 1)

num = int(input("Digite um número inteiro positivo para calcular o produtório: "))
print(f"O produtório de 1 a {num} é {produtorio(num)}")