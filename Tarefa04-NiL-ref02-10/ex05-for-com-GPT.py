import math
from itertools import count

# Função para calcular o crescimento populacional
def calcular_populacao(popA, popB, txA, txB):
    for tempo in count():  # Loop infinito
        paisA = popA * math.pow(1 + txA, tempo)
        paisB = popB * math.pow(1 + txB, tempo)

        if paisA >= paisB:
            print("Esses são os anos que levam para ter a população semelhante: ", tempo)
            return True
        else:
            continue

# Loop principal
while True:
    popA = int(input("Qual a população inicial do país A? : "))
    popB = int(input("Qual a população inicial do país B? : "))
    txA = float(input("Qual a taxa % de crescimento de A? : ")) / 100
    txB = float(input("Qual a taxa % de crescimento de B? : ")) / 100

    if calcular_populacao(popA, popB, txA, txB):
        repetir = input("Deseja realizar uma nova operação? (S/N): ").strip().upper()
        if repetir != "S":
            break
