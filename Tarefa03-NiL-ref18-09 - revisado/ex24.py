n1 = float(input("Indique um número: "))
n2 = float(input("Indique outro número: "))
op = input("Qual operação quer fazer? Indique 'soma', 'subt', 'multip' ou 'div'")

soma = n1 + n2
subt = n1 - n2
multip = n1 * n2
div =  n1 / n2
fs = soma.is_integer()
fss = subt.is_integer()
fmp = multip.is_integer()
fdiv = div.is_integer()

if op == "soma":
    print(soma)
    if soma / 2:
        print("número par")
    else:
        print("numero ímpar")
    if soma >=0:
        print("Número positivo")
    else:
        print("Número negativo")
    if fs == True:
        print("número inteiro")
    else:
        print("número decimal")
elif op == "subt":
    print(subt)
    if subt / 2:
        print("número par")
    else:
        priny("numero ímpar")
    if subt >=0:
        print("Número positivo")
    else:
        print("Número negativo")
    if fss == True:
        print("número inteiro")
    else:
        print("número decimal")
elif op == "multip":
    print(multip)
    if (div / 2) and (div % 2 == 0):
        print("número par")
    else:
        print("numero ímpar")
    if multip >= 0:
        print("Número positivo")
    else:
        print("Número negativo")
    if fmp == True:
        print("número inteiro")
    else:
        print("número decimal")
elif op == "div":
    print(div)
    if div % 2 == 0:
        print("número par")
    else:
        print("numero ímpar")
    if div >= 0:
        print("Número positivo")
    else:
        print("Número negativo")
    if fdiv == True:
        print("número inteiro")
    else:
        print("número decimal")
else:
    print("operação inválida")