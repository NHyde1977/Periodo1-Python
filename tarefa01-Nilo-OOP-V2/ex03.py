class Retangulo:
    """Representa uma peça de piso"""
    def __init__(self, largura: float, altura: float):
        self.__height = altura
        self.__width = largura

    def set_lxa(self, largura, altura):
        """Modifica os valores da largura e altura"""
        self.__height = altura
        self.__width = largura

    def get_lados(self):
        """Retorna a altura e largura"""
        return self.__height, self.__width

    def get_area(self):
        """Calcula a área"""
        return self.__height * self.__width

    def get_perimetro(self):
        """Calcula o perímetro"""
        return 2 * (self.__height + self.__width)


class Local:
    """Representa o ambiente que será forrado com pisos"""
    def __init__(self, largura_local: float, altura_local: float, piso: Retangulo):
        self.__height_local = altura_local
        self.__width_local = largura_local
        self.__piso = piso  # O objeto Retangulo que representa o piso

    def calcular_material(self):
        """Calcula a quantidade de pisos e rodapés necessários"""
        # Quantidade de pisos na largura e altura (sem arredondamento)
        qtd_pisos_largura = self.__width_local / self.__piso.get_lados()[1]
        qtd_pisos_altura = self.__height_local / self.__piso.get_lados()[0]

        # Quantidade total de pisos
        qtd_pisos = qtd_pisos_largura * qtd_pisos_altura

        # Perímetro do local para calcular rodapé
        perimetro = 2 * (self.__height_local + self.__width_local)

        return qtd_pisos, perimetro


# **Programa Principal**
# Entrada do usuário
largura_local = float(input("Digite a largura do local (m): "))
altura_local = float(input("Digite a altura do local (m): "))

largura_piso = float(input("Digite a largura de uma peça de piso (m): "))
altura_piso = float(input("Digite a altura de uma peça de piso (m): "))

# Criamos o objeto piso com a classe Retangulo
piso = Retangulo(largura_piso, altura_piso)

# Criamos o local
local = Local(largura_local, altura_local, piso)

# Calculamos a quantidade de materiais necessários
pisos, rodapes = local.calcular_material()

# Exibimos os resultados
print(f"\nQuantidade de peças de piso necessárias: {pisos:.2f}")
print(f"Quantidade de rodapés necessários: {rodapes:.2f} metros")
