litro = float(input("Quantos litros deseja abastecer? "))
comb = (input("Qual combustível deseja abastecer? 'A-álcool, G-gasolina'"))

pa = 1.9
pg = 2.5

at1 = (litro * pa)*0.97
at2 = (litro * pa)*0.95

gt1 = (litro * pg)*0.96
gt2 = (litro * pg)*0.94

if (litro <=20) and (comb == "A"):
    print(at1)
elif (litro >20) and (comb == "A"):
    print(at2)
elif (litro <=20) and (comb == "G"):
    print(gt1)
elif (litro >20) and (comb == "G"):
    print(gt2)
else:
    print("dados inválidos")