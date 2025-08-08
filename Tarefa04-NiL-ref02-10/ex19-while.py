numeros = [int(input(f'Digite o {i+1}º número [entre 0 e 1000]: ')) for i in range(4)]
maior = max(numeros)
menor = min(numeros)
status = False

while status == False:
    if any(n < 0 or n > 1000 for n in numeros):
        print("Um ou mais números fora do intervalo de zero a 100")
        status = False
    else:
        maior = max(numeros)
        menor = min(numeros)
        print(f"Maior Número: {maior}\nMenor Número: {menor}")
        status = True