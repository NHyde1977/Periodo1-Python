import math

tp = float(input("qual o tamanho da parede a ser pintada (metros quadrados)? "))

cobertura = tp/6 # 1L de tinta cobre 6m
latas = cobertura/18
galao = cobertura/3.6
vlatas = latas*80
vgalao = galao*25


print("Latas necessárias: ", math.ceil(latas))
print("Valor total das latas (1 lata custa 80 reais): R$", math.ceil(vlatas))
print("Gações necessárias: ", math.ceil(galao))
print("Valor total dos galões (1 galão custa 25 reais): R$", math.ceil(vgalao))
print("melhor composição de latas e galões", (cobertura/18), "e", ((math.ceil(cobertura/18)-(cobertura/18))/3.6))
