from Veiculo import Veiculo

class Utilitario(Veiculo):
    
    def __init__(
                self, 
                capacidade_carga_kg: float,
                placa: str,
                modelo: str,
                ano: int,
                diaria_base: float,
                status: str,
                categoria_cnh_exigida: str
                 ):

        super().__init__(placa, modelo, ano, diaria_base, status, categoria_cnh_exigida)

        self.__capacidade_carga_kg = capacidade_carga_kg

    @property
    def capacidade_carga_kg(self):
        return self.__capacidade_carga_kg