num = float(input("Indique um número? "))

resultado = num.is_integer()

if resultado == True:
    print("É um número inteiro")
else:
    print("É um número decimal")