n = int(input("Digite um número: "))
fat = 1
for i in range(1, n+1):
    fat = fat * i

print(f"O valor do fatorial foi {fat}")