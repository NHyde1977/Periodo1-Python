# class Macaco:
#     def __init__(self, nome, bucho): ideal seria não passar o Bucho, ainda que o valor de None
#         self.__name = nome
#         self.__stomach = bucho

# o macoco pode comer o outro e mais qualquer objeto.

class Macaco:
    def __init__(self, nome):
        self.__nome = nome
        self.__bucho = []  # inicia com uma lista nova, vazia e separada

    def comer(self, comida):
        self.__bucho.append(comida)

    def digerir(self):
        self.__bucho.clear() #apaga tudo da barriga

    def ver_bucho(self):
        print(f"{self.__nome} tem isso na barriga neste exato momento: {self.__bucho}")

macaco1 = Macaco("Tião")
macaco2 = Macaco("Kong")

# macaco1.comer("Banana", "Maçã", "Pera")
# macaco1.ver_bucho() >aqui dá erro pq só pode comer 1 coisa de cada vez

macaco1.comer("Banana")
macaco1.ver_bucho()

macaco1.comer("Outra Banana")
macaco1.ver_bucho()

macaco2.comer(macaco1)
macaco2.ver_bucho()

macaco2.comer("Ultraman")
macaco2.ver_bucho()

macaco1.digerir()
macaco1.ver_bucho()

macaco2.digerir()
macaco2.ver_bucho()