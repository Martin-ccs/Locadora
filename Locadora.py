

class Locadora:

    def __init__(
                 self,
                 nome: str,
                 veiculos: list,
                 clientes: list,
                 funcionarios: list,
                 locacoes: list
                 ):

        self.__nome = nome
        self.__veiculos = veiculos
        self.__clientes = clientes
        self.__funcionarios = funcionarios
        self.__locacoes = [] # é uma composicao.

    @property
    def nome(self):
        return self.__nome

    @property
    def veiculos(self):
        return self.__veiculos

    @property
    def clientes(self):
        return self.__clientes

    @property
    def funcionarios(self):
        return self.__funcionarios

    @property
    def locacoes(self):
        return self.__locacoes

    def cadastrar_veiculo(self, v):
        if not isinstance(v, (Carro, Moto, Utilitario)):
            return ValueError
        self.__veiculos.append(v)



