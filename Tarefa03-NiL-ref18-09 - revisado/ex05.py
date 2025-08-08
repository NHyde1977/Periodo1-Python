nota1 = float(input("indique a primeira nota: "))
nota2 = float(input("indique a segunda nota: "))
media = ((nota1 + nota2)/2)

if (media > 7) or (media == 7):
    print("Aprovado")
    if (media == 10):
        print("Aprovado com Distinção")
    else:
        print("reprovado")
else:
    print("Reprovado")