while True:
    n = int(input("Digite um número qualquer ou 0 para sair: "))

    if n == 0:
        print("Programa encerrado")
        break

    if n < 1:
        print("Número inválido. Por favor, digite um número positivo!")
        continue

    divisores = []
    is_primo = True

    for i in range(2, int(n**0.5) + 1):
#O motivo de verificar apenas até a raiz quadrada de n é que,
# se n tem um divisor maior que sua raiz quadrada,
# então deve ter um divisor menor.
# Por exemplo, se um número n é divisível por algum número i maior que √n,
# a outra parte do produto n / i será um número menor que √n.
# Aparentemente fazendo isso, se reduz a quantidade de checks de "primalidade".
        if n % i == 0:
            divisores.append(i)
            if i != n // i:
# operador de divisão inteira.
# A linha if i != n // i: serve para evitar a adição de divisores duplicados à lista.
# Se i for igual a n // i, apenas um deles deve ser adicionado,
# garantindo que cada divisor seja listado uma única vez.
                divisores.append(n // i)
            is_primo = False
    if is_primo:
        print(f"O número {n} é primo.")
    else:
        divisores.sort()
        print(f"O número {n} não é primo. Ele é divisível por: {', '.join(map(str, divisores))}.")
