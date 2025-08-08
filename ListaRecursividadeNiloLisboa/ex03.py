# nesse aqui eu empaquei. A primeira opção seria transformar em string e inverter
# mas ai não teria recursividade envolvida...
# a IA sugeriu umar o menor divisor de dezena que no caso é o número 10.

# def inversao (n):
#     if n <10:
#         return n
#     else:
#         return n % 10
#         len(str(n // 10))

def inversao(n):
    if n < 10:
        return n
    else:
        ult_digito = n % 10 # resto da devisão por 1 dezena
        qtd_digitos = len(str(n // 10)) #vê o tamanho do número convertido pra string, excluindo o último número
#calculando só a parte inteira da divisão
        return ult_digito * (10 ** qtd_digitos) + inversao(n // 10)

num = int(input("Digite um número pra inverter: "))
print(f"O número invertido de {num} é {inversao(num)}")