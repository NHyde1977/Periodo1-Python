import math

popA = int(input("Qual a população inicial do pais A? :"))
popB = int(input("Qual a população inicial do pais B? :"))

txA = (float(input("Qual a taxa % de crescimento de A"))/100)*1
txB = (float(input("Qual a taxa % de crescimento de B"))/100)*1

tempo = 0

paisA = popA*math.pow(txA,tempo)
paisB = popB*math.pow(txB,tempo)

igualaram = True

while True:
    if (paisA >= paisB) or (paisA <= paisB):
        igualaram = True
        print("Esses são os anos que levam para ter a população semelhante: ", tempo)
        repetir = input("Deseja realizar uma nova operação? : S/N")
        if repetir == "S":
            popA = int(input("Qual a população inicial do pais A? :"))
            popB = int(input("Qual a população inicial do pais B? :"))

            txA = (float(input("Qual a taxa % de crescimento de A")) / 100) * 1
            txB = (float(input("Qual a taxa % de crescimento de B")) / 100) * 1
        elif paisA >= paisB:
            igualaram = True
            print("Esses são os anos que levam para ter a população semelhante: ", tempo)
        elif paisA <= paisB:
            tempo = tempo + 1
            paisA = popA * math.pow(txA, tempo)
            paisB = popB * math.pow(txB, tempo)
            igualaram = False
        else:
            break

    else:
        tempo = tempo +1
        paisA = popA*math.pow(txA,tempo)
        paisB = popB*math.pow(txB,tempo)
        igualaram = False

