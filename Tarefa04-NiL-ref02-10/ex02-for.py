for _ in range(5):  # Um limite de tentativas, pode ser ajustado
    user = input("Informe o nome de usuário: ")
    password = input("Informe a senha: ")

    if user != password:
        print("User authenticated")
        break  # Sai do loop se o usuário for autenticado
    else:
        print("User = Password. Tente novamente")
else:
    print("Número máximo de tentativas atingido.")
