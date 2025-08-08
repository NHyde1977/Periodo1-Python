# n = int(input("Digite um número: "))
# fat = 1
# for i in range(1, n+1):
#     fat = fat * i
# if n > 0 and n < 17:
#     print(f"O valor do fatorial foi {fat}")
# else:
#     print("Número inválido")
# while True:
#     n = int(input("Digite um número: "))
#     fat = 1
#     for i in range(1, n + 1):
#         fat = fat * i
#         if n > 0 and n < 17:
#             print(f"O valor do fatorial foi {fat}")
#         else:
#             print("Número inválido")


while True:
    n = int(input("Digite um número (entre 1 e 16, ou 0 para sair): "))

    if n == 0:
        print("Terminado")
        break  # Permite sair do loop

    if n > 0 and n < 17:
        fat = 1
        for i in range(1, n + 1):
            fat *= i
        print(f"O valor do Fatorial de {n} é {fat}")
    else:
        print("Número inválido. Por favor, digite um número entre 1 e 16!")