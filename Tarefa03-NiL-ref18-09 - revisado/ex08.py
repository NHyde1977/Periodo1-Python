prod1 = float(input("indique o preço do produto 1: "))
prod2 = float(input("indique o preço do produto 2: "))
prod3 = float(input("indique o preço do produto 3: "))

p1 = "produto 1"

if (prod1 < prod2) and (prod1 < prod3):
    print("O produto mais barato é de preço :", prod1, p1)
elif (prod2 < prod1) and (prod2 < prod3):
        print("O produto mais barato é de preço:", prod2)
elif (prod3 < prod1) and (prod3 < prod2):
        print("O produto mais barato é de preço:", prod3)

else:
    print("Há dois ou mais valores de produtos iguais")