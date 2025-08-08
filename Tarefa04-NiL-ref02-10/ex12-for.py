t = int(input('Digite um valor do número para saber a tabuada: '))

tb = t*1,  t*2, t*3, t*4, t*5, t*6, t*7, t*8, t*9, t*10

if 1 <= t <= 10:
    for i in range(1,11):
        resultado = t * i
        print(f'{t} X {i} = {resultado}')
else:
    print('Erro. Digite um número entre 1 e 10.')