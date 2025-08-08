# Repetições do supino
# coach prof Bruno
# 4 séries, 8 rep de 30kg

series = 4
rep = 8
peso = 30

conta_serie = 0
conta_rep = 0

for i in (range(series)):
    conta_rep = 0
    conta_serie = conta_serie + 1
    print(f"série {conta_serie}")
    for j in (range(rep)):
        conta_rep = conta_rep +1
        print(f"repetição {conta_rep} - supino de peso {peso}")