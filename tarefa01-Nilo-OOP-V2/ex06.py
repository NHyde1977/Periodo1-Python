class TV:
    def __init__(self, canal=1, volumetv=5):
        self.__channel = canal if 1 <= canal <= 13 else 1 #tal do operador ternário.
        self.__volume = volumetv if 0 <= volumetv <= 10 else 5

    def alterar_canal(self, canal):
        if 1 <= canal <= 13:
            self.__channel = canal
        else:
            print("Canal inválido! Escolha um canal entre 1 e 13.")

    def alterar_volume(self, volumetv):
        if 0 <= volumetv <= 10:
            self.__volume = volumetv
        else:
            print("Volume inválido! Escolha um valor entre 0 e 10.")

    def aumentar_volume(self):
        if self.__volume < 10:
            self.__volume += 1
        else:
            print("Volume máximo atingido!")

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print("Volume mínimo atingido!")

    def get_status(self):
        return f"Canal: {self.__channel}, Volume: {self.__volume}"
