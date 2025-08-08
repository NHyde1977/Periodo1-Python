while True:
    n = int(input("Digite um número qualquer ou 0 para sair): "))

    if n == 0:
        print("Programa encerrado")
        break

    if n > 0 and n % 2 != 0:
        for _ in range(1):
            print(f"O número é primo")
    elif n > 0 and n % 2 == 0:
        for _ in range(1):
            print(f"O número é não é primo")
    else:
        print("Número inválido. Por favor, digite um número!")