#mudar nome, depósito e saque

class ContaCorrente:
    def __init__(self, num_conta, correntista, saldo=0):
        self.__accnumber = num_conta
        self.__nameholder = correntista
        self.__balance = saldo

    def alterar_nome(self, novo_nome):
        self.__nameholder = novo_nome

    def sacar(self, valor):
        if valor > self.__balance:
            print(f"Saldo insuficiente. Seu saldo é: {self.__balance}")
        else:
            self.__balance -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.__balance}")

    def depositar(self, valor):
        self.__balance += valor

    def get_saldo(self):
        return self.__balance

