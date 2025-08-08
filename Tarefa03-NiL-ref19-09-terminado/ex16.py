import math
a = float(input("indique um número"))

if a == 0:
    print("a equação não é do segundo grau")
else:
    b = float(input("indique um outro número"))
    c = float(input("indique um outro número"))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("a equação possui não tem raiz real")
    elif delta == 0:
        x1 = -b / (2*a)
        print("a equação possui uma raiz: ", x1)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("A equação possui duas raízes: ", x1, x2)