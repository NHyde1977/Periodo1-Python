from collections import Counter

p1 = input("Telefonou para a vítima? S/N")
p2 =input("Esteve no local do crime? S/N")
p3 = input("Mora perto da vítima? S/N")
p4 = input("Devia para a vítima? S/N")
p5 = input("Já trabalhou com a vítima? S/N")

res = [p1,p2,p3,p4,p5]
counter = Counter(res)

if counter == {'n': 3, 's': 2}:
    print("suspeita")
elif counter == {'n': 2, 's': 3} or counter == {'n': 1, 's': 4}:
    print("Cúmplice")
elif counter == {'s': 5}:
    print("Assassino")
else:
    print("respostas inválidas")
print(counter)