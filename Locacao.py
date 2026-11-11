

class Locacao:

    def __init__(
                 self,
                 id: int,
                 data_prevista: Date,
                 data_prevista_devolucao: Date,
                 data_devolucao_real: Date,
                 valor_total: float,
                 status: str
                 ):

        self.__id = id
        self.__data_prevista = data_prevista
        self.__data_prevista_devolucao = data_prevista_devolucao
        self.__data_devolucao_real = data_devolucao_real
        self.__valor_total = valor_total
        self.__status = status

    @property
    def id(self):
        return self.__id

    @property
    def data_prevista(self):
        return self.__data_prevista

    @property
    def data_prevista_devolucao(self):
        return self.__data_prevista_devolucao

    @property
    def data_devolucao_real(self):
        return self.__data_devolucao_real

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def status(self):
        return self.__status

    def dias_previstos(self):
        pass

    def calcular_multa(self, data):
        pass

    def finalizar(self, data):
        pass



    