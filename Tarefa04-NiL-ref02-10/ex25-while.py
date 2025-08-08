idade_lista = []
idade_indicadas = 0
soma_das_idades = 0

while True:
    idade = int(input("Digite a idade (em anos) para a série de cálculos (valores inteiros e positivos): "))

    if idade >= 0:
        idade_lista.append(idade)
        idade_indicadas += 1
        soma_das_idades += idade

        media = soma_das_idades / idade_indicadas
        print(f"Média acumulada das notas: {media:.2f}")
        if media <= 25:
            print("A amostra é majoritariamente jovem")
        elif (media == 26 or media < 60):
            print("A amostra é majoritariamente Adulta")
        elif media >= 60:
            print("A amostra é majoritariamente Idosa")

    else:
        print("Dado inválido. Por favor, digite um número!")
