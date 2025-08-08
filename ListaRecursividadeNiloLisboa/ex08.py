def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

resultado = mdc(x, y)
print(f"O MDC de {x} e {y} é {resultado}")