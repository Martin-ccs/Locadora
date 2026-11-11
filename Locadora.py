

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
        pass

    def cadastrar_cliente(self, c):
        pass

    def buscar_veiculo(self, placa):
        pass

    def buscar_cliente(self, cpf):
        pass

    def alugar(self):
        pass

    def devolver(self, id, data):
        pass

    def listar_veiculos_disponiveis(self):
        pass

    def listar_locacoes_ativas(self):
        pass

    def faturamento_total(self):
        pass
    



