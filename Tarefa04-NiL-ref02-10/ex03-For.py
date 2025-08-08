from itertools import count

# Para o nome
for _ in count():  # Loop infinito
    nome = input("Escreva seu nome: ")
    if len(nome) <= 3:
        print("Nome com menos de 3 caracteres. Por favor repita")
    else:
        break

# Para a idade
for _ in count():  # Loop infinito
    idade = int(input("Qual a sua idade? "))
    if idade < 0 or idade > 150:
        print("Idade inválida. Por favor repita")
    else:
        break

# Para o salário
for _ in count():  # Loop infinito
    sal = float(input("Qual o seu salário? "))
    if sal <= 0:
        print("Dado de salário inválido. Por favor repita")
    else:
        break

# Para o sexo
for _ in count():  # Loop infinito
    sex = input("Qual o seu sexo? Indique 'F' ou 'M': ").upper()
    if sex == 'F' or sex == 'M':
        break
    else:
        print("Dado inválido, por favor repita")

# Para o estado civil
for _ in count():  # Loop infinito
    ecivil = input("Qual o seu estado civil? Indique 'c', 's', 'v' ou 'd': ")
    if ecivil in ['c', 's', 'v', 'd']:
        break
    else:
        print("Dado inválido, por favor repita")

# Exibindo os dados informados
print(f'Os dados informados foram: \nnome: {nome}\nidade: {idade}\nSalário: {sal}\nSexo: {sex}\nEstado Civil: {ecivil}')
