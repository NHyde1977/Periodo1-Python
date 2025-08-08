l1 = float(input('Digite um número: '))
l2 = float(input('Digite um número: '))
l3 = float(input('Digite um número: '))

if (l1+l2 > l3) or (l1+l3 > l2) or (l2+l3 > l1):
    print ("forma um triangulo")
    if (l1 == l2) or (l2 == l3) or (l1 == l3):
        print ("triangulo Isósceles")
    elif (l1 == l2 == l3):
        print ("triangulo Equilátero")
    elif (l1 != l2) and (l1 != l3) and (l2 != l3):
        print("triangulo Escaleno")
else:
    print("não é um triangulo")