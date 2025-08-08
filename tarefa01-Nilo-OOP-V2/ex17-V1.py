class Porco:
    def __init__(self, fome=5, tedio=0): # Fome e tédio entre 0 e 10
        self.__hungry = max(0, min(fome, 10))
        self.__boredom = max(0, min(tedio, 10))

    def alimentarporco(self, qtdcomida):
        self.__hungry = max(0, self.__hungry - qtdcomida)

    def brincarporco(self, horas):
        self.__boredom = min(10, self.__boredom - horas)

class Galinha:
    def __init__(self, fome=5, tedio=0):
        self.__hungry = max(0, min(fome, 10))  # Fome e tédio entre 0 e 10
        self.__boredom = max(0, min(tedio, 10))

    def alimentargalinha(self, qtdcomida):
        self.__hungry = max(0, self.__hungry - qtdcomida)

    def brincargalinha(self, horas):
        self.__boredom = min(10, self.__boredom - horas)

class Vaca:
    def __init__(self, fome=5, tedio=0):
        self.__hungry = max(0, min(fome, 10))  # Fome e tédio entre 0 e 10
        self.__boredom = max(0, min(tedio, 10))

    def alimentarvaca(self, qtdcomida):
        self.__hungry = max(0, self.__hungry - qtdcomida)

    def brincarvaca(self, horas):
        self.__boredom = min(10, self.__boredom - horas)

