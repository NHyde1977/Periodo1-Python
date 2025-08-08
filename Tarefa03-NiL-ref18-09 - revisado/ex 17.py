ano = int(input("Indique o ano para fazer a validação: "))

if ((ano %4 == 0) and (ano %100 != 0)) or (ano %400 == 0):
    print("esse ano é bissexto")
else:
    print ("esse ano não é bissexto")