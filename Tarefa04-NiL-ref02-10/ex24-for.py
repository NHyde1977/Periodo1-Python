import sys
notas_lista = []
notas_indicadas = 0
soma_das_notas = 0

for i in range(sys.maxsize**10):
    nota = int(input("Digite a nota para a série de cálculos (valores de zero a 10): "))

    if nota >= 0:
        notas_lista.append(nota)
        notas_indicadas += 1
        soma_das_notas += nota

        media = soma_das_notas / notas_indicadas
        print(f"Média acumulada das notas: {media:.2f}")

    else:
        print("Dado inválido. Por favor, digite um número!")
