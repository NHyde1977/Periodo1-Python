while True:
    n = int(input("Digite um número qualquer ou 0 para sair: "))

    if n == 0:
        print("Programa encerrado")
        break

    if n < 1:
        print("Número inválido. Por favor, digite um número positivo!")
        continue

    total_divisoes = 0
    primos = []

    for num in range(2, n + 1):
        is_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            total_divisoes = total_divisoes+1
            if num % i ==0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    print(f"Números primos entre 1 e {n}: {', '.join(map(str, primos))}")
    print(f"Número total de divisões executadas: {total_divisoes}")