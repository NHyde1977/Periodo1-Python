n1 = int(input("indique o primeiro número"))
n2 = int(input("indique o segundo número"))
n3 = int(input("indique o terceiro número"))

if (n1 < n2) and (n1 < n3):
    print("O menor número é o :", n1)
elif (n2 < n1) and (n2 < n3):
        print("O menor número é o :", n2)
elif (n3 < n1) and (n3 < n2):
        print("O menor número é o :", n3)

else:
    print("Há dois ou mais números iguais")