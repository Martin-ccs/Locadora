from ABC import ABC

class Veiculo(ABC):

    def __init__(
                self, 
                placa: str,
                modelo: str,
                ano: int,
                diaria_base: float,
                status: str,
                categoria_cnh_exigida: str
                 ):

        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano
        self.__diaria_base = diaria_base
        self.__status = status
        self.__categoria_cnh_exigida = categoria_cnh_exigida

    @property
    def placa(self):
        return self.__placa

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def diaria_base(self):
        return self.__diaria_base

    @property
    def status(self):
        return self.__status

    @property
    def categoria_cnh_exigida(self):
        return self.__categoria_cnh_exigida

    def calcular_valor_aluguel(self, dias):
        pass

    def esta_disponivel(self):
        pass

    
