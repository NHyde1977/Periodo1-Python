num = int(input("indique um número inteiro (menor que 1000): "))

if num <1000:
    cen = num //100
    dez = (num%100) //10
    uni = num %10
    print(cen, "dezena(s)", dez, "dezena(s)", uni, "unidade(s)")
else:
    print("número maior ou igual que 1000")