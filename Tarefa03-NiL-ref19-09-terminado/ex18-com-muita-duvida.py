dia = int(input("indique o dia do mês"))
mes = int(input("indique o número do mês"))
ano = int(input("indique o ano"))

if dia >= 1 and dia <= 31:
    if mes in range(1,13):
        print("data valida: ", dia,"/",mes,"/",ano)
else:
    print("data invalida")