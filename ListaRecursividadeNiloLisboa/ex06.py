def potencia (k, n):
    if n == 0:
        return 1
    else:
        return k * potencia(k, n - 1)

base = int(input("Digite um número para a base da potencia: "))
pot = int(input("Digite um número da potencia: "))
print(f"o resultado é  {potencia(base, pot)}")