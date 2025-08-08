maca = float(input("Quantos quilos de maçã deseja? "))
morango = float(input("Quantos quilos de morango deseja? "))

pma1 = 1.8
pmo1 = 2.5
pma2 = 1.5
pmo2 = 2.2
desc = 0.9
tkg = (maca + morango)


if maca <= 5 and morango <= 5 :
    if tkg > 8 and ((maca * pma1)+(morango * pmo1) <=25):
        print("total de maça R$ ", maca * pma1, "total de morango R$ ", morango * pmo1)
    elif ((maca * pma1)+(morango * pmo1) >25):
        print("total de maça R$ ", ((maca * pma1) * desc), "total de morango R$ ", (morango * pmo1) * desc)
    else:
        print("Dado inválido")
elif maca <= 5 and morango > 5:
    if tkg > 8 and ((maca * pma1)+(morango * pmo2) <=25):
        print("total de maça R$ ", maca * pma1, "total de morango R$ ", morango * pmo2)
    elif ((maca * pma1) + (morango * pmo2) > 25):
        print("total de maça R$ ", ((maca * pma1) * desc), "total de morango R$ ", (morango * pmo2) * desc)
    else:
        print("Dado inválido")
    #print(("total de maça R$ ",maca * pma1), ("total de morango R$ ", morango * pmo2))
elif maca > 5 and morango <= 5:
    if tkg > 8 and ((maca * pma2)+(morango * pmo1) <=25):
        print("total de maça R$ ", maca * pma2, "total de morango R$ ", morango * pmo1)
    elif ((maca * pma2) + (morango * pmo1) > 25):
        print("total de maça R$ ", ((maca * pma2) * desc),"total de morango R$ ", (morango * pmo1) * desc)
    else:
        print("dado inválido")
    #print(("total de maça R$ ",maca * pma2), ("total de morango R$ ", morango * pmo1))
elif maca > 5 and morango > 5:
    if tkg > 8 and ((maca * pma2)+(morango * pmo2) <=25):
        print("total de Maça R$ ", maca * pma2, "total de morango R$ ", morango * pmo2)
    elif (maca * pma2) + (morango * pmo2)  > 25:
        print("total de maça R$ ", (maca * pma2) * desc, "total de morango R$ ", (morango * pmo2)*desc)
    else:
        print("Dado inválido")
    #print(("total de maça R$ ",maca * pma2), ("total de morango R$ ", morango * pmo2))
else:
    print("resultado inválido")