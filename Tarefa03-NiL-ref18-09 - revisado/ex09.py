#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print (n3, n2, n1)
elif n2 > n1 and n2 > n3 and n3 > n1:
    print (n1, n3, n2)
elif n3 > n1 and n3 > n2 and n2 > n1:
    print (n1, n2, n3)
else:
    print("há um ou mais números iguais")
