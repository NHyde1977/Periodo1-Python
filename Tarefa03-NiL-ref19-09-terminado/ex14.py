n1 = float(input('Digite um valor: '))
n2 = float(input('Digite um valor: '))
md = ((n1 + n2)/2)

if (md >= 9) or (md == 10):
    print("conceito A")
    print (n1)
    print(n2)
    print(md)
    print ("Aprovado")
elif (md >= 7.5) and (md <= 8.9):
    print("conceito B")
    print(n1)
    print(n2)
    print(md)
    print("Aprovado")
elif (md >= 6) and (md <= 7.4):
    print("conceito C")
    print(n1)
    print(n2)
    print(md)
    print("Aprovado")
elif (md >= 4) and (md <= 5.9):
    print("conceito D")
    print(n1)
    print(n2)
    print(md)
    print("Reprovado")
elif (md >= 0) and (md <= 3.9):
    print("conceito E")
    print(n1)
    print(n2)
    print(md)
    print("Reprovado")
else:
    print("conceito não reconhecido")