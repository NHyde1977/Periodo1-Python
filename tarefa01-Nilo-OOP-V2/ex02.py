class Quadrado:
    def __init__(self, lado=None):
        self.__side = lado

    def set_side(self, lado):
        self.__side = lado

    def get_area(self):
        return self.__side * self.__side

q = Quadrado(6)
print(q.get_area())