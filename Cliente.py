from Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self,
                 numero_cnh: str,
                 categoria_cnh: str,
                 validade_cnh: str,
                 locacoes: list,
                 ):

        super().__init__(nome, cpf)

        self.__numero_cnh = numero_cnh
        self.__categoria_cnh = categoria_cnh
        self.__validade_cnh = validade_cnh
        self.__locacoes = locacoes


    @property
    def numero_cnh(self):
        return self.__numero_cnh

    @property
    def categoria_cnh(self):
        return self.__categoria_cnh

    @property
    def validade_cnh(self):
        return self.__validade_cnh

    @property
    def locacoes(self):
        return self.__locacoes

    def cnh_validade(self, data):
        pass

    def pode_dirigir(self, veiculo, data):
        pass