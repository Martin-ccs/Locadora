from Veiculo import Veiculo 

class Moto(Veiculo):

    def __init__(
                self, 
                cilindradas: int,
                placa: str,
                modelo: str,
                ano: int,
                diaria_base: float,
                status: str,
                categoria_cnh_exigida: str
                 ):

        super().__init__(placa, modelo, ano, diaria_base, status, categoria_cnh_exigida)

        self.__cilindradas = cilindradas

    @property
    def cilindradas(self):
        return self.__cilindradas
    