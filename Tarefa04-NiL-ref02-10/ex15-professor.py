n = 10
a, b=0,1
print(a, end=",")

for _ in range(n-1):
    print(b, end=",")
    a, b = b, a + b