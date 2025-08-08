carne = input("Qual carne você deseja? Indique 'file', 'alcatra' ou 'picanha")
kgs = float(input("Quantos quilos você deseja? "))
cartao = input("Qual cartão você deseja usar? Indique 'T' para Tabajara e 'Q' para qualquer outros")

fd1 = 4.9
fd2 = 5.8
a1 = 5.9
a2 = 6.9
p1 = 6.9
p2 = 7.8
desc = 0.9

if carne == 'file' and kgs <= 5:
    if cartao == "T":
        print((kgs*fd1)*desc)
    else:
        print(kgs * fd1)
elif carne == 'file' and kgs > 5:
    if cartao == "T":
        print((kgs*fd2)*desc)
    else:
        print(kgs * fd2)
elif carne == 'alcatra' and kgs <= 5:
    if cartao == "T":
        print((kgs*a1)*desc)
    else:
        print(kgs * a1)
elif carne == 'alcatra' and kgs > 5:
    if cartao == "T":
        print((kgs*a2)*desc)
    else:
        print(kgs * a2)
elif carne == 'picanha' and kgs <= 5:
    if cartao == "T":
        print((kgs*p1)*desc)
    else:
        print(kgs * p1)
elif carne == 'picanha' and kgs > 5:
    if cartao == "T":
        print((kgs*p2)*desc)
    else:
        print(kgs * p2)