import math

tempo = 0

paisA = 80000*math.pow(1.03,tempo)
paisB = 200000*math.pow(1.015,tempo)

igualaram = True

while True:
    if paisA >= paisB:
        igualaram = True
        print("Esses são os anos que levam para ter a população semelhante: ", tempo)
        break
    else:
        tempo = tempo +1
        paisA = 80000*math.pow(1.03,tempo)
        paisB = 200000*math.pow(1.015,tempo)
        igualaram = False


