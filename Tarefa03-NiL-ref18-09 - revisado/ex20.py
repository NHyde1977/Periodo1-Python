n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

md = (n1+n2+n3)/3

if (md >= 7) and (md <10):
    print("Aprovado - ", "média :", md)
elif md <= 5:
    print("Reprovado - ", "média :", md)
elif md == 10:
    print("Aprovado com distinção - ", "média :", md)
else:
    print("Valor inválido")