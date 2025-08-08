def conta_digito(n, k):
    if n == 0:
        return 0
    elif n % 10 == k:
        return 1 + conta_digito(n // 10, k)
    else:
        return conta_digito(n // 10, k)

numero = int(input("Digite um número natural: "))
digito = int(input("Digite o dígito para procurar (de 0 até 9): "))

quantidade = conta_digito(numero, digito)
print(f"O dígito {digito} ocorre {quantidade} vezes em {numero}.")
