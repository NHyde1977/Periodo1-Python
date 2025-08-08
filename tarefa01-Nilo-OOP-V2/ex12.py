class ContaInvestimento:
    def __init__(self, num_conta, correntista, saldo=1000, juros=10):
        self.__accnumber = num_conta
        self.__nameholder = correntista
        self.__balance = saldo
        self.__interest = juros

    def aplicarjuros(self):
        self.__balance += self.__balance * (self.__interest / 100)

    def saldoatual(self):
        print(f"Saldo: {self.__balance}")


contanova = ContaInvestimento(1,'Cliente1', 1000, 10)

contanova.aplicarjuros()
contanova.aplicarjuros()
contanova.aplicarjuros()
contanova.aplicarjuros()

contanova.saldoatual()