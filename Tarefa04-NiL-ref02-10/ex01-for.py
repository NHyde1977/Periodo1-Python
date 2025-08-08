for _ in range(100):  # Um limite de iterações, pode ser ajustado
    nota = input("Digite a nota: ")
    if int(nota) in range(11):  # range(11)
        print("Nota válida...")
        break  # Sai do loop se a nota for válida
    else:
        print("Nota Inválida - repita o processo...")
