nome = None
senha = None

while (nome==senha):
    nome = input("Digite o Nome: ")
    senha = input("Digite a senha: ")
    if nome==senha:
        print("Valores inválidos - digite novamente")

print("Nome e senhas OK")