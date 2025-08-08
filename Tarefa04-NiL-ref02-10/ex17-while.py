#n = int(input("Digite um número: "))
#fat = 1
#for i in range(1, n+1):
#    fat = fat * i
#print(f"O valor do fatorial foi {fat}")

n = int(input("Digite um número: "))
fat = 1
i = 1
while i <= n:
    fat = fat * i
    i = i + 1
print(f"O valor do fatorial foi {fat}")