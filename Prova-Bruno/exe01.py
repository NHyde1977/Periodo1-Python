nome = input("Qual o nome do atleta? ")
idade = int(input("Qual a idade?"))

if idade > 18:
    print(f'{nome} pertence a categoria de Adulto')
elif idade >= 16 and idade < 18:
    print(f'{nome} pertence a categoria Juvenil')
elif idade >= 10 and idade <= 15:
    print(f'{nome} pertence a categoria Junior')
elif idade >= 1 and idade <= 9:
    print(f'{nome} se enquadra na categoria Infantil')
elif idade == 0:
    print(f'{nome} muito pequeno e não pode ser aceito ainda no clube.')

