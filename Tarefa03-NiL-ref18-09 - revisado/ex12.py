vh = float(input("Qual o valor da sua hora? "))
ht = int(input("Quantas horas trabalhou no mês? "))
sal = vh*ht

dir1 = 0
dir2 = 0.05
dir3 = 0.1
dir4 = 0.2

sind = 0.03
fgts = 0.11
inss = 0.1

if sal <= 900:
    print("salário bruto: ", sal)
    print(" (-) IR", dir1, (sal*dir1))
    print(" (-) INSS", inss, (sal*inss))
    print("FGTS ", fgts, (sal*fgts))
    print("Total de descontos", (dir1*sal)+(inss*sal))
    print("salário líquido", sal-((dir1*sal)+(inss*sal)))

elif sal <= 1500:
    print("salário bruto: ", sal)
    print(" (-) IR", dir2, (sal * dir2))
    print(" (-) INSS", inss, (sal * inss))
    print("FGTS ", fgts, (sal * fgts))
    print("Total de descontos", (dir2 * sal) + (inss * sal))
    print("salário líquido", sal - ((dir2 * sal) + (inss * sal)))

elif sal <= 2500:
    print("salário bruto: ", sal)
    print(" (-) IR", dir2, (sal * dir3))
    print(" (-) INSS", inss, (sal * inss))
    print("FGTS ", fgts, (sal * fgts))
    print("Total de descontos", (dir3 * sal) + (inss * sal))
    print("salário líquido", sal - ((dir3 * sal) + (inss * sal)))

elif sal > 2500:
    print("salário bruto: ", sal)
    print(" (-) IR", dir2, (sal * dir4))
    print(" (-) INSS", inss, (sal * inss))
    print("FGTS ", fgts, (sal * fgts))
    print("Total de descontos", (dir4 * sal) + (inss * sal))
    print("salário líquido", sal - ((dir4 * sal) + (inss * sal)))