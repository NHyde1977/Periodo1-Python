num = int(input("Qual valor você deseja sacar (mínimo R$10, máximo R$600? "))

if (num >10) and (num <600):
    cem = num // 100
    cinq = (num%100) // 50
    dez = ((num - (cem*100) - (cinq*50))%100) // 10
    cin = ((num - (cem*100) - (cinq*50) - (dez*10)%100)) // 5
    um = ((num - (cem*100) - (cinq*50) - (dez*10) - (cin*5))) // 1
    print("notas de 100:", cem, "notas de 50:", cinq, "notas de 10:", dez, "notas de 5:", cin, "notas de 1:", um)
else:
    print("número maior que R$600")