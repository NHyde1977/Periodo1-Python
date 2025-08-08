l1 = float(input('Digite um número: '))
l2 = float(input('Digite um número: '))
l3 = float(input('Digite um número: '))

if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print("não é um triangulo")
elif l1 == l2 == l3:
    print('É um triângulo Equilátero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('É um triângulo Isósceles')
elif (l1 != l2) and (l1 != l3) and (l2 != l3):
    print('É um triângulo Escaleno')
