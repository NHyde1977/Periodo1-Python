sal = float(input("Qual o seu salário?"))

sf1 = 0.2
sf2 = 0.15
sf3 = 0.1
sf4 = 0.05

if sal <= 280:
    print("salário antes do reajuste: ", sal)
    print("percentual de aumento aplicado: ", sf1)
    print("valor do aumento: ", (sf1*sal))
    print("novo salário, após o aumento: ", (sf1*sal)+sal)

elif (sal < 281) or (sal >= 700):
    print("salário antes do reajuste: ")
    print("percentual de aumento aplicado: ", sf2)
    print("valor do aumento: ", (sf2 * sal))
    print("novo salário, após o aumento: ", (sf2 * sal)+sal)

elif (sal < 700) or (sal >= 1500):
    print("salário antes do reajuste: ")
    print("percentual de aumento aplicado: ", sf3)
    print("valor do aumento: ", (sf3*sal))
    print("novo salário, após o aumento: ", (sf3*sal)+sal)

elif (sal < 1501):
    print("salário antes do reajuste: ")
    print("percentual de aumento aplicado: ", sf4)
    print("valor do aumento: ", (sf4*sal))
    print("novo salário, após o aumento: ", (sf4*sal)+sal)

else:
    print ("valor não reconhecido")