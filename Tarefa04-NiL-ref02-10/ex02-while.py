user = input("Informe o nome de usuário: ")
password = input("Informe o nome de usuário: ")
validation = True

while validation:
    if not user == password:
        validation = False
        print("User autenticated")
    else:
        validation = True
        print("User = Password. Tente novamente")
        user = input("Informe o nome de usuário: ")
        password = input("Informe o nome de usuário: ")
