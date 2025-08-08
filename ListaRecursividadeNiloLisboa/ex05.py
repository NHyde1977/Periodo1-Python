def somar (n):
    if n == 1:
        return 1
    elif n > 1:
        return n + somar(n - 1)

num = int(input("Digite um número para somar recursivamente: "))
print(f"A soma é {somar(num)}")