import math

# Inicializa o tempo
tempo = 0

# Define os valores iniciais das populações
paisA = 80000 * math.pow(1.03, tempo)
paisB = 200000 * math.pow(1.015, tempo)

# Loop infinito usando itertools.count
for _ in range(100):  # Limite alto para simular um loop potencialmente infinito
    if paisA >= paisB:
        print("Esses são os anos que levam para ter a população semelhante: ", tempo)
        break
    else:
        tempo += 1
        paisA = 80000 * math.pow(1.03, tempo)
        paisB = 200000 * math.pow(1.015, tempo)
