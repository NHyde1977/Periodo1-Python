while True:
    nome = input("Escreva seu nome: ")
    if len(nome) <= 3:
        nome = False
        print("Nome com menos de 3 caracteres. Por favor repita")
    else:
        break
while True:
    idade = int(input("Qual a sua idade? "))
    if (idade < 0) or (idade > 150):
        idade = False
        print("Idade inválida. Por favor repita")
    else:
        break
while True:
    sal = float(input("Qual o seu salário? "))
    if sal <= 0:
        sal = False
        print("Dado de salário inválid0. Por favor repita")
    else:
        break
while True:
    sex = input("Qual o seu sexo? Indique 'F' ou 'M': ")
    if sex == "M" or sex == "F":
        sex = False
        print("Dado inválido, por favor repita")
    else:
        break
while True:
    ecivil = input("Qual o seu estado civil? Indique 'c', 's', 'v' ou 'd'")
    if (ecivil == "c") or (ecivil == "s") or (ecivil == "v") or (ecivil == "d"):
        break
    else:
        print("Dado inválido, por favor repita")

print(f'Os dados informados foram: \nnome {nome}\nidade [{idade}\nSalário {sal}\nSexo {sex}\nEstado Cicil {ecivil}')