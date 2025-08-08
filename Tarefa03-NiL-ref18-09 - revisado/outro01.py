nota = input("Digite a nota: ")
not_valid = True

while not_valid:
    if int(nota) in range(11): # range(11)
        print("Nota válida...")
        not_valid = False
    else:
        not_valid = True
        print("Nota Inválida - repita o processo...")
        nota = input("Digite a nota: ")