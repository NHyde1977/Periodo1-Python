class Bola:
        def __init__(self, cor=None, circunferencia=None, material=None):
                self.__color = cor
                self.__radius = circunferencia
                self.__mat = material

        def set_color(self, cor):
                self.__color = cor

        def get_color(self):
                return self.__color

        def __str__(self):
                return f"Bola da cor {self.__color}, circunferência {self.__radius}cm e material {self.__mat}."

obj = Bola('branca', '10', 'plástico')
print(obj)