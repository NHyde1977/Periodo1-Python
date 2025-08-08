class Funcionario:
    def __init__(self, nome = None, salario = None):
        self.__name = nome
        self.__salary = salario

    def cadastrarnome(self, nomefuncionario):
        self.__name = nomefuncionario

    def cadastarsalario(self, salario):
        self.__salary = salario

    def aumento(self, aumentoperc):
        self.__salary = self.__salary * (1+aumentoperc)