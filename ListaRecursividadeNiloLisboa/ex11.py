def Multip_Rec(n1, n2):
    if n1 == 0:
        return 0
    else:
        return n2 + Multip_Rec(n1 - 1, n2)

n1 = int(input("Digite o primeiro número inteiro (positivo): "))
n2 = int(input("Digite o segundo número inteiro (positivo): "))

resultado = Multip_Rec(n1, n2)
print(f"O resultado de {n1} x {n2} é {resultado}")