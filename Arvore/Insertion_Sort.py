from array import array


def insertion_sort(array):
    for loop_externo in range (1, len(array)): #percorre do segundo elemento até o final
        loop_interno = loop_externo
        while array[loop_interno - 1] > array[loop_interno] and loop_interno > 0:
            #verifica se o elemento da esquerda é maior que o atual
            #o "loop_interno > 0" evita que o índice fique negativo e a função pegue o último da lista.
            array[loop_interno - 1], array[loop_interno] = array[loop_interno], array[loop_interno - 1]
            #troca a posição se menor
            loop_interno -= 1
            #vai "voltando" um passo na lista, comparando com os elementos anteriores até achar valor menor
            #ou o início da lista

array = [2, 2, 2, 6, 5, 1, 3, 4]
insertion_sort(array)
print(array)